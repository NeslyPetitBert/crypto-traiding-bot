import json


class EmailConfig:
    HOST = ''
    PORT = ''
    RECIPIENT_EMAIL_ADDRESS = ''
    SENDER_EMAIL_ADDRESS = ''
    PASSWORD = ''
    SUBJECT = ''
    MESSAGE = ''

    @staticmethod
    def read_from_file() -> None:
        """
        Loads configuration from config/config.json file.
        Call this method before using the class.

        :return: None
        """
        with open('modules/config/email.config.json') as fp:
            json_dict = dict(json.load(fp))
            EmailConfig.HOST = str(json_dict.get('HOST', EmailConfig.HOST))
            EmailConfig.PORT = str(json_dict.get('PORT', EmailConfig.PORT))
            EmailConfig.RECIPIENT_EMAIL_ADDRESS = str(json_dict.get('RECIPIENT_EMAIL_ADDRESS', EmailConfig.RECIPIENT_EMAIL_ADDRESS))
            EmailConfig.SENDER_EMAIL_ADDRESS = str(json_dict.get('SENDER_EMAIL_ADDRESS', EmailConfig.SENDER_EMAIL_ADDRESS))
            EmailConfig.PASSWORD = str(json_dict.get('PASSWORD', EmailConfig.PASSWORD))
            EmailConfig.SUBJECT = str(json_dict.get('SUBJECT', EmailConfig.SUBJECT))
            EmailConfig.MESSAGE = str(json_dict.get('MESSAGE', EmailConfig.MESSAGE))

