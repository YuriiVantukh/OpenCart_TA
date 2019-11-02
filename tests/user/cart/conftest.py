import allure
import pytest

from helpers.constants import Outputs
from helpers.driverfactory import DriverFactory
from helpers.settings import (BASE_HOST,
                              BASE_USER_EMAIL,
                              BASE_USER_PASSWORD)
from pages.home import HomePage


@pytest.fixture(scope="function", autouse="false")
def login_setup(request):
    driver = DriverFactory.get_driver()
    driver.get(BASE_HOST)
    HomePage(driver)\
        .goto_login()\
        .input_password(BASE_USER_PASSWORD)\
        .input_email(BASE_USER_EMAIL)\
        .login()\
        .goto_homepage()
    while Outputs.TEXT_ZERO_PRODUCT_QUANTITY not in HomePage(driver).get_product_quantity():
        HomePage(driver).goto_cart().delete_good_from_cart()
    yield driver
    attach = driver.get_screenshot_as_png()
    if request.node.rep_setup.failed:
        allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            allure.attach(request.function.__name__, attach, allure.attach_type.PNG)

    def logout_teardown():
        while Outputs.TEXT_ZERO_PRODUCT_QUANTITY not in HomePage(driver).get_product_quantity():
            HomePage(driver).goto_cart().delete_good_from_cart()
        HomePage(driver).logout()
        driver.close()
    request.addfinalizer(logout_teardown)


@pytest.fixture(scope="module", autouse=False, params=[
    (2, 200.00),
    (3, 300.00),
    (4, 500.00)
    ])
def param_test(request):
    return request.param
