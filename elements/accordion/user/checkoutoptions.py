"""
This module describes one of the step checkouts
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.base import BasePageElement
from elements.button import Button
from locators.checkout import CheckoutPageLocators


# pylint: disable=too-few-public-methods
class CheckoutOptionsUser(BasePageElement):
    """
    This class describes checkout options steps of the purchase
    """

    def __init__(self, driver):
        super().__init__(driver)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CheckoutPageLocators.GUEST_ACCOUNT))

        self.guest_account = self.driver.find_element(*CheckoutPageLocators.GUEST_ACCOUNT)
        self.register_account = self.driver.find_element(*CheckoutPageLocators.REGISTER_ACCOUNT)

        self.btn_account = Button(self.driver, CheckoutPageLocators.BTN_ACCOUNT)
        self.btn_login = Button(self.driver, CheckoutPageLocators.BTN_LOGIN)

        self.email_field = self.driver.find_element(*CheckoutPageLocators.E_MAIL)
        self.pass_field = self.driver.find_element(*CheckoutPageLocators.PASSWORD)

        self.alert = self.driver.find_element(*CheckoutPageLocators.ALERT)
