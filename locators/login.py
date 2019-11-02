"""
Locators for Login Page are placed here
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class LoginPageLocators(BasePageLocators):
    """
    Locators for Login Page are placed here
    """
    EMAIL_INPUT_FIELD = (By.ID, "input-email")
    PASSWORD_INPUT_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
