"""
Account Page comes here.
"""
import logging
from locators.account import AccountLocators
from .base import BasePage
from .addressbook import AddressBookPage
from .editaccount import EditAccountPage
from .password import PasswordPage


class AccountPage(BasePage):
    """
    Account Page methods come here.
    """

    def goto_address_book_page(self) -> AddressBookPage:
        """
        Redirect to AddressBook page.
        """
        logging.info("Click on 'Address Book' link.")
        self.driver.find_element(*AccountLocators.ADDRESS_BOOK_LINK).click()
        return AddressBookPage(self.driver)

    def goto_edit_account_page(self) -> EditAccountPage:
        """
        Redirect to EditAccount page.
        """
        logging.info("Click on 'Edit Account' link.")
        self.driver.find_element(*AccountLocators.EDIT_ACCOUNT_LINK).click()
        return EditAccountPage(self.driver)

    def goto_homepage(self):
        """
        Redirect to Home page.
        """
        self.driver.find_element(*AccountLocators.YOUR_STORE_LINK).click()
        return self

    def goto_password_page(self) -> PasswordPage:
        """
        Redirect to Password page.
        """
        logging.info("Click on 'Password' link.")
        self.driver.find_element(*AccountLocators.PASSWORD_LINK).click()
        return PasswordPage(self.driver)

    def get_account_alert_message_text(self) -> str:
        """
        Receive a message from the account after adding,
        editing or deleting a record.

        :return: informal text message.
        """
        logging.info("Get informal message from 'Account' page.")
        return self.driver.find_element(*AccountLocators.INFO_MESSAGE).text
