import logging

class CustomFormatter(logging.Formatter):

    yellow = "\x1b[38;2;218;165;32m"  
    cyan_blue = "\x1b[38;2;0;255;255m" 
    soft_green = "\x1b[38;2;173;255;47m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "[%(name)s %(asctime)s](%(filename)s:%(lineno)d) %(levelname)s: %(message)s"

    FORMATS = {
        logging.DEBUG: soft_green + format + reset,
        logging.INFO: cyan_blue + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%H:%M:%S") 
        return formatter.format(record)

logger = logging.getLogger("SMS")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)
