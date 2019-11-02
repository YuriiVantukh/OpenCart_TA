import pytest
from pages.account import AccountPage
from pages.editaccount import EditAccountPage
from dbhelpers.customer import DbCustomer
from helpers.settings import TEST_DATA
from helpers.data import load_from_json_file
from helpers.constants import Returns


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-39')
@pytest.mark.parametrize("new_data", load_from_json_file(TEST_DATA["personalinfo_valid"]))
def test_edit_correct_account_info(init_driver, new_data):
    with pytest.allure.step("Fill 'Edit Account' form with data."):
        driver = init_driver
        AccountPage(driver)\
            .goto_edit_account_page()\
            .fill_edit_account_form(new_data)
    with pytest.allure.step("Retrieving info about successfully updated account."):
        assert AccountPage(
            driver).get_account_alert_message_text() == Returns.TEXT_SUCCESS_ACCOUNT_UPDATED
    with pytest.allure.step("Compare data from application with data from db."):
        assert new_data == DbCustomer.get_from_db_by_email(new_data)


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-44')
@pytest.mark.parametrize("new_data", load_from_json_file(TEST_DATA["personalinfo_invalid"]))
def test_edit_incorrect_account_info(init_driver, new_data):
    with pytest.allure.step("Fill 'Edit Account' form with data."):
        driver = init_driver
        AccountPage(driver)\
            .goto_edit_account_page()\
            .fill_edit_account_form(new_data)
    with pytest.allure.step("Check error message in the 'First Name' field."):
        assert EditAccountPage(
            driver).get_user_firstname_error() == Returns.TEXT_DANGER_FIRST_NAME_INVALID
    with pytest.allure.step("Check error message in the 'Last Name' field."):
        assert EditAccountPage(
            driver).get_user_lastname_error() == Returns.TEXT_DANGER_LAST_NAME_INVALID
    with pytest.allure.step("Check error message in the 'Telephone' field."):
        assert EditAccountPage(
            driver).get_user_telephone_error() == Returns.TEXT_DANGER_TELEPHONE_FORM
