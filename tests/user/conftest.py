import allure
import pytest

from dbhelpers.updaters import create_all_db_tables
from helpers.driverfactory import DriverFactory
from helpers.settings import (BASE_HOST,
                              BASE_USER_EMAIL,
                              BASE_USER_PASSWORD)
from pages.home import HomePage
from helpers.settings import DB_PRESET


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.yield_fixture()
def init_driver(request):
    driver = DriverFactory.get_driver()
    driver.maximize_window()
    driver.get(BASE_HOST)
    HomePage(driver) \
        .goto_login() \
        .input_email(BASE_USER_EMAIL) \
        .input_password(BASE_USER_PASSWORD) \
        .login()
    yield driver
    attach = driver.get_screenshot_as_png()
    if request.node.rep_setup.failed:
        allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            allure.attach(request.function.__name__, attach, allure.attach_type.PNG)

    def fin():
        HomePage(driver).logout()
        driver.close()
    request.addfinalizer(fin)


@pytest.yield_fixture()
def init_user_db():
    yield create_all_db_tables(DB_PRESET["user_base"])
