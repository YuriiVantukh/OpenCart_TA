"""
Account Page comes here.
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class AccountLocators(BasePageLocators):
    """
    Locators for Account Page are placed here
    """
    ADDRESS_BOOK_LINK = (By.LINK_TEXT, "Address Book")
    EDIT_ACCOUNT_LINK = (By.XPATH, "//div[@id='content']//a[.='Edit Account']")
    YOUR_STORE_LINK = (By.LINK_TEXT, "Your Store")
    PASSWORD_LINK = (By.XPATH, "//div[@id='content']//a[.='Password']")
    INFO_MESSAGE = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
