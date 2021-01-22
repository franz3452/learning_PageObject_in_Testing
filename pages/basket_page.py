from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def should_be_basket_url(self):
        assert '/basket/' in self.browser.current_url, 'basket url not found'

    def should_be_empty_basket(self):
        self.should_not_be_goods_in_basket()
        self.should_message_empty_basket()

    def should_be_not_empty_basket(self):
        self.should_be_goods_in_basket()
        self.should_not_message_empty_basket()

    def should_be_goods_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Where're no items in basket"
        assert True

    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Where're items in empty basket"
        assert True
#перепеши тест через if elif else
    def should_message_empty_basket(self):
        assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, 'Empty basket message isnt presented'
        assert True

    def should_not_message_empty_basket(self):
        assert not self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)