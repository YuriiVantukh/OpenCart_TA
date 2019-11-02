"""
This module describes one of the step checkouts
"""

from elements.base import BasePageElement
from elements.button import Button
from locators.checkout import CheckoutPageLocators


# pylint: disable=too-few-public-methods
class CheckoutOptionsGuest(BasePageElement):
    """
    This class describes checkout options steps of the purchase
    """

    def __init__(self, driver):
        super().__init__(driver)

        self.guest_account = Button(self.driver, CheckoutPageLocators.GUEST_ACCOUNT)
        self.register_account = Button(self.driver, CheckoutPageLocators.REGISTER_ACCOUNT)

        self.btn_account = Button(self.driver, CheckoutPageLocators.BTN_ACCOUNT)
