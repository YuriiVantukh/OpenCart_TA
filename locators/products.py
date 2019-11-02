"""
Locators for Products Page are placed here
"""
from selenium.webdriver.common.by import By

from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class ProductsPageLocators(BasePageLocators):
    """
    Locators for Products Page are placed here
    """
    MAC_PRODUCT_IMAGE = (By.XPATH,
                         '//a[contains(@href, "route=product/product&path=20_27&product_id=41")]')

    @staticmethod
    def find_product_link(product_name: str) -> tuple:
        """
        Wrapper for product name locator on the Products page.

        :param product_name: Name of product need to be added
        :return: WebElement locator
        """
        link = (By.XPATH, '//h4/a[text()="{}"]'.format(product_name))
        return link
