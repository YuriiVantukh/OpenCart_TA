"""
Contains the EditAccountPage class for interacting with the EditAccount page.
"""
import logging
from locators.editaccount import EditAccountLocators
from models.personaldetails import PersonalDetails
from .base import BasePage


# pylint: disable=too-few-public-methods
class EditAccountPage(BasePage):
    """
    Contains methods for interacting with the EditAccount page.
    """

    @staticmethod
    def _change_data_in_text_fields(form_textfield: "WebElement", data: PersonalDetails):
        """
        Enter the data in the textfield.

        :param form_textfield: textfield's id.
        :param data: data entered in the textfield.
        """
        logging.info(f"Set data into {form_textfield} text field.")
        if data is not None:
            form_textfield.click()
            form_textfield.clear()
            form_textfield.send_keys(data)

    def fill_edit_account_form(self, user_data: PersonalDetails) -> "EditAccountPage":
        """
        Change user data in the Edit Account form.

        :param user_data: data entered in the textfield.
        :return: self object.
        """
        self._change_data_in_text_fields(
            self.driver.find_element(*EditAccountLocators.FIRSTNAME_FIELD), user_data.first_name)
        self._change_data_in_text_fields(
            self.driver.find_element(*EditAccountLocators.LASTNAME_FIELD), user_data.last_name)
        self._change_data_in_text_fields(
            self.driver.find_element(*EditAccountLocators.EMAIL_FIELD), user_data.email)
        self._change_data_in_text_fields(
            self.driver.find_element(*EditAccountLocators.TELEPHONE_FIELD), user_data.telephone)
        self.driver.find_element(*EditAccountLocators.BTN_CONTINUE).click()
        return self

    def get_email_from_form(self) -> PersonalDetails:
        """
        Take data from the E-mail field.

        :return: PersonalDetails object with email.
        """
        logging.info("Take email data and convert into PersonalDetails object.")
        data = self.driver.find_element(*EditAccountLocators.EMAIL_FIELD).get_attribute('value')
        return PersonalDetails(email=data)

    def get_user_firstname_error(self) -> str:
        """
        Get an error message from the 'First Name' field.

        :return: firstname error message.
        """
        logging.info("Get error message from 'First Name' field.")
        return self.driver.find_element(*EditAccountLocators.FIRSTNAME_ERROR).text

    def get_user_lastname_error(self) -> str:
        """
        Get an error message from the 'Last Name' field.

        :return: lastname error message.
        """
        logging.info("Get error message from 'Last Name' field.")
        return self.driver.find_element(*EditAccountLocators.LASTNAME_ERROR).text

    def get_user_telephone_error(self) -> str:
        """
        Get an error message from the 'Telephone' field.

        :return: address1 error message.
        """
        logging.info("Get error message from 'Telephone' field.")
        return self.driver.find_element(*EditAccountLocators.TELEPHONE_ERROR).text
