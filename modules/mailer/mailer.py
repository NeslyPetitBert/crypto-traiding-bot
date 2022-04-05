import smtplib

from modules.config.config import EmailConfig
from modules.logger.logger import Logger

EmailConfig.read_from_file()

class Mailer:
    def mailer(subject: str, msg: str) -> None:
        try:
            server = smtplib.SMTP(EmailConfig.HOST+':'+EmailConfig.PORT)

            server.ehlo()
            server.starttls()
            server.login(EmailConfig.SENDER_EMAIL_ADDRESS, EmailConfig.PASSWORD)
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(EmailConfig.SENDER_EMAIL_ADDRESS, EmailConfig.RECIPIENT_EMAIL_ADDRESS, message)
            server.quit()
            Logger.logger_info("Success: Your email has been sent!")
        except:
            Logger.logger_critical("Error : Your email was not sent")