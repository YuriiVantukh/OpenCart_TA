"""
Cart Page comes here.
"""
import logging

from urllib.parse import urlparse

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from locators.cart import CartPageLocators
from .base import BasePage
from .checkout import CheckoutPage


# pylint: disable=logging-format-interpolation
# pylint: disable=attribute-defined-outside-init
class CartPage(BasePage):
    """
    Cart Page methods come here.
    """

    def edit_good_qty(self, qty: int) -> "CartPage":
        """
        Make webdriver change qty of first product in Cart.

        :param qty: Quantity of product, that you want to get after update.
        :return: Cart Page Object with changed qty of first product in Cart.
        """
        logging.info('editing first product quantity in Cart')
        edit_field = self.driver.find_element(*CartPageLocators.QTY_FIELD)
        edit_field.clear()
        edit_field.send_keys(qty)
        self.driver.find_element(*CartPageLocators.BTN_UPDATE).click()
        return self

    def delete_good_from_cart(self) -> "CartPage":
        """
        Make webdriver delete first product from Cart.
        Refresh browser page for make shore changes will appear.

        :return: Cart Page Object with deleted first product in Cart.
        """
        logging.info('deleting first product from Cart')
        self.driver.find_element(*CartPageLocators.BTN_DELETE).click()
        self.driver.refresh()
        return self

    def edit_product_qty_by_model(self, edit_model: str, qty: int) -> "CartPage":
        """
        Make webdriver edit quantity of certain product to Cart

        :param edit_model: Model of product, which quantity we want to edit.
        :param qty: Quantity of product, that you want to get after update.
        :return: Cart Page Object with edited certain product quantity.
        """
        logging.info('editing quantity of certain product in Cart by model')
        edit_field = self.driver.find_element(
            *CartPageLocators.find_product_edit_field(edit_model))
        edit_field.clear()
        edit_field.send_keys(qty)
        edit_field.send_keys(Keys.ENTER)
        return self

    def delete_product_by_model(self, delete_model: str) -> "CartPage":
        """
        Make webdriver delete certain product from Cart

        :param delete_model: Model of product, which we want to delete from Cart.
        :return: Cart Page Object with deleted certain product from Cart.
        """
        logging.info('certain product from Cart by model')
        self.driver.find_element(
            *CartPageLocators.find_product_delete_field(delete_model)).click()
        self.driver.refresh()
        return self

    def get_alert_too_much(self) -> str:
        """
        Get too much product alert text.

        :return: Text of too much product alert.
        """
        logging.info('getting the text of too much product alert')
        error_message = self.driver.find_element(*CartPageLocators.ALERT_TOO_MUCH_PRODUCT)
        return error_message.text

    def goto_checkout(self) -> "CheckoutPage":
        """
        Make webdriver go to Checkout Page

        :return: Checkout Page Object.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CartPageLocators.GO_CHECKOUT)
        )
        element = self.driver.find_element(*CartPageLocators.GO_CHECKOUT)
        element.click()
        return CheckoutPage(self.driver)

    def is_on_cart_page(self) -> bool:
        """
        Check whether driver is on shopping cart page now.

        :return: True if driver is on shopping cart page, False if not
        """
        current_url_path = urlparse(self.driver.current_url).path
        if current_url_path == "/opencart.com/index.php":
            logging.info("You are on shopping cart page!")
            return True
        logging.error("Something went wrong!")
        return False

    def is_cart_empty(self) -> bool:
        """
        Check whether the shopping cart page is empty.

        :return: True if it`s empty, False if not
        """
        empty_cart_text = self.driver.find_element(*CartPageLocators.EMPTY_CART_TEXT)
        if empty_cart_text:
            logging.info("Your shopping cart is empty!")
            return True
        logging.error("Something went wrong!")
        return False

    def is_product_added(self, product_name: str) -> bool:
        """
        Check whether the product page is added to cart.

        :param product_name: Name of added product
        :return: True if product was added, False if not
        """
        if self.driver.find_element(*CartPageLocators.find_product_link(product_name)):
            logging.info("You have added {} to your cart!".format(product_name))
            return True
        logging.error("Something went wrong!")
        return False

    def click_on_continue_button(self):
        """
        Click on the Continue button when cart is empty.

        :return: instance driver
        """
        self.driver.find_element(*CartPageLocators.BTN_CONTINUE).click()
        logging.info("Clicked on continue button!")
        return self.driver

    def _product_number(self, number: int):
        """
        Protected method to get product number.
        """
        self.row = self.driver.find_element(*CartPageLocators.product_number(number))
        return self.row

    def edit_qty_field(self, quantity: int) -> "Cart Page":
        """
        Edit quantity of added product.

        :param quantity: quantity of added product
        :return: Cart Page Object with changed qty of added product
        """
        self._product_number(1)
        input_field = self.row.find_element(*CartPageLocators.QTY_FIELD_2)
        input_field.clear()
        input_field.send_keys(quantity)
        input_field.send_keys(Keys.ENTER)
        logging.info("You have edited product quantity")
        return self

    def click_on_delete_btn(self) -> "Cart Page":
        """
        Delete product from Cart.

        :return: Cart Page Object with deleted product from Cart.
        """
        self._product_number(1)
        self.row.find_element(*CartPageLocators.PRODUCT_ROW).click()
        logging.info("You have deleted product from cart")
        return self

    def is_cart_modified(self) -> bool:
        """
        Check whether the shopping cart page was modified.

        :return: True if it`s modified, False if not
        """
        modified_cart_text = self.driver.find_element(*CartPageLocators.MODIFIED_CART_TEXT)
        if modified_cart_text:
            logging.info("Shopping cart was modified")
            return True
        logging.error("Something went wrong!")
        return False
