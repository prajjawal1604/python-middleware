import logging
import os
from datetime import datetime
from Config import Config


class Logger:
    """Singleton Logger Class with General Logging Format."""
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

        # General logging format
        log_format = (
            "%(asctime)s | %(levelname)s | %(module)s | "
            "message=%(message)s | process=%(process)d | thread=%(threadName)s"
        )

        # Configure the logger
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format=log_format,
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        self.logger = logging.getLogger("GeneralLogger")

    def get_logger(self):
        return self.logger


logger = Logger()

# Example usage
if __name__ == "__main__":
    log = Logger().get_logger()
    log.info("Application started successfully.")
    log.warning("This is a warning message.")
    log.error("An error occurred while processing.")
    log.info({"event": "User login"})
