from selenium import webdriver



driver = webdriver.Chrome(r"C:\Users\vin\PycharmProjects\seleniumTest01\Browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello JS")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute('value'))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shop = driver.find_element_by_xpath("//a[contains(text(), 'Shop')]")
# driver.find_element_by_css_selector("a[href*='shop']")
# Click event by javascript
driver.execute_script("arguments[0].click();", shop)
# Scrolling by javascript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.close()
