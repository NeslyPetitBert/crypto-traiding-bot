import ftx
import pandas as pd
import ta
import time
import json
from math import *

from modules.logger.logger import Logger
from modules.mailer.mailer import Mailer
from modules.sms.sms import SMS

accountName = 'FTX_ma28_ma48_rsi_beta'
pairSymbol = 'BTC/USD'
fiatSymbol = 'USD'
cryptoSymbol = 'BTC'
myTruncate = 3

client = ftx.FtxClient(api_key='cle_api_du_sous_compte_a_utiliser',
                   api_secret='cle_secret_api_du_sous_compte_a_utiliser', subaccount_name=accountName)

data = client.get_historical_data(
    market_name=pairSymbol, 
    resolution=3600, 
    limit=1000, 
    start_time=float(
    round(time.time()))-100*3600, 
    end_time=float(round(time.time())))
df = pd.DataFrame(data)

df['EMA28']=ta.trend.ema_indicator(df['close'], 28)
df['EMA48']=ta.trend.ema_indicator(df['close'], 48)
df['STOCH_RSI']=ta.momentum.stochrsi(df['close'])
#print(df)

def getBalance(myclient, coin):
    jsonBalance = myclient.get_balances()
    if jsonBalance == []: 
        return 0
    pandaBalance = pd.DataFrame(jsonBalance)
    Logger.logger_info('Balance details : \n'+ pandaBalance.to_string() + '\n')
    if pandaBalance.loc[pandaBalance['coin'] == coin].empty: 
        return 0
    else: 
        return float(pandaBalance.loc[pandaBalance['coin'] == coin]['total'])

def truncate(n, decimals=0):
    r = floor(float(n)*10**decimals)/10**decimals
    return str(r)
    
fiatAmount = getBalance(client, fiatSymbol)
cryptoAmount = getBalance(client, cryptoSymbol)
actualPrice = df['close'].iloc[-1]
minToken = 5/actualPrice
print('coin price :',actualPrice, 'usd balance', fiatAmount, 'coin balance :',cryptoAmount, '\n')

if df['EMA28'].iloc[-2] > df['EMA48'].iloc[-2] and df['STOCH_RSI'].iloc[-2] < 0.8:
    if float(fiatAmount) > 5:
        quantityBuy = truncate(float(fiatAmount)/actualPrice, myTruncate)
        
        Mailer.mailer("Purchasse order", "Your "+ cryptoSymbol + " purchase order was successful")
        SMS.send_sms("Purchasse order : Your "+ cryptoSymbol + " purchase order was successful")
        Logger.logger_info("Purchasse order : Your "+ cryptoSymbol + " purchase order was successful")

        buyOrder = client.place_order(
            market=pairSymbol, 
            side="buy", 
            price=None, 
            size=quantityBuy, 
            type='market')
        print("BUY", buyOrder + "\n")
    else:
        buying_message = "The market is trending up, but you don't have enough " + fiatSymbol + " to place buy orders for " + cryptoSymbol
        Mailer.mailer("Uptrend", buying_message)
        SMS.send_sms("Uptrend : " + buying_message)
        Logger.logger_info("Uptrend : " + buying_message)

elif df['EMA28'].iloc[-2] < df['EMA48'].iloc[-2] and df['STOCH_RSI'].iloc[-2] > 0.2:
    if float(cryptoAmount) > minToken:

        Mailer.mailer("Sell order", "Your "+ cryptoSymbol + " sell order was successful")
        SMS.send_sms("Sell order : Your "+ cryptoSymbol + " sell order was successful")
        Logger.logger_info("Sell order : Your "+ cryptoSymbol + " sell order was successful")
        
        sellOrder = client.place_order(
            market=pairSymbol, 
            side="sell", 
            price=None, 
            size=truncate(cryptoAmount, myTruncate), 
            type='market')
        print("SELL", sellOrder)
    else:
        selling_message = "The market is trending down, but you don't have " + cryptoSymbol + " to place sell orders."
        Mailer.mailer("Bearish trend", selling_message)
        SMS.send_sms("Bearish trend : " + selling_message)
        Logger.logger_info("Bearish trend : " + selling_message)
else :
  no_order_message = 'No opportunity to take, none of the conditions are met to issue a buy or sell order on ' + cryptoSymbol
  Mailer.mailer('Neutral', no_order_message)
  SMS.send_sms('Neutral : ' + no_order_message)
  Logger.logger_info('Neutral : ' + no_order_message)
