# import logging
# from logging import config
# import pkg_resources

# log_dir = "logs"
# os.makedirs(log_dir, exist_ok=True)

# class Logger:

#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Logger, cls).__new__(cls)
#             cls._instance.__init__()
#         return cls._instance

#     def __init__(self):
#         config.fileConfig('logging.conf')
    
#     def get_logger(name):
#         return logging.getLogger(name)


# logger = Logger()


################
import logging
import os
from datetime import datetime
from Config import Config


class Logger:
    """Singleton Logger Class to handle API logging dynamically per month."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
            cls._instance._setup_logger()
        return cls._instance

    def _setup_logger(self):
        # Ensure the logs directory exists
        log_dir = f"{Config.LOGS_PATH.value}/logs"
        os.makedirs(log_dir, exist_ok=True)

        # Get the current month and generate a log file name
        current_month = datetime.now().strftime("%Y-%m")
        log_file = os.path.join(log_dir, f"log_{current_month}.log")

        # Configure the logger
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='{"time": "%(asctime)s", "level": "%(levelname)s", "module": "%(module)s", "message": %(message)s}',
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Create a logger instance
        self.logger = logging.getLogger("Logger")

    def get_logger(self):
        return self.logger

logger = Logger()

# Example usage in your API
# if __name__ == "__main__":
#     logger = Logger().get_logger()
#     logger.info("API started successfully.")
#     logger.error("Sample error log for testing.")