import pytest
from dbhelpers.address import DbAddress
from pages.account import AccountPage
from pages.addressbook import AddressBookPage


@pytest.allure.testcase('https://ssu-jira.softserveinc.com/browse/OPENCARTPY-42')
def test_delete_address_by_index(init_user_db, init_driver, index=1):
    driver = init_driver
    AccountPage(driver)\
        .goto_address_book_page()
    with pytest.allure.step("Take the number of address book records on the page."):
        previous_address_list = AddressBookPage(driver).records_count()
    with pytest.allure.step("Delete address book record by index %d." % index):
        AddressBookPage(driver).delete_record_by_index(index)
    with pytest.allure.step("Take len of address list after deleting the record"):
        updated_address_list = AddressBookPage(driver).records_count()
    with pytest.allure.step("Compare the length of the list before and after deleting the record"):
        assert previous_address_list - 1 == updated_address_list
    with pytest.allure.step("Collect id's list from db."):
        assert len(DbAddress.get_id_list_from_db()) == 1
