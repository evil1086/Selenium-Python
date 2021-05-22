import inspect

import pytest
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    #def __init__(self, driver):
     #   self.driver = driver

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

    def screen_capture(self):
        self.driver.get_screenshot_as_file("success.png")
