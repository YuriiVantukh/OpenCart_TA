import pytest

from helpers.settings import BASE_HOST
from pages.checkout import CheckoutPage
from pages.product import ProductPage



@pytest.fixture()
def driver(init_driver):
    driver = init_driver
    driver.get('http://demo.opencart.com/index.php?route=product/product&product_id=47')
    # driver.get(f'{BASE_HOST}/index.php?route=product/product&product_id=47')
    (ProductPage(driver).add_to_cart()
                        .goto_cart()
                        .goto_checkout())
    yield driver


@pytest.mark.skip(reason="this person already got a job")
def test_base_flow(driver):
    (CheckoutPage(driver).checkout_options_guest()
                         .add_billing_details_guest()
                         .delivery_method_guest()
                         .payment_method_guest()
                         .confirm_order())
