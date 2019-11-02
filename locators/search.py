"""
Locators for Search Page are placed here
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class SearchPageLocators(BasePageLocators):
    """
    Locators for Search Page are placed here
    """
    SEARCH_FIELD = (By.NAME, 'search')
    SEARCH_BUTTON = (By.CLASS_NAME, 'btn btn-default btn-lg')

    SEARCH_KEYWORDS = (By.ID, 'input-search')
    SEARCH_IN_PRODUCT_DESCRIPTION_FLAG = (By.ID, 'description')
    SEARCH_CATEGORY = (By.NAME, 'category_id')
    SEARCH_IN_SUBCATEGORY_FLAG = (By.NAME, 'subcategory')
    SEARCH_BUTTON_LOCAL = (By.ID, 'button-search')

    # appears only if at least 1 product found (raises NoSuchElementException ?)
    MANAGE_SEARCH_RESULTS = (By.XPATH,
                             "//button[@id='list-view']//parent::"
                             "div//parent::div//parent::div[@class='row']")
    # appears only if at least 1 product found (raises NoSuchElementException ?)
    SEARCH_RESULTS = (By.XPATH, "//div[@class='product-thumb']")
