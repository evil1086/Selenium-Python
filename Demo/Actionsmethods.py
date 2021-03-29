from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(r"C:\Users\vin\PycharmProjects\seleniumTest01\Browsers\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
mouse_hover = driver.find_element_by_css_selector("button[id = 'mousehover']")
action.move_to_element(mouse_hover).perform()
child_menu = driver.find_element_by_link_text("Top")
action.move_to_element(child_menu).click().perform()

# It will redirect on below URL
driver.get("http://demo.guru99.com/test/simple_context_menu.html")

# dbl_click = driver.find_element_by_xpath("//button[text() = 'Double-Click Me To See Alert']")
action.double_click(driver.find_element_by_xpath("//button[contains(text(),'Double-Click Me To See Alert']")).perform()
alert = driver.switch_to.alert

temp = alert.text

assert temp == "You double clicked me.. Thank You.."

print("assertion working as expected")
print("Test")
driver.close()
