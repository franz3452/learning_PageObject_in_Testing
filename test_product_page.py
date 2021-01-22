import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time

product_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_good_to_cart(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.add_good_to_cart_btn()
    page.solve_quiz_and_get_code()
    page.should_good_added_to_cart()


@pytest.mark.parametrize('n_offer',[pytest.param(i, marks=pytest.mark.xfail(i==7, reason='не будет исправлдено')) for i in range(10)])
def test_link_param_offer(browser, n_offer):
    page = ProductPage(browser, product_page_link+'?promo=offer{}'.format(n_offer))
    page.open()
    page.add_good_to_cart_btn()
    page.solve_quiz_and_get_code()
    page.should_good_added_to_cart()

def test_guest_should_see_login_link_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.new
def test_guest_should_be_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()