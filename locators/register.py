"""
Locators for register form are placed here
"""
from selenium.webdriver.common.by import By


# pylint: disable=too-few-public-methods
class RegisterElementLocators:
    """
    Locators for register form are placed here
    """

    FIRSTNAME = (By.ID, 'input-firstname')
    LASTNAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    CONFIRM_PASSWORD = (By.ID, 'input-confirm')
    CONTINUE = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')
    AGREE = (By.NAME, 'agree')


# pylint: disable=too-few-public-methods
class ErrorsRegisterElement:
    """
    Locators for register form errors are placed here
    """
    ETITLE = (By.XPATH, "//div[@id='account-register']/div")
    EFIRSTNAME = (By.XPATH, "//fieldset[@id='account']/div[2]/div/div")
    ELASTNAME = (By.XPATH, "//fieldset[@id='account']/div[3]/div/div")
    EEMAIL = (By.XPATH, "//fieldset[@id='account']/div[4]/div/div")
    ETELEPHONE = (By.XPATH, "//fieldset[@id='account']/div[5]/div/div")
    EPASSWORD = (By.XPATH, "//div[@id='content']/form/fieldset[2]/div/div/div")
    ECONFIRMPASSWORD = (By.XPATH, '//*[@id="content"]/form/fieldset[2]/div[2]/div/div')
