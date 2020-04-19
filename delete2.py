import math

from selenium import webdriver

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
driver.get(link)

button = driver.find_element_by_xpath("//button[@type='submit']")
button.click()
needWindow = driver.window_handles[1]
driver.switch_to.window(needWindow)
x = driver.find_element_by_xpath("//span[@id='input_value']").text



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
needInput = driver.find_element_by_xpath("//input[@class='form-control']")
needInput.send_keys(y)
needButton = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
needButton.click()
