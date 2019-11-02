"""
Contains the AddressBookPage class for interacting with the AddressBook page.
"""
import logging
import re
from typing import List
from models.addressbook import AddressBook
from locators.addressbook import AddressBookLocators
from .base import BasePage
from .addaddress import AddAddressPage


class AddressBookPage(BasePage):
    """
    Contains methods for interacting with the AddressBook page.
    """

    def get_alert_message_text(self) -> str:
        """
        Receive a message from the address book after adding,
        editing or deleting a record.

        :return: informal text message.
        """
        logging.info("Get informal message from 'Address Book' page.")
        return self.driver.find_element(*AddressBookLocators.ALERT_MESSAGE).text

    def records_count(self) -> int:
        """
        Count the number of address records on the Address Book page.

        :return: count of address book records.
        """
        logging.info("Get entries count on 'Address Book' page.")
        return len(self.driver.find_elements(*AddressBookLocators.BTN_EDIT_LIST))

    def goto_editaddress_page_by_index(self, index: int) -> AddAddressPage:
        """
        Edit address book entry from the Address Book page
        by it's positional index.

        :param index: positional index of address entry
        in list of addresses on the Address Book page.
        :return: AddAddressPage.
        """
        logging.info(f"Click on 'Edit' button by index {index}.")
        self.driver.find_elements(*AddressBookLocators.BTN_EDIT_LIST)[index].click()
        return AddAddressPage(self.driver)

    def delete_record_by_index(self, index: int) -> "AddressBookPage":
        """
        Delete Address Book entry from Address Book page
        by it's positional index.

        :param index: positional index of address entry
        in list of addresses on Address Book page.
        :return: self object.
        """
        logging.info(f"Click on 'Delete' button by index {index}.")
        self.driver.find_elements(*AddressBookLocators.BTN_DELETE_LIST)[index].click()
        return self

    def goto_add_address_page(self) -> AddAddressPage:
        """
        Open Add Address form on Address Book page.

        :return: AddAddressPage.
        """
        logging.info("Click on 'New Address' button.")
        self.driver.find_element(*AddressBookLocators.BTN_NEW_ADDRESS).click()
        return AddAddressPage(self.driver)

    def get_content_info_from_list(self) -> List[AddressBook]:
        """
        Get text of each individual address record in table on the Address Book page,
        filter and convert it into object, append them to list and return it.

        :return: list of AddressBook objects.
        """
        logging.info("Get list of AddressBook objects with all address entries on page.")
        address_list = []
        for line in self.driver.find_elements(*AddressBookLocators.CONTENT_LIST):
            content = re.sub(r'\s', '', line.text)
            address_list.append(AddressBook(content=content))
        return address_list

    @staticmethod
    def get_content_info_from_form(address_obj: AddressBook) -> AddressBook:
        """
        Get text from AddressBook object, filter and convert it into another AddressBook object.

        :param address_obj: object that we used to create/edit Add Address form.
        :return: AddressBook object with filtered text.
        """
        logging.info("Get text from AddressBook object,"
                     "filter and convert it into another AddressBook object.")
        info_from_object = []
        for attr in address_obj.__dict__.items():
            if attr[1] is not None:
                info_from_object.append(attr[1])
        content = re.sub(r'\s', '', "".join(info_from_object))
        return AddressBook(content=content)

    def get_content_info_by_index(self, index: int) -> AddressBook:
        """
        Get text from address record  by index in table on the Address Book page,
        filter and convert it into object.

        :return: AddressBook object.
        """
        logging.info(f"Convert data from {index} entry to AddressBook object.")
        info = self.driver.find_elements(*AddressBookLocators.CONTENT_LIST)[index].text
        content = re.sub(r'\s', '', info)
        return AddressBook(content=content)

    def get_list_of_ids(self) -> List[int]:
        """
        Get id list from UI.

        :return: list with id's.
        """
        id_list = []
        logging.info(f"Get id's list {id_list}")
        data = self.driver.find_elements(*AddressBookLocators.BTN_EDIT_LIST)
        for ui_id in data:
            id_list.append(int(ui_id.get_attribute("href")[74:]))
        return sorted(id_list)
