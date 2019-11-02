"""
Returns Page locators come here
"""
from selenium.webdriver.common.by import By

from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class ReturnsPageLocators(BasePageLocators):
    """
    It contains constants
    """

    FIRST_NAME = (By.ID, 'input-firstname')
    LAST_NAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    ORDER_ID = (By.ID, 'input-order-id')
    DATE_ORDERED = (By.ID, 'input-date-ordered')

    PRODUCT_NAME = (By.ID, 'input-product')
    PRODUCT_CODE = (By.ID, 'input-model')
    QUANTITY = (By.ID, 'input-quantity')
    REASON = (By.XPATH, '//*[@id="content"]/form/fieldset[2]/div[4]/div')
    COMMENT = (By.ID, 'input-comment')

    BTN_BACK = (By.CSS_SELECTOR, '.pull-left a')
    BTN_SUBMIT = (By.CSS_SELECTOR, '.pull-right input[type="submit"]')
