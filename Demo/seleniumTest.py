import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"C:\Users\vin\PycharmProjects\seleniumTest01\Browsers\chromedriver.exe")


driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


driver.get("https://www.amazon.in")
driver.minimize_window()
print(driver.current_url)
driver.back()

# Css selector : Tagname[Attribute = 'value']
# in  the browser $("Tagname[Attribute = 'value']")
# RegEx: [Attribute* = 'value']
# If ID is available then we can use : "Attribute#id"
driver.find_element_by_css_selector("input[name='q']").click()
print('css selector is working as expected')

# when multiple class is present : $("[class* = 'classname']") ---- In browser
driver.find_element_by_css_selector("[class='gLFyf gsfi']").send_keys("Yahoo")
# Xpath: //Tagname[@Attribute = "value"]
# in the browser $x("//tagname[@Attribute= 'value']")
# RegEx: //*[Contains(@Attribute, 'value')]
driver.find_element_by_xpath("//input[@name='q']").click()
print('Xpath is working perfectly fine')

driver.get("https://login.salesforce.com/?locale=in")
driver.find_element_by_css_selector("input#username").send_keys("vinod")
print('able to find username with tagname#id method')
driver.find_element_by_css_selector("input.password").send_keys("Pawar")
print('able to find password using tagname.classname')
driver.find_element_by_link_text("Forgot Your Password?").click()
print('clicked on the forget password link')
driver.implicitly_wait(10)
# using the text we can use xpath  --- > "//tagname[text() = 'text_to_search']"
driver.find_element_by_xpath("//a[text() = 'Cancel']").click()
print('generating xpath using text working fine')

# using the parent tag we can create xpath - //tagname[@Attribute = 'value']/childTag
driver.find_element_by_xpath("//div[@id = 'usernamegroup']/label").text

messsage = driver.find_element_by_css_selector("form[name = 'login'] label").text

assert "Username" in messsage

driver.get("http://demo.guru99.com/test/newtours/register.php")
# Using selecct tag to select value from the drop down

dropdown = Select(driver.find_element_by_name("country"))
dropdown.select_by_visible_text('ALGERIA')
print("Drop down selection is working with the select tag")


driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_css_selector("input[id = 'autosuggest']").send_keys("Ind")
time.sleep(2)

# this line capture dynamic suggested values from the drop down
countries = driver.find_elements_by_css_selector("li[class = 'ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country == "India":
        country.click()
        break

driver.find_element_by_id("autosuggest").text

# to capture values which appear dynamically we use get_attribute method
assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"
print('Assertion works as expected')




driver.close()
