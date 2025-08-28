import logging

from logging.handlers import RotatingFileHandler
from core.config import settings

class Logger:
    DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    def __init__(self,filename="logs/app.log"):
        logging.basicConfig(filename=filename,
                level=logging.DEBUG, 
                format=self.DEFAULT_FORMAT)

    def log_info(self,job):
        logging.debug(f"INFO: {job}")

