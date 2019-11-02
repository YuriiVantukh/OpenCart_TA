"""
Class Button comes here.
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from elements.base import BasePageElement


# pylint: disable=too-few-public-methods
class Button(BasePageElement):
    """
    Button methods come here.
    """

    def __init__(self, driver, locator):
        """
        Add locator property

       :param driver: state of driver
       :param locator: tuple contains attribute available for By class and the same locator
        """
        super().__init__(driver)
        self.locator = locator

    def click(self):
        """
        Click on the button defined by the locator
        """
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.locator))
        self.driver.find_element(*self.locator).click()
