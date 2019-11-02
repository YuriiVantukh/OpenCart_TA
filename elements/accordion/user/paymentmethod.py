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
class PaymentMethodUser(BasePageElement):
    """
    This class describes payment method steps of the purchase
    """

    def __init__(self, driver):
        super().__init__(driver)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CheckoutPageLocators.AGREE_TERMS_AND_CONDITIONS)
        )

        self.btn_agree = Button(self.driver, CheckoutPageLocators.AGREE_TERMS_AND_CONDITIONS)
        self.btn_continue = Button(self.driver, CheckoutPageLocators.BTN_CONTINUE_S_5)
