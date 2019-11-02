"""
Register Page comes here.
"""
# pylint: disable=duplicate-code
from selenium.webdriver.common.keys import Keys

from helpers.generators import (generate_random_email,
                                get_random_name,
                                get_random_digit,
                                get_random_password)
from .base import BasePage

RANDOM_NAME_LENGTH = 5
RANDOM_DIGITS_LENGTH = 9


class RegisterPage(BasePage):
    """
    Register Page methods come here.
    """

    last_created_password = None
    last_created_email = None

    def input_firstname(self):
        """Make webdriver set random 'First Name' value with presetted length."""
        self.driver.find_element_by_id("input-firstname")\
            .send_keys(get_random_name(RANDOM_NAME_LENGTH))
        return self

    def input_lastname(self):
        """Make webdriver set random 'Last Name' value with presetted length."""
        self.driver.find_element_by_id("input-lastname")\
            .send_keys(get_random_name(RANDOM_NAME_LENGTH))
        return self

    def input_email(self):
        """
        Make webdriver set random 'E-Mail' value with presetted length of local-name.
        Save generated E-Mail to last_created_email variable (for login).
        """
        self.last_created_email = generate_random_email(RANDOM_NAME_LENGTH)
        self.driver.find_element_by_id("input-email")\
            .send_keys(self.last_created_email)
        return self

    def input_telephone(self):
        """Make webdriver set random 'Telephone' value with presetted length."""
        self.driver.find_element_by_id("input-telephone")\
            .send_keys(get_random_digit(RANDOM_DIGITS_LENGTH))
        return self

    def input_password(self):
        """
        Make webdriver set random 'Password' value with presetted length.
        Save generated password to last_created_password variable (for login and confirm).
        """
        self.last_created_password = get_random_password(RANDOM_NAME_LENGTH)
        self.driver.find_element_by_id("input-password").send_keys(self.last_created_password)
        return self

    def input_confirm_password(self):
        """
        Make webdriver set 'Confirm Password' value
        (take from last_created_password variable).
        """
        self.driver.find_element_by_id("input-confirm").send_keys(self.last_created_password)
        return self

    def check_checkbox(self):
        """Make webdriver check 'Privacy Policy' Checkbox."""
        self.driver.find_element_by_name("agree").send_keys(Keys.SPACE)
        return self

    def registration(self):
        """Make webdriver click 'Continue' Button for registration complete."""
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/div/input[2]').click()
        return self
