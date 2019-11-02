"""
Class Base comes here.
"""
from selenium import webdriver


# pylint: disable=too-few-public-methods
class BasePageElement:
    """Base element."""

    def __init__(self, driver=None):
        """
        Initialization of base driver.
        """
        self.driver = driver if driver else webdriver.Chrome()
