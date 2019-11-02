"""
Contains EditAccountLocators class with EditAccount page element locators.
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class EditAccountLocators(BasePageLocators):
    """
    Contains constants with EditAccount page element locators.
    """

    FIRSTNAME_FIELD = (By.ID, "input-firstname")
    LASTNAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    TELEPHONE_FIELD = (By.ID, "input-telephone")
    BTN_CONTINUE = (By.XPATH, "//input[@type='submit']")
    FIRSTNAME_ERROR = (By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
    LASTNAME_ERROR = (By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
    TELEPHONE_ERROR = (By.XPATH, "//input[@id='input-telephone']/following-sibling::div")
