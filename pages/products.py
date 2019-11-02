"""
Products Page comes here.
"""
# pylint: disable=too-few-public-methods
# pylint: disable=logging-format-interpolation
import logging

from locators.products import ProductsPageLocators
from .base import BasePage
from .product import ProductPage


class ProductsPage(BasePage):
    """
    Products Page methods come here.
    """
    def goto_mac_desktops(self) -> "ProductPage":
        """
        Make webdriver click MAC desktop.

        :return: Product MAC Page Object.
        """
        logging.info('clicking MAC image to get MAC Product Page')
        self.driver.find_element(*ProductsPageLocators.MAC_PRODUCT_IMAGE).click()
        return ProductPage(self.driver)

    def goto_product_page(self, product_name: str) -> "ProductPage":
        """
        Click on selected product link.

        :param product_name: Name of product you want to add
        :return: ProductPage object
        """
        self.driver.find_element(*ProductsPageLocators.find_product_link(product_name)).click()
        logging.info("You went to {} product page!".format(product_name))
        return ProductPage(self.driver)
