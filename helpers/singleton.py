"""Singleton for driver"""

from selenium.webdriver import Chrome

# pylint: disable=too-few-public-methods
class Wrapper:
    """Wrapper for driver"""
    instance = None
    connection = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Wrapper, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def webdriver_rem(self):
        """Init driver"""
        self.connection = Chrome()
        return self.connection
