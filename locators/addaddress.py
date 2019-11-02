"""
Contains AddAddressLocators class with AddAddress page element locators.
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class AddAddressLocators(BasePageLocators):
    """
    Contains constants with AddAddress page element locators.
    """

    FIRSTNAME_ERROR = (By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
    LASTNAME_ERROR = (By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
    ADDRESS1_ERROR = (By.XPATH, "//input[@id='input-address-1']/following-sibling::div")
    CITY_ERROR = (By.XPATH, "//input[@id='input-city']/following-sibling::div")
    POSTCODE_ERROR = (By.XPATH, "//input[@id='input-postcode']/following-sibling::div")
    REGION_ERROR = (By.XPATH, "//select[@id='input-zone']/following-sibling::div")
    FIRSTNAME_FIELD = (By.ID, "input-firstname")
    LASTNAME_FIELD = (By.ID, "input-lastname")
    COMPANY_FIELD = (By.ID, "input-company")
    ADDRESS1_FIELD = (By.ID, "input-address-1")
    ADDRESS2_FIELD = (By.ID, "input-address-2")
    CITY_FIELD = (By.ID, "input-city")
    POSTCODE_FIELD = (By.ID, "input-postcode")
    COUNTRY_OPTION = (By.ID, "input-country")
    REGION_OPTION = (By.ID, "input-zone")
    BTN_CONTINUE = (By.XPATH, "//input[@type='submit']")
