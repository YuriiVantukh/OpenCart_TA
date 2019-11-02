"""
This module describes one of the step checkouts
"""

from elements.base import BasePageElement
from elements.button import Button
from locators.checkout import CheckoutPageLocators


# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
class Confirm(BasePageElement):
    """
    This class describes confirm of the purchase
    """

    def __init__(self, driver):
        super().__init__(driver)

        self.btn_continue = Button(self.driver, CheckoutPageLocators.BTN_CONFIRM_ORDER)
