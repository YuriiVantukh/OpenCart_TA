import pytest

from helpers.constants import Returns
from helpers.settings import (BASE_HOST,
                              BASE_USER_EMAIL,
                              BASE_USER_PASSWORD)
from pages.home import HomePage
from pages.returns import ReturnsPage


@pytest.fixture()
def driver(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    (HomePage(driver).goto_login()
                     .input_email(BASE_USER_EMAIL)
                     .input_password(BASE_USER_PASSWORD)
                     .login())
    HomePage(driver).goto_returns()
    yield driver
    HomePage(driver).logout()


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-36')
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@pytest.allure.CRITICAL
@pytest.mark.parametrize('mode', ['base', 'personal'])
def test_positive_and_submit(driver, mode):
    (ReturnsPage(driver).fill_order_information(mode=mode, order_id='0000001')
                        .fill_product_information()
                        .click_submit())
    assert 'return/success' in driver.current_url


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-36')
@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@pytest.allure.NORMAL
@pytest.mark.parametrize('mode', ['base', 'personal'])
def test_positive_and_back(driver, mode):
    (ReturnsPage(driver).fill_order_information(mode=mode)
                        .fill_product_information()
                        .click_back())
    assert 'account' in driver.current_url


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-36')
@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@pytest.allure.NORMAL
@pytest.mark.negative
def test_required_fiels(driver):
    ReturnsPage(driver).click_submit()
    with pytest.allure.step('Check base text-danger field'):
        assert (ReturnsPage(driver).get_text_danger('order_id') ==
                Returns.TEXT_DANGER_ORDER_ID)
        assert (ReturnsPage(driver).get_text_danger('product_name') ==
                Returns.TEXT_DANGER_PRODUCT_NAME)
        assert (ReturnsPage(driver).get_text_danger('product_code') ==
                Returns.TEXT_DANGER_PRODUCT_CODE)

    with pytest.allure.step('Color is red'):
        assert (ReturnsPage(driver).get_color('order_id') ==
                ReturnsPage(driver).get_color('product_name') ==
                ReturnsPage(driver).get_color('product_code') ==
                Returns.DANGER_COLOR)
