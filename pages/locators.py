from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#invalid_class_for_login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')

    NAME_OF_THE_BOOK = (By.CSS_SELECTOR, '.product_main >h1')

    SUCCESS_MESSAGE_WITH_GOOD_NAME = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in > div > strong')

    COAST_OF_THE_BOOK = (By.CSS_SELECTOR, '.product_main >p.price_color')

    SUM_OF_THE_CART = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs')