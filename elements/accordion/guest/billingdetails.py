"""
This module describes one of the step checkouts
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from elements.base import BasePageElement
from elements.button import Button
from locators.checkout import CheckoutPageLocators


# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
class BillingDetailsGuest(BasePageElement):
    """
    This class describes billing details steps of the purchase
    """

    def __init__(self, driver):
        super().__init__(driver)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CheckoutPageLocators.FIRST_NAME_PAYMENT))

        self.firstname = self.driver.find_element(*CheckoutPageLocators.FIRST_NAME_PAYMENT)
        self.lastname = self.driver.find_element(*CheckoutPageLocators.LAST_NAME_PAYMENT)
        self.email = self.driver.find_element(*CheckoutPageLocators.EMAIL_PAYMENT)
        self.telephone = self.driver.find_element(*CheckoutPageLocators.TELEPHONE_PAYMENT)
        self.company = self.driver.find_element(*CheckoutPageLocators.COMPANY_PAYMENT)
        self.address_1 = self.driver.find_element(*CheckoutPageLocators.ADDRESS_1_PAYMENT)
        self.address_2 = self.driver.find_element(*CheckoutPageLocators.ADDRESS_2_PAYMENT)
        self.city = self.driver.find_element(*CheckoutPageLocators.CITY_PAYMENT)
        self.post_code = self.driver.find_element(*CheckoutPageLocators.POST_CODE_PAYMENT)
        self.country = self.driver.find_element(*CheckoutPageLocators.COUNTRY_PAYMENT)
        self.region_or_state = self.driver.find_element(
            *CheckoutPageLocators.REGION_OR_STATE_PAYMENT)
        self.checkbox_delivery = self.driver.find_element(
            *CheckoutPageLocators.CHECKBOX_DELIVERY)
        self.btn = Button(self.driver, CheckoutPageLocators.BTN_CONTINUE_S_2_G)
