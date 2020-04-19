from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    firstName = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
    lastName = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    email = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
    firstName.send_keys("Ivan")
    lastName.send_keys("Ivanov")
    email.send_keys("mail@mail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_xpath("//span[@id='input_value']").text
searchInput = browser.find_element_by_xpath("//input[@id='answer']")
soloCheckBox = browser.find_element_by_xpath("//label[@for='robotCheckbox']")
needsRadioButton = browser.find_element_by_xpath("//input[@id='robotsRule']")
needsButton = browser.find_element_by_xpath("//button[@type='submit']")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
searchInput.send_keys(y)
soloCheckBox.click()
needsRadioButton.click()
needsButton.click()
browser.quit()
