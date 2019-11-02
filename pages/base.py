"""
Base Page comes here.
"""
import logging
from selenium import webdriver

from locators.base import BasePageLocators


# pylint: disable=too-few-public-methods
class BasePage:
    """
    Base class to initialize the base page that will be called from all pages.
    """

    def __init__(self, driver=None):
        """
        Initialization of base driver.

        :param driver: Receives driver with default value None.
        """
        self.driver = driver if driver else webdriver.Chrome()
        self.grey_cart_btn = GreyCartBtn(self.driver)


class GreyCartBtn:
    """
    Class to work with grey Cart button.
    """
    def __init__(self, driver):
        """
        Initialization of grey Cart Button.

        :param driver: Well, it's driver.
        """
        self.driver = driver

    def is_cart_btn_empty(self) -> bool:
        """
        Check whether the cartbutton is empty.

        :return: True if it`s empty, False if not
        """
        empty_cart_btn_text = self.driver.find_element(*BasePageLocators.EMPTY_CART_BUTTON_TEXT)
        if empty_cart_btn_text:
            logging.info("Your cart button is empty!")
            return True
        logging.error("Your Cart was not empty by default!!")
        return False

    def click_btn_grey_cart(self) -> "GreyCartBtn":
        """
        Make webdriver click grey Cart button.

        :return: Home Page Object with clicked grey Cart button.
        """
        logging.info('clicking grey Cart button')
        self.driver.find_element(*BasePageLocators.BTN_GREY_CART).click()
        return self

    def click_link_viewcart(self) -> "GreyCartBtn":
        """
        Make webdriver click Viewcart Link in grey Cart button.

        :return: Home Page Object with clicked Viewcart link.
        """
        logging.info('clicking Viewcart link')
        self.driver.find_element(*BasePageLocators.LINK_VIEW_CART).click()
        return self

    def click_link_checkout(self) -> "GreyCartBtn":
        """
        Make webdriver click Checkout Link in grey Cart button.

        :return: Home Page Object with clicked Checkout link.
        """
        logging.info('clicking Checkout link')
        self.driver.find_element(*BasePageLocators.LINK_CHECKOUT).click()
        return self

    def click_delete_btn(self) -> "GreyCartBtn":
        """
        Make webdriver click Checkout Link in grey Cart button.

        :return: Home Page Object with deleted first item from cart.
        """
        self.driver.find_element(*BasePageLocators.BTN_DELETE).click()
        logging.info('clicking delete btn')
        self.driver.refresh()
        return self
