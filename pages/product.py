"""
Product Page comes here.
"""
import logging
import time

from locators.product import ProductPageLocators
from .base import BasePage
from .cart import CartPage

DRIVER_WAIT_TIME = 1


# pylint: disable=too-few-public-methods
class ProductPage(BasePage):
    """
    Product Page methods come here.
    """

    def add_to_cart(self) -> "ProductPage":
        """
        Make webdriver add product to Cart.

        :return: Product Page Object with added product into Cart.
        """
        logging.info('adding product to the Cart')
        self.driver.find_element(*ProductPageLocators.BTN_CART).click()
        time.sleep(DRIVER_WAIT_TIME)
        return self

    def goto_cart(self) -> "CartPage":
        """
        Make webdriver go to Cart Page.

        :return: Cart Page Object.
        """
        logging.info('clicking Cart Link in top Bar')
        time.sleep(DRIVER_WAIT_TIME)
        self.driver.find_element(*ProductPageLocators.GO_CART).click()
        return CartPage(self.driver)

    def get_product_add_confirmation(self) -> str:
        """
        Get success product add alert text.

        :return: Text of product add alert
        """
        logging.info('getting the text of success product add to Cart')
        success_text = self.driver.find_element(*ProductPageLocators.ALERT)
        return success_text.text
