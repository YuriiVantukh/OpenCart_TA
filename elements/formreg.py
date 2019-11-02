""" account register form"""
from helpers.singleton import Wrapper
from locators.login import LoginPageLocators
from locators.register import RegisterElementLocators
from locators.register import ErrorsRegisterElement


# pylint: disable=too-few-public-methods


class Element:
    """init class elements who takes method By and locators"""

    def __init__(self, method, locator):
        self.locator = locator
        self.method = method


# pylint: disable=too-few-public-methods
class FormsElement(Element):
    """reload get and set methods """

    def __get__(self, obj, cls=None):
        Wrapper().connection.find_element(self.method, self.locator).click()

    def __set__(self, obj, value):
        """Gets the text of the specified object"""
        Wrapper().connection.find_element(self.method, self.locator).clear()
        Wrapper().connection.find_element(self.method, self.locator).send_keys(value)


class ERRORELEMENT(Element):
    """reload get and set methods """

    def __get__(self, obj, cls=None):
        error_text = Wrapper().connection.find_element(self.method, self.locator).text
        return error_text


# pylint: disable=too-few-public-methods
class Reg:
    """Init class elements form account register"""
    url_login = 'http://localhost/opencart/index.php?route=account/login'
    url = 'http://localhost/opencart/index.php?route=account/register'
    first_name = FormsElement(*RegisterElementLocators.FIRSTNAME)
    last_name = FormsElement(*RegisterElementLocators.LASTNAME)
    e_mail = FormsElement(*RegisterElementLocators.EMAIL)
    telephone = FormsElement(*RegisterElementLocators.TELEPHONE)
    password = FormsElement(*RegisterElementLocators.PASSWORD)
    confirm_password = FormsElement(*RegisterElementLocators.CONFIRM_PASSWORD)
    agree_checkbox = FormsElement(*RegisterElementLocators.AGREE)
    continue_btn = FormsElement(*RegisterElementLocators.CONTINUE)
    telephone_error = ERRORELEMENT(*ErrorsRegisterElement.ETELEPHONE)
    first_name_error = ERRORELEMENT(*ErrorsRegisterElement.EFIRSTNAME)
    last_name_error = ERRORELEMENT(*ErrorsRegisterElement.ELASTNAME)
    e_mail_error = ERRORELEMENT(*ErrorsRegisterElement.EEMAIL)
    password_error = ERRORELEMENT(*ErrorsRegisterElement.EPASSWORD)
    password_confirm_error = ERRORELEMENT(*ErrorsRegisterElement.ECONFIRMPASSWORD)
    title_error = ERRORELEMENT(*ErrorsRegisterElement.ETITLE)
    input_password = FormsElement(*LoginPageLocators.PASSWORD_INPUT_FIELD)
    input_email = FormsElement(*LoginPageLocators.EMAIL_INPUT_FIELD)
    login_btn = FormsElement(*LoginPageLocators.LOGIN_BUTTON)

    def open(self) -> None:
        """
        Open register page
        :return: none
        """
        Wrapper().webdriver_rem().get(self.url)

    @staticmethod
    def close() -> None:
        """
        Close driver
        :return:none
        """
        Wrapper().connection.close()

    def login(self):
        """
        Open register page
        :return: none
        """
        Wrapper().webdriver_rem().get(self.url_login)

    @staticmethod
    def title() -> str:
        """
        find title page
        :return: title
        """
        return Wrapper().connection.title

    @staticmethod
    def validator() -> str:
        """
        validation message
        return: message which generates validator
        """
        validation_message = Wrapper().connection.find_element_by_id('input-email').get_attribute\
            ("validationMessage")
        return validation_message
