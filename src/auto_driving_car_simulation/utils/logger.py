import logging
from ..config.config import Config


class Logger:
    """
    Class to handle logging setup and configuration.
    """

    @staticmethod
    def setup_logger(name: str):
        """
        Set up the logger with the specified name.

        Args:
            name (str): Name of the logger.

        Returns:
            logger (logging.Logger): Configured logger instance.
        """
        logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        formatter = Config.LOGGING_FORMAT
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(Config.LOGGING_LEVEL)
        return logger
