from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(r"C:\Users\vin\PycharmProjects\seleniumTest01\Browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//a[contains(text(), 'Shop')]").click()
products = driver.find_elements_by_xpath("//div[@class = 'card h-100']")
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()


driver.find_element_by_xpath("//a[contains(text(), 'Checkout')]").click()

products_in_cart = driver.find_elements_by_xpath("media-heading")

#assert productName == products_in_cart

driver.find_element_by_xpath("//button[contains(text(), 'Checkout' )]").click()
driver.find_element_by_id("country").send_keys("ind")

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))

driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class = 'checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[value = 'Purchase']").click()
success_msg = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in success_msg

driver.get_screenshot_as_file("success.png")





