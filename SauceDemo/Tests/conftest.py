from selenium import webdriver
from urllib import request
import pytest


# To enable command line browser invocation, we are using this
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    # This will invoke the specified browser from the command line
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(r"C:\Users\vin\PycharmProjects\seleniumTest01\Browsers\chromedriver.exe")

    elif browser_name == "IE":
        pass
    elif browser_name == "firefox":
        pass

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
