# execute_bot_and_take_profit
FTX crypto Market bot with python
 * Edit 'modules/config/email.config.json' file with your personal information
 * Edit 'ftx_ma28_ma48_rsi_beta_btc.py' file with your personal information 'accountName and client'
 * Finally, call or type python 'ftx_ma28_ma48_rsi_beta_btc.py' to execute this program

# A personaliser : 
    # modules\config\email.config.json
        # "RECIPIENT_EMAIL_ADDRESS": "",
        # "SENDER_EMAIL_ADDRESS": "",
        # "PASSWORD": "", (NB : il s'agit du mot de passe application si webmail et 2fa)
    # modules\sms\config.py
        # voir les pages : 
            # https://www.universfreebox.com/article/26337/Nouveau-Free-Mobile-lance-un-systeme-de-notification-SMS-pour-vos-appareils-connectes
            # Activer l'option depuis son espace abonné et récupérer l'user, le mot de passe
    # betaEMAcrossRSI_FtxBTC.py
    # betaEMAcrossRSI_FtxBTC.py
        # Pour l'instant, un fichier par paire à optimiser pour que le même fichier soit utilisé pour l'ensemble des paires à trader.
        # accountName = 'le_nom_du_sous_compte_a_utiliser'
        # pairSymbol = 'BTC/USD'
        # fiatSymbol = 'USD'
        # cryptoSymbol = 'BTC'
        # myTruncate = 3
        # Toutes les valeurs sont personnalisables.
        # api_key (à personnaliser)
        # secret_key (à personnaliser)
        # https://help.ftx.com/hc/en-us/articles/360043498812-Subaccounts