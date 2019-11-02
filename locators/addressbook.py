"""
Contains AddressBookLocators class with AddressBook page element locators.
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class AddressBookLocators(BasePageLocators):
    """
    Contains constants with AddressBook page element locators.
    """

    BTN_EDIT = (By.XPATH, "//td[@class='text-right']//a[.='Edit']")
    BTN_EDIT_LIST = (By.XPATH, "//div[@class='table-responsive']//a[.='Edit']")
    BTN_DELETE = (By.XPATH, "//td[@class='text-right']//a[.='Delete']")
    BTN_DELETE_LIST = (By.XPATH, "//div[@class='table-responsive']//a[.='Delete']")
    BTN_NEW_ADDRESS = (By.XPATH, "//div[@id='content']//a[.='New Address']")
    ALERT_MESSAGE = (By.XPATH, "//div[@id='account-address']/div[1]")
    CONTENT_LIST = (By.XPATH, '//*[@id="content"]//table/tbody//td[1]')
