import pytest
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestGoodPage():
    def test_btn_add_good_to_cart_exists(self, browser):
        browser.get(link)
        #time.sleep(10)
        btn_add_to_cart = len(browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket'))
        assert btn_add_to_cart == 1, 'Элемент не найден'
