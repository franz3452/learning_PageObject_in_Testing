from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_good_to_cart_btn(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        btn.click()

    def name_of_bought_book(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_THE_BOOK)
        return name_of_book.text

    def coast_of_the_book(self):
        coast_of_the_book = self.browser.find_element(*ProductPageLocators.COAST_OF_THE_BOOK)
        return coast_of_the_book.text.split()[0]

#ожидаемые результаты

    def should_good_added_to_cart(self):
        self.should_message_good_add_to_cart()

        self.should_message_cart_coast()

    def should_message_good_add_to_cart(self):

        assert self.name_of_bought_book() == self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_WITH_GOOD_NAME).text, 'Название добавленной книги не совпадает с сообщ' \
                                                                       'нием о добавлении в корзину'
        assert True

    def should_message_cart_coast(self):

        assert self.coast_of_the_book() in \
               self.browser.find_element(*ProductPageLocators.SUM_OF_THE_CART).text, 'Цена товара не обновилась'
        assert True
