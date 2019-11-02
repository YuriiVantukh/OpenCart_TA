import pytest
from pages.account import AccountPage
from pages.addressbook import AddressBookPage
from helpers.settings import TEST_DATA
from helpers.data import load_from_json_file
from helpers.constants import Returns


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-41')
@pytest.mark.parametrize("address", load_from_json_file(TEST_DATA["addressbook_valid"]))
def test_edit_address_by_index(init_user_db, init_driver, address, index=1):
    driver = init_driver
    AccountPage(driver)\
        .goto_address_book_page()\
        .goto_editaddress_page_by_index(index)\
        .fill_address_form(address)
    with pytest.allure.step("Take information from edited address record from Add Address form."):
        info_from_edited_address = AddressBookPage.get_content_info_from_form(address)
    with pytest.allure.step("Take information about edited address on Address Book page."):
        updated_info_from_address_list = AddressBookPage(driver).get_content_info_by_index(index)
    with pytest.allure.step("Retrieving info about successfully updated address."):
        assert AddressBookPage(
            driver).get_alert_message_text() == Returns.TEXT_SUCCESS_ADDRESS_UPDATED
    with pytest.allure.step("Compare info about edited address."):
        assert info_from_edited_address == updated_info_from_address_list
