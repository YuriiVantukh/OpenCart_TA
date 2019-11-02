"""
Contains PasswordLocators class with Password page element locators.
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class PasswordLocators(BasePageLocators):
    """
    Contains constants with Password page element locators.
    """

    PASSWORD_FIELD = (By.ID, "input-password")
    PASSWORD_CONFIRM_FIELD = (By.ID, "input-confirm")
    BTN_CONTINUE = (By.XPATH, "//input[@type='submit']")
