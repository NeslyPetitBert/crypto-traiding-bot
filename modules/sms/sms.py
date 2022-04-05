import requests

from modules.sms.config import SmsConfig
from modules.logger.logger import Logger

User = SmsConfig.USER
Pass = SmsConfig.PASS
Url = SmsConfig.URL
Msg = SmsConfig.MSG


class SMS:
    def send_sms(custom_msg: str) -> None:
        try:
            response = requests.get(Url+f'user={User}&pass={Pass}&msg={custom_msg}')
            if response.status_code == 200:
                Logger.logger_info("Success: Your sms has been sent!")
            elif response.status_code == 400:
                Logger.logger_info("Error: One of the mandatory parameters is missing.")
            elif response.status_code == 402:
                Logger.logger_info("Error: Too many SMS were sent in too little time.")
            elif response.status_code == 403:
                Logger.logger_info("Error: The service is not activated on the subscriber area, or incorrect login / key.")
            elif response.status_code == 500:
                Logger.logger_info("Server side error. Please try again later.")
            else:
                Logger.logger_info("Error : Your sms was not sent")
        except Exception as e:
            Logger.logger_critical("Error : An unexpected error has occurred")