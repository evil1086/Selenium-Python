from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\vin\PycharmProjects\seleniumTest01\Browsers\chromedriver.exe")
print("sample TC has been started")
driver.maximize_window()
driver.get("https://www.google.com")
print("google search element found")
gmail_element = driver.find_element_by_name("q")
gmail_element.send_keys("myntra")
print("search for the element")
time.sleep(5)
search_element = driver.find_element_by_class_name("gNO89b").send_keys(Keys.ENTER)
time.sleep(5)
print("sample TC has been finished")
driver.close()

