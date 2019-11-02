"""
Contains the PasswordPage class for interacting with the Password page.
"""
import logging
from locators.password import PasswordLocators
from models.password import Password
from .base import BasePage


# pylint: disable=too-few-public-methods
class PasswordPage(BasePage):
    """
    Contains methods for interacting with the Password page.
    """

    @staticmethod
    def _change_password_in_text_fields(form_textfield: "WebElement", data: Password):
        """
        Enter the data in the textfield.

        :param form_textfield: textfield's id.
        :param data: data entered in the textfield.
        """
        logging.info(f"Set {data} into {form_textfield} text field.")
        if data is not None:
            form_textfield.click()
            form_textfield.clear()
            form_textfield.send_keys(data)

    def fill_password_form(self, user_data: Password) -> "PasswordPage":
        """
        Change user data in the Edit Account form.

        :param user_data: data entered in the textfield.
        :return: PasswordPage object.
        """
        self._change_password_in_text_fields(
            self.driver.find_element(*PasswordLocators.PASSWORD_FIELD), user_data.password)
        self._change_password_in_text_fields(
            self.driver.find_element(*PasswordLocators.PASSWORD_CONFIRM_FIELD), user_data.password)
        self.driver.find_element(*PasswordLocators.BTN_CONTINUE).click()
        return self
