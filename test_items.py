import pytest


def test_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button.is_displayed, "Button is not found!"
