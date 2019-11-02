import time

import pytest

from helpers.settings import URL, BASE_USER_EMAIL, BASE_USER_PASSWORD
from locators.checkout import CheckoutPageLocators
from pages.checkout import CheckoutPage
from pages.home import HomePage
from pages.product import ProductPage


@pytest.fixture()
def driver(init_driver):
    driver = init_driver
    driver.get(URL)
    (ProductPage(driver).add_to_cart().goto_cart().goto_checkout())
    yield driver
    HomePage(driver).logout()


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-32')
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_valid_checkout(driver):
    with pytest.allure.step('User enter valid credential for login'):
        CheckoutPage(driver).checkout_options_user(BASE_USER_EMAIL, BASE_USER_PASSWORD)
    with pytest.allure.step('Choose new address and confirm'):
        CheckoutPage(driver).choose_new_address() \
                            .add_billing_details_user()
    with pytest.allure.step('Choose new address for delivery'):
        CheckoutPage(driver).choose_new_address_delivery() \
                            .add_delivery_details_user()
    CheckoutPage(driver).delivery_method_user()
    CheckoutPage(driver).payment_method_user()
    CheckoutPage(driver).confirm_order()


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-32')
def test_invalid_checkout(driver):
    email = 'exemple@gmail.com'
    password = '123'
    time.sleep(1)
    with pytest.allure.step('User enter invalid credentials for login'):
        checkout = CheckoutPage(driver).checkout_options_user(email, password)
    try:
        alert = checkout.driver.find_element(*CheckoutPageLocators.ALERT)
        assert "Warning: No match for E-Mail Address and/or Password." in alert.text
    except AssertionError:
        CheckoutPage(driver).checkout_options_user(BASE_USER_EMAIL, BASE_USER_PASSWORD)
    CheckoutPage(driver).choose_new_address().add_billing_details_user()
