from operator import attrgetter
import pytest
from dbhelpers.address import DbAddress
from pages.account import AccountPage
from pages.addressbook import AddressBookPage
from pages.addaddress import AddAddressPage
from helpers.constants import Returns
from helpers.settings import TEST_DATA
from helpers.data import load_from_json_file


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-38')
@pytest.mark.parametrize("address_data", load_from_json_file(TEST_DATA["addressbook_valid"]))
def test_add_correctly_address(init_driver, address_data):
    driver = init_driver
    AccountPage(driver)\
        .goto_address_book_page()
    with pytest.allure.step("Collect address book list from Address Book page."):
        previous_address_list = AddressBookPage(driver).get_content_info_from_list()
    with pytest.allure.step("Collect id's list from Address Book page."):
        previous_ui_ids_list = AddressBookPage(driver).get_list_of_ids()
    with pytest.allure.step("Create new address book record."):
        AddressBookPage(driver)\
            .goto_add_address_page()\
            .fill_address_form(address_data)
    with pytest.allure.step("Collect address book list from Address Book page with new record."):
        updated_address_list = AddressBookPage(driver).get_content_info_from_list()
    with pytest.allure.step("Take information from new address record."):
        info_from_new_address = AddressBookPage(driver).get_content_info_from_form(address_data)
    with pytest.allure.step("Append info from new record into old list."):
        previous_address_list.append(info_from_new_address)
    with pytest.allure.step("Collect id's list from Address Book page."):
        updated_ui_ids_list = AddressBookPage(driver).get_list_of_ids()
    with pytest.allure.step("Collect id's list from db."):
        updated_db_ids_list = DbAddress.get_id_list_from_db()
    with pytest.allure.step("Compare id's lists."):
        assert updated_ui_ids_list == updated_db_ids_list
    with pytest.allure.step("Compare len of id's lists."):
        assert len(previous_ui_ids_list) + 1 == len(updated_ui_ids_list)
    with pytest.allure.step("Retrieving info about successfully added address."):
        assert AddressBookPage(
            driver).get_alert_message_text() == Returns.TEXT_SUCCESS_ADDRESS_ADDED
    with pytest.allure.step("Compare old and new content lists."):
        assert sorted(previous_address_list, key=attrgetter(
            'content')) == sorted(updated_address_list, key=attrgetter('content'))


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-43')
@pytest.mark.parametrize("data", load_from_json_file(TEST_DATA["addressbook_invalid"]))
def test_add_incorrectly_address(init_driver, data):
    driver = init_driver
    with pytest.allure.step("Collect id's list from db."):
        previous_db_ids_list = DbAddress.get_id_list_from_db()
    AccountPage(driver)\
        .goto_address_book_page()\
        .goto_add_address_page()\
        .fill_address_form(data)
    with pytest.allure.step("Collect new id's list from db."):
        updated_db_ids_list = DbAddress.get_id_list_from_db()
    with pytest.allure.step("Compare id's lists."):
        assert previous_db_ids_list == updated_db_ids_list
    with pytest.allure.step("Check error message in the 'First Name' field."):
        assert AddAddressPage(
            driver).get_firstname_error() == Returns.TEXT_DANGER_FIRST_NAME_INVALID
    with pytest.allure.step("Check error message in the 'Last Name' field."):
        assert AddAddressPage(
            driver).get_lastname_error() == Returns.TEXT_DANGER_LAST_NAME_INVALID
    with pytest.allure.step("Check error message in the 'Address 1' field."):
        assert AddAddressPage(
            driver).get_address1_error() == Returns.TEXT_DANGER_ADDRESS1_INVALID
    with pytest.allure.step("Check error message in the 'City' field."):
        assert AddAddressPage(
            driver).get_city_error() == Returns.TEXT_DANGER_CITY_INVALID
    with pytest.allure.step("Check error message in the 'Post Code' field."):
        assert AddAddressPage(
            driver).get_postcode_error() == Returns.TEXT_DANGER_POSTCODE_INVALID
    with pytest.allure.step("Check error message in the 'Country' drop down option."):
        assert AddAddressPage(
            driver).get_region_error() == Returns.TEXT_DANGER_REGION_STATE_INVALID
