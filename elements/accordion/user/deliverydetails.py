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
class DeliveryDetailsUser(BasePageElement):
    """
    This class describes delivery details steps of the purchase
    """

    def __init__(self, driver):
        super().__init__(driver)

        self.btn_new_address_delivery = Button(self.driver,
                                               CheckoutPageLocators.RADIO_ADDRESS_DELIVERY)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CheckoutPageLocators.FIRST_NAME_SHIPPING))

        self.firstname = self.driver.find_element(*CheckoutPageLocators.FIRST_NAME_SHIPPING)
        self.lastname = self.driver.find_element(*CheckoutPageLocators.LAST_NAME_SHIPPING)
        self.company = self.driver.find_element(*CheckoutPageLocators.COMPANY_SHIPPING)
        self.address_1 = self.driver.find_element(*CheckoutPageLocators.ADDRESS_1_SHIPPING)
        self.address_2 = self.driver.find_element(*CheckoutPageLocators.ADDRESS_2_SHIPPING)
        self.city = self.driver.find_element(*CheckoutPageLocators.CITY_SHIPPING)
        self.country = self.driver.find_element(*CheckoutPageLocators.COUNTRY_SHIPPING)
        self.region_or_state = self.driver. \
            find_element(*CheckoutPageLocators.REGION_OR_STATE_SHIPPING)

        self.btn = Button(self.driver, CheckoutPageLocators.BTN_CONTINUE_S_3)
