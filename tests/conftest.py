import allure
import pytest

from helpers.driverfactory import DriverFactory


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
    yield driver
    attach = driver.get_screenshot_as_png()
    if request.node.rep_setup.failed:
        allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
    driver.close()
