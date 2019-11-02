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
class DeliveryMethodGuest(BasePageElement):
    """
    This class describes delivery details steps of the purchase
    """
    def __init__(self, driver):
        super().__init__(driver)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CheckoutPageLocators.FIRST_NAME_SHIPPING))

        self.btn = Button(self.driver, CheckoutPageLocators.BTN_CONTINUE_S_4)
