"""
Class TextField comes here.
"""
from elements.base import BasePageElement


# pylint: disable=too-few-public-methods
class TextField(BasePageElement):
    """
    TextField methods come here.
    """

    def __init__(self, driver, locator):
        """
        Add _elem property

        :param driver: state of driver
        :param locator: tuple contains attribute available for By class and the same locator
        """
        super().__init__(driver)
        self._elem = self.driver.find_element(*locator)

    def set(self, value):
        """
        Set the value in the element

        :param value:
        :return: object of the class
        """
        self._elem.send_keys(value)
        return self

    def clear(self):
        """
        Clear the value in the element

        :return: object of the class
        """
        self._elem.clear()
        return self
