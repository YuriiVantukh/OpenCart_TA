"""
Home Page comes here.
"""
import logging
import time
from urllib.parse import urlparse

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base import BasePageLocators
from .cart import CartPage
from .login import LoginPage
from .products import ProductsPage
from .returns import ReturnsPage
from .base import BasePage

DRIVER_WAIT_TIME = 1

# pylint: disable=too-many-public-methods
class HomePage(BasePage):
    """
    Home Page methods come here.
    """
    def goto_login(self):
        """
        Go to Login Page.
        """
        self.driver.find_element(*BasePageLocators.MY_ACCOUNT_DROPDOWN).click()
        self.driver.find_element(*BasePageLocators.GO_LOGIN).click()
        return LoginPage(self.driver)

    def is_on_home_page(self) -> bool:
        """
        Check whether driver is on home page now.

        :return: True if you are on home page, False if not
        """
        current_url_path = urlparse(self.driver.current_url).path
        if current_url_path == "/opencart.com/":
            logging.info("You are on home page!")
            return True
        logging.error("Something went wrong!")
        return False

    def goto_cart(self) -> "CartPage":
        """
        Click on the Shopping Cart tab.

        :return: CartPage object
        """
        self.driver.find_element(*BasePageLocators.GO_CART).click()
        logging.info("Clicked on the Shopping Cart tab")
        return CartPage(self.driver)

    def goto_returns(self) -> "ReturnsPage":
        """
        Go to Returns Page.

        :return: object of ReturnsPage class
        """
        self.driver.find_element(*BasePageLocators.RETURNS).click()
        return ReturnsPage(self.driver)

    def click_nav_components(self) -> "HomePage":
        """
        Click on the Components Tab.

        :return: Home page object with dropped out components list
        """
        self.driver.find_element(*BasePageLocators.COMPONENTS).click()
        logging.info("Clicked on on the Components Tab")
        return self

    def click_nav_components_monitors(self) -> "ProductsPage":
        """
        Click on the Component Tab and on the Monitors link after that.

        :return: ProductsPage object
        """
        self.click_nav_components()
        monitors = self.driver.find_element(*BasePageLocators.MONITORS)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(BasePageLocators.MONITORS))
        monitors.click()
        logging.info("Clicked on on the Monitors link")
        return ProductsPage(self.driver)

    def click_nav_phones(self) -> "ProductsPage":
        """
        Click on the Phones Tab.

        :return: ProductsPage object
        """
        self.driver.find_element(*BasePageLocators.PHONES).click()
        logging.info('Clicked on the Phones tab')
        return ProductsPage(self.driver)

    def click_nav_desktops(self) -> "HomePage":
        """
        Click Desktops Tab.

        :return: Home Page with clicked Desktops Navigation Bar.
        """
        logging.info('clicking top Navigation Desktops Bar')
        self.driver.find_element(*BasePageLocators.DESKTOPS).click()
        time.sleep(DRIVER_WAIT_TIME)
        return self

    def click_nav_laptops(self) -> "HomePage":
        """
        Click Laptops Tab.
        :return:self
        """
        self.driver.find_element(*BasePageLocators.LAPTOPS).click()
        return self

    def click_nav_tablets(self) -> ProductsPage:
        """
        Click Tablets Tab.
        :return:driver
        """
        self.driver.find_element(*BasePageLocators.TABLETS).click()
        return ProductsPage(self.driver)

    def click_nav_cameras(self) -> ProductsPage:
        """
        Click Cameras Tab.
        :return:driver
        """
        self.driver.find_element(*BasePageLocators.CAMERAS).click()
        return ProductsPage(self.driver)

    def click_nav_mp3_players(self) -> "HomePage":
        """
        Click MP3 Players Tab.
        :return:self
        """
        self.driver.find_element(*BasePageLocators.MP3S).click()
        return self

    def click_nav_desktops_pc(self) -> ProductsPage:
        """
        Click Desktops Tab.
        Click Pc.
        :return:driver
        """
        self.click_nav_desktops()
        self.driver.find_element(*BasePageLocators.PC).click()
        return ProductsPage(self.driver)

    def click_nav_desktops_mac(self) -> "ProductsPage":
        """
        Click Desktops Tab.
        Click Mac.

        :return: Products MAC Page Object
        """
        logging.info('clicking top navigation for getting to the Desktops->MAC Products Page')
        self.click_nav_desktops()
        time.sleep(1)
        self.driver.find_element(*BasePageLocators.MAC).click()
        time.sleep(1)
        return ProductsPage(self.driver)

    def click_nav_desktops_show_all(self) -> ProductsPage:
        """
        Click Desktops Tab.
        Click Show all desktops.
        :return:driver
        """
        self.click_nav_desktops()
        self.driver.find_element(*BasePageLocators.ALL_DESKTOPS).click()
        return ProductsPage(self.driver)

    def click_nav_laptops_macs(self) -> ProductsPage:
        """
        Click Laptops Tab.
        Click Macs.
        :return:driver
        """
        self.click_nav_laptops()
        self.driver.find_element(*BasePageLocators.MACS).click()
        return ProductsPage(self.driver)

    def click_nav_laptops_windows(self) -> ProductsPage:
        """
        Click Laptops Tab.
        Click Windows.
        :return:driver
        """
        self.click_nav_laptops()
        self.driver.find_element(*BasePageLocators.WINDOWS).click()
        return ProductsPage(self.driver)

    def click_nav_laptops_show_all(self) -> ProductsPage:
        """
        Click Laptops Tab.
        Click Show all Laptops .
        :return:driver
        """
        self.click_nav_laptops()
        self.driver.find_element(*BasePageLocators.ALL_LAPTOPS).click()
        return ProductsPage(self.driver)

    def click_nav_components_mice(self) -> ProductsPage:
        """
        Click Components Tab.
        Click Mice .
        :return:driver
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.MICE).click()
        return ProductsPage(self.driver)

    def click_nav_components_printers(self) -> ProductsPage:
        """
        Click Components Tab.
        Click Printers .
        :return:driver
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.PRINTERS).click()
        return ProductsPage(self.driver)

    def click_nav_components_scanners(self) -> ProductsPage:
        """
        Click Components Tab.
        Click Scanners.
        :return:driver
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.SCANNERS).click()
        return ProductsPage(self.driver)

    def click_nav_components_webcamera(self) -> ProductsPage:
        """
        Click Components Tab.
        Click Web Camera.
        :return:driver
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.WEBCAMERAS).click()
        return ProductsPage(self.driver)

    def click_nav_components_show_all(self)->ProductsPage:
        """
        Click Components Tab.
        Click Show all components.
        :return:driver
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.ALL_COMPONENTS).click()
        return ProductsPage(self.driver)

    def get_components_list(self) -> list:
        """
        Find all subcategory Components
        :return:subcategory components
        """
        components_list = self.driver.find_elements(*BasePageLocators.LIST_COMPONENTS)
        return components_list

    def get_desktops_list(self) -> list:
        """
        Find all subcategory Desktops
        :return:subcategory desktops
        """
        desktops_list = self.driver.find_elements(*BasePageLocators.LIST_DESKTOPS)
        return desktops_list

    def get_laptops_list(self) -> list:
        """
        Find all subcategory Laptops
        :return:subcategory laptops
        """
        laptops_list = self.driver.find_elements(*BasePageLocators.LIST_LAPTOPS)
        return laptops_list

    def get_product_quantity(self) -> str:
        """
        Get quantity of the products into the Cart text.

        :return: Text of product quantity.
        """
        logging.info('getting the text of product quantity into the Cart')
        edited_cart = self.driver.find_element(*BasePageLocators.BTN_GREY_CARD_AMOUNT)
        return edited_cart.text

    def logout(self) -> "HomePage":
        """
        Logout from user's account.
        """
        logging.info("Click on 'My Account' dropdown and click 'Logout'.")
        time.sleep(DRIVER_WAIT_TIME)
        self.driver.find_element(*BasePageLocators.MY_ACCOUNT_DROPDOWN).click()
        self.driver.find_element(*BasePageLocators.LOGOUT).click()
        return self

    def title(self) -> str:
        """
        find the page name
        :return:page title
        """
        return self.driver.title
