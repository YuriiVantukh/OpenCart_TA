import pytest

from helpers.constants import Outputs
from pages.cart import CartPage
from pages.home import HomePage
from pages.base import GreyCartBtn
from pages.product import ProductPage

NEW_PRODUCT_QUANTITY = 2
NEW_PRODUCT_PRICE = 200.00
SET_TOO_MUCH_PRODUCT = 999


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-7')
@pytest.allure.CRITICAL
@pytest.mark.dependency(name="1")
@pytest.mark.run(order=1)
def test_check_default_cart_empty(login_setup):
    driver = login_setup
    with pytest.allure.step('Testing that Cart is empty by default'):
        GreyCartBtn(driver)\
            .click_btn_grey_cart()\
            .is_cart_btn_empty()


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-7')
@pytest.allure.NORMAL
@pytest.mark.dependency(name="2", depends=["1"])
@pytest.mark.run(order=2)
def test_add_product_to_cart(login_setup):
    driver = login_setup
    with pytest.allure.step('Testing adding products to the Cart'):
        HomePage(driver)\
            .click_nav_desktops_mac()\
            .goto_mac_desktops()\
            .add_to_cart()
        assert (Outputs.TEXT_ALERT_PRODUCT_ADD in
                ProductPage(driver).get_product_add_confirmation())


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-7')
@pytest.allure.MINOR
@pytest.mark.dependency(name="3", depends=["2"])
@pytest.mark.run(order=3)
def test_edit_product_qty(login_setup):
    driver = login_setup
    with pytest.allure.step('Testing editing product quantity into the Cart'):
        HomePage(driver)\
            .click_nav_desktops_mac()\
            .goto_mac_desktops()\
            .add_to_cart()\
            .goto_cart()\
            .edit_good_qty(NEW_PRODUCT_QUANTITY)
        assert (Outputs.get_edited_product_quantity(NEW_PRODUCT_QUANTITY)
                in HomePage(driver).get_product_quantity())


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-7')
@pytest.allure.NORMAL
@pytest.mark.dependency(name="4", depends=["2"])
@pytest.mark.run(order=4)
def test_product_sum_price(login_setup, param_test):
    driver = login_setup
    (NEW_PRODUCT_QUANTITY, NEW_PRODUCT_PRICE) = param_test
    with pytest.allure.step(
            'Testing proper sum price after editing products quantity into the Cart'):
        HomePage(driver)\
            .click_nav_desktops_mac()\
            .goto_mac_desktops()\
            .add_to_cart()\
            .goto_cart()\
            .edit_good_qty(NEW_PRODUCT_QUANTITY)
        assert (Outputs.get_edited_product_price(NEW_PRODUCT_PRICE)
                in HomePage(driver).get_product_quantity())


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-7')
@pytest.allure.MINOR
@pytest.mark.dependency(name="5", depends=["3"])
@pytest.mark.run(order=5)
@pytest.mark.negative
def test_too_much_product(login_setup):
    driver = login_setup
    with pytest.allure.step('Testing alert appearing after adding too much products to the Cart'):
        HomePage(driver)\
            .click_nav_desktops_mac()\
            .goto_mac_desktops()\
            .add_to_cart()\
            .goto_cart()\
            .edit_good_qty(SET_TOO_MUCH_PRODUCT)
        assert (Outputs.TEXT_ALERT_TOO_MUCH_PRODUCT in CartPage(driver).get_alert_too_much())


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-7')
@pytest.allure.NORMAL
@pytest.mark.dependency(name="6", depends=["2"])
@pytest.mark.run(order=6)
@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-7')
def test_delete_product_from_cart(login_setup):
    driver = login_setup
    with pytest.allure.step('Testing deleting products from the Cart'):
        HomePage(driver)\
            .click_nav_desktops_mac()\
            .goto_mac_desktops()\
            .add_to_cart()\
            .goto_cart()\
            .delete_good_from_cart()
        assert Outputs.TEXT_ZERO_PRODUCT_QUANTITY in HomePage(driver).get_product_quantity()
