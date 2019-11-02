""""
Module contains class, which creates single DriverFactory that provides us specified WebDriver
"""

from selenium import webdriver


# pylint: disable=too-few-public-methods
class DriverFactory:
    """"
    Class to create single DriverFactory that provides us needed specified WebDriver
    """

    @staticmethod
    def get_driver(driver_name='chrome'):
        """
        Create driver according to given driver text name
        """
        if driver_name.lower() == 'chrome':
            _single_web_driver = webdriver.Chrome()
        elif driver_name.lower() == 'firefox':
            _single_web_driver = webdriver.Firefox()
        elif driver_name.lower() in ('ie', 'iexplorer', 'internetexplorer'):
            _single_web_driver = webdriver.Ie()
        elif driver_name.lower() == 'edge':
            _single_web_driver = webdriver.Edge()
        elif driver_name.lower() == 'safari':
            _single_web_driver = webdriver.Safari()
        elif driver_name.lower() == 'opera':
            _single_web_driver = webdriver.Opera()
        else:
            raise ValueError('Unknown name of browser')
        return _single_web_driver
