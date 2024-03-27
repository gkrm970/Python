import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        """
        Generates a logger object for logging purposes.

        Returns:
            logger (logging.Logger): The logger object for logging messages.
        """
        path = os.path.abspath(os.curdir) + "\\logs\\automation.log"
        logging.basicConfig(
            filename=path,
            format="%(asctime)s: %(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
        )
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger


logger = LogGen.loggen()
