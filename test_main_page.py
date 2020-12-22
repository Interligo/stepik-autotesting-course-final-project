from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
