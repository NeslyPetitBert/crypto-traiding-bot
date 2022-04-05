import logging
import sys

logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

logHandler = logging.StreamHandler(sys.stdout)
# logHandler.setLevel(logging.DEBUG)

# create a logging format
logging.basicConfig(
    level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s- %(message)s'
)

class Logger:
    def logger_info(message: str):
        logger.info(message)

    def logger_critical(message: str):
        logger.critical(message)