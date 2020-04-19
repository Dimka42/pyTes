import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")
button = driver.find_element_by_xpath("//button[@id='book']")
price = WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "100")
)
button.click()
x = driver.find_element_by_xpath("//span[@id='input_value']").text
needInput = driver.find_element_by_xpath("//input[@id='answer']")
answerButton = driver.find_element_by_xpath("//button[@id='solve']")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
needInput.send_keys(y)
answerButton.click()
