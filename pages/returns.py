"""
Returns Page comes here.
"""
import logging
from typing import Dict
from faker import Faker

from elements.button import Button
from elements.textfield import TextField
from locators.returns import ReturnsPageLocators
from .base import BasePage
from .login import LoginPage

# pylint: disable=invalid-name
fake = Faker()


# pylint: disable=no-member
class ReturnsPage(BasePage):
    """
    Returns Page methods come here.
    """

    def get_text_danger(self, field: tuple) -> str:
        """
        Get text-danger of the field

        :param field: locator the field
        :return: text-danger
        """
        return self.driver.find_element_by_css_selector(
            f'#{getattr(ReturnsPageLocators, field.upper())[1]}+div').text

    def get_color(self, field: tuple) -> str:
        """
       Get value color of the field

       :param field: locator the field
       :return: value color of the field
       """
        return self.driver.find_element_by_css_selector(
            f'#{getattr(ReturnsPageLocators, field.upper())[1]}+div').value_of_css_property('color')

    def fill_order_information(self, mode: str = 'base', **kwargs: Dict[str, int]) -> 'ReturnsPage':
        """
        Fill order information fields depends on the chosen mode

        :param mode: sets the operating mode
        :param kwargs: contains the required values
        :return: object of the class
        """
        order_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.ascii_safe_email(),
            'telephone': fake.phone_number(),
            'order_id': fake.isbn10(separator=""),
            'date_ordered': fake.date(pattern="%Y-%m-%d",
                                      end_datetime=None)
        }

        last_data = {key: kwargs.get(key, value) for key, value in order_data.items()}

        logging.info(f'Start fill order information fields, mode = {mode}')
        if mode == 'personal':
            TextField(self.driver,
                      ReturnsPageLocators.FIRST_NAME).clear().set(last_data['first_name'])
            TextField(self.driver,
                      ReturnsPageLocators.LAST_NAME).clear().set(last_data['last_name'])
            TextField(self.driver,
                      ReturnsPageLocators.EMAIL).clear().set(last_data['email'])
            TextField(self.driver,
                      ReturnsPageLocators.TELEPHONE).clear().set(last_data['telephone'])
            logging.info('Personal fields of the order information are filled')

        self.driver.find_element(
            *ReturnsPageLocators.ORDER_ID).send_keys(last_data['order_id'])
        self.driver.find_element(
            *ReturnsPageLocators.DATE_ORDERED).send_keys(last_data['date_ordered'])
        logging.info('Base fields of the order information are filled')

        return self

    def fill_product_information(self) -> "ReturnsPage":
        """
        Fill all fields of product information

        :return: object of the class
        """
        self.driver.find_element(
            *ReturnsPageLocators.PRODUCT_NAME).send_keys(fake.first_name())
        self.driver.find_element(
            *ReturnsPageLocators.PRODUCT_CODE).send_keys(fake.isbn10(separator=""))
        self.driver.find_element(
            *ReturnsPageLocators.QUANTITY).send_keys('5')

        self.driver.find_element(*ReturnsPageLocators.REASON).find_element_by_xpath(
            '//*[@id="content"]/form/fieldset[2]/div[4]/div/div[3]/label').click()
        self.driver.find_element(
            *ReturnsPageLocators.COMMENT).send_keys(fake.paragraph(nb_sentences=3,
                                                                   variable_nb_sentences=True,
                                                                   ext_word_list=None))
        logging.info('All fields of the product information are filled')

        return self

    def click_submit(self) -> "ReturnsPage":
        """
        Click on submit button

        :return: object of the class
        """
        Button(self.driver, ReturnsPageLocators.BTN_SUBMIT).click()
        logging.info('Click on SUBMIT button')
        return self

    def click_back(self) -> LoginPage:
        """
        Click on back button

        :return: object of LoginPage class
        """
        Button(self.driver, ReturnsPageLocators.BTN_BACK).click()
        logging.info('Click on BACK button')
        return LoginPage(self.driver)

    def logout(self):
        """
        Click on logout in right column

        :return: object of HomePage class
        """
        self.driver.find_element_by_xpath('//*[@id="column-right"]/div/a[13]').click()
        return self.driver
