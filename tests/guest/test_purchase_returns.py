import pytest

from helpers.constants import Returns
from helpers.settings import BASE_HOST
from pages.home import HomePage
from pages.returns import ReturnsPage


@pytest.fixture()
def driver(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    HomePage(driver).goto_returns()
    yield driver


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-35')
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@pytest.allure.CRITICAL
def test_positive_and_submit(driver):
    (ReturnsPage(driver).fill_order_information(mode='personal', order_id='0000001')
                        .fill_product_information()
                        .click_submit())
    assert 'return/success' in driver.current_url


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-35')
@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@pytest.allure.NORMAL
def test_positive_and_back(driver):
    (ReturnsPage(driver).fill_order_information(mode='personal', order_id='0000001')
                        .fill_product_information()
                        .click_back())
    assert 'login' in driver.current_url


@pytest.mark.skip(reason="this person already got a job")
@pytest.mark.negative
@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-35')
@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@pytest.allure.NORMAL
def test_required_fields(driver):
    ReturnsPage(driver).click_submit()

    with pytest.allure.step('Check all text-danger field'):
        assert (ReturnsPage(driver).get_text_danger('first_name') ==
                Returns.TEXT_DANGER_FIRST_NAME)
        assert (ReturnsPage(driver).get_text_danger('last_name') ==
                Returns.TEXT_DANGER_LAST_NAME)
        assert (ReturnsPage(driver).get_text_danger('email') ==
                Returns.TEXT_DANGER_EMAIL)
        assert (ReturnsPage(driver).get_text_danger('telephone') ==
                Returns.TEXT_DANGER_TELEPHONE)
        assert (ReturnsPage(driver).get_text_danger('order_id') ==
                Returns.TEXT_DANGER_ORDER_ID)
        assert (ReturnsPage(driver).get_text_danger('product_name') ==
                Returns.TEXT_DANGER_PRODUCT_NAME)
        assert (ReturnsPage(driver).get_text_danger('product_code') ==
                Returns.TEXT_DANGER_PRODUCT_CODE)

    with pytest.allure.step('Their color is red'):
        assert (ReturnsPage(driver).get_color('first_name') ==
                ReturnsPage(driver).get_color('last_name') ==
                ReturnsPage(driver).get_color('email') ==
                ReturnsPage(driver).get_color('telephone') ==
                ReturnsPage(driver).get_color('order_id') ==
                ReturnsPage(driver).get_color('product_name') ==
                ReturnsPage(driver).get_color('product_code') ==
                Returns.DANGER_COLOR)


@pytest.mark.skip(reason="this person already got a job")
@pytest.fixture(
    params=[
        {
            'first_name': '00c001',
            'last_name': '5wwew5we5'
        },
        {
            'first_name': 're@#1',
            'last_name': 's=0)'
        }],
    ids=['{first_name: 00c001, last_name: 5wwew5we5}',
         '{first_name: re@#1, last_name: s=0)}']
)
def invalid_data(request):
    return request.param


@pytest.mark.skip(reason="this person already got a job")
@pytest.mark.negative
@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-35')
@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@pytest.allure.NORMAL
def test_invalid_order_info(driver, invalid_data):
    (ReturnsPage(driver).fill_order_information(mode='personal', **invalid_data)
                        .click_submit())
    assert (ReturnsPage(driver).get_text_danger('first_name') ==
            Returns.TEXT_DANGER_FIRST_NAME_INVALID)
    assert (ReturnsPage(driver).get_text_danger('last_name') ==
            Returns.TEXT_DANGER_LAST_NAME_INVALID)
    assert (ReturnsPage(driver).get_text_danger('email') ==
            Returns.TEXT_DANGER_EMAIL_INVALID)
    assert (ReturnsPage(driver).get_text_danger('telephone') ==
            Returns.TEXT_DANGER_TELEPHONE_INVALID)
    assert (ReturnsPage(driver).get_text_danger('order_id') ==
            Returns.TEXT_DANGER_ORDER_ID_INVALID)
