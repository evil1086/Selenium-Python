import inspect
import logging


class BaseClass:

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        # it will invokes the files name in which we want to store the logs
        filehandler = logging.FileHandler("logfile.log")
        logger.addHandler(filehandler)
        # This will prepare log format
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        # Creation of link between the log formatter and file handler
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        return logger
