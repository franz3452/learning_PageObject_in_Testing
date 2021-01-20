import pytest
from pages.product_page import ProductPage
import time

product_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_good_to_cart(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.add_good_to_cart_btn()
    page.solve_quiz_and_get_code()
    page.should_good_added_to_cart()

@pytest.mark.new
@pytest.mark.parametrize('n_offer',[pytest.param(i, marks=pytest.mark.xfail(i==7, reason='не будет исправлдено')) for i in range(10)])
def test_link_param_offer(browser, n_offer):
    page = ProductPage(browser, product_page_link+'?promo=offer{}'.format(n_offer))
    page.open()
    page.add_good_to_cart_btn()
    page.solve_quiz_and_get_code()
    page.should_good_added_to_cart()