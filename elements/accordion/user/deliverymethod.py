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
class DeliveryMethodUser(BasePageElement):
    """
    This class describes delivery method steps of the purchase
    """

    def __init__(self, driver):
        super().__init__(driver)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CheckoutPageLocators.BTN_CONTINUE_S_4)
        )
        self.btn_s_4 = Button(self.driver, CheckoutPageLocators.BTN_CONTINUE_S_4)
