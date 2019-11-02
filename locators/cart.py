"""
Locators for Cart Page are placed here
"""
from typing import Tuple

from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class CartPageLocators(BasePageLocators):
    """
    Locators for Cart Page are placed here
    """
    GO_CHECKOUT = (By.XPATH, '//a[contains(@href, "route=checkout/checkout")]')
    EMPTY_CART_TEXT = (By.XPATH, '//p[text()="Your shopping cart is empty!"]')
    BTN_CONTINUE = (By.XPATH, '//a[contains(@href, "route=common/home")]')
    QTY_FIELD = (By.XPATH, '//div[@id="content"]//input')
    BTN_UPDATE = (By.XPATH, '//div[@id="content"]//button[1]')
    BTN_DELETE = (By.XPATH, '//div[@id="content"]//button[2]')

    BTN_DELETE_PRODUCT = (By.CLASS_NAME, 'btn btn-danger')
    BTN_EDIT_QTY = (By.CLASS_NAME, 'btn-primary')
    FIELD_PRODUCT_QTY = (By.CLASS_NAME, 'form-control')
    MODIFIED_CART_TEXT = (
        By.XPATH, '//div[contains(text(),"You have modified your shopping cart!")]')
    TOTAL_SUM = (By.XPATH, '//div[@id="content"]/tbody/td[6]')
    ALERT_TOO_MUCH_PRODUCT = (By.XPATH, '//*[@id="checkout-cart"]/div[2]')
    PRODUCT_ROW = (By.XPATH, "//button[2]")
    QTY_FIELD_2 = (By.TAG_NAME, "input")

    @staticmethod
    def product_number(number: int) -> tuple:
        """
        Wrapper for product locator on the Cart page.

        :param number: Name of product need to be added
        :return: WebElement locator
        """
        product_row = (By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr[{}]'.format(number))
        return product_row

    @staticmethod
    def find_product_edit_field(edit_model: str) -> Tuple:
        """
        Wrapper for product edit field locator.

        :param edit_model: Model of product, which quantity we want to edit.
        :return: Tuple for finding product's edit field
        """
        edit_field = (By.XPATH, '//a[text()="{}"]'.format(edit_model))
        return edit_field

    @staticmethod
    def find_product_delete_field(delete_model: str) -> Tuple:
        """
        Wrapper for product delete field locator.

        :param delete_model: Model of product, which we want to delete from Cart.
        :return: Tuple for finding product's delete button
        """
        delete = (By.XPATH, '//a[text()="{}"]'.format(delete_model))
        return delete

    @staticmethod
    def find_product_link(product_name: str) -> Tuple:
        """
        Wrapper for product name locator on the Cart page.

        :param product_name: Name of product need to be added
        :return: WebElement locator
        """
        link = (By.XPATH, '//td[2]/a[text()="{}"]'.format(product_name))
        return link
