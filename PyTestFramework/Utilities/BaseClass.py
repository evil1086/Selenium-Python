import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import inspect
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_presence(self, text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def screen_capture(self):
        self.driver.get_screenshot_as_file("success.png")

    def selectdropdown(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

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

