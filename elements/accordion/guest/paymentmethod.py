"""
This module describes one of the step checkouts
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.base import BasePageElement
from elements.button import Button
from locators.checkout import CheckoutPageLocators


# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
class PaymentMethodGuest(BasePageElement):
    """
    This class describes delivery details steps of the purchase
    """
    def __init__(self, driver):
        super().__init__(driver)

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(CheckoutPageLocators.AGREE_TERMS_AND_CONDITIONS))

        self.agree = self.driver.find_element(*CheckoutPageLocators.AGREE_TERMS_AND_CONDITIONS)
        self.btn = Button(self.driver, CheckoutPageLocators.BTN_CONTINUE_S_5)
