"""
Locators for Product Page are placed here
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class ProductPageLocators(BasePageLocators):
    """
    Locators for Product Page are placed here
    """
    BTN_CART = (By.ID, 'button-cart')
    ALERT = (By.CLASS_NAME, 'alert')
