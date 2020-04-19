from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import os

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
driver.get(link)
firstName = driver.find_element_by_xpath("//input[@name='firstname']")
lastName = driver.find_element_by_xpath("//input[@name='lastname']")
email = driver.find_element_by_xpath("//input[@name='email']")
downloader = driver.find_element_by_xpath("//input[@type='file']")
button = driver.find_element_by_xpath("//button[@type='submit']")
file = os.path.abspath("X:\hollow.txt")

firstName.send_keys("Name")
lastName.send_keys("lastName")
email.send_keys("email")
downloader.send_keys(file)
button.click()



