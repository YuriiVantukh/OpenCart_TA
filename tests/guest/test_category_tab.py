import allure
import pytest

from helpers.settings import BASE_HOST
from pages.home import HomePage
from db.categ import quantity_desktops, quantity_laptops, quantity_components


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The PC window opens when a user clicks on a PC link on the category tab')
def test_pc(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_desktops_pc()
    assert ('PC' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The Mac window opens when a user clicks on a Mac link on the category tab')
def test_mac(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_desktops_mac()
    assert ('Mac' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The all desktops window opens when a user clicks on a '
             'show all desktops link on the category tab')
def test_show_all_desktops(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_desktops_show_all()
    assert ('Desktops' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.CRITICAL
@allure.step('count subcategoty in desktops tab')
def test_count_category_desktop(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    list_cat_desktops = page.get_desktops_list()
    assert (len(list_cat_desktops) == quantity_desktops)


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.CRITICAL
@allure.step('subcategorys in desktops tab is visibel')
def test_display_category_desktop(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_desktops()
    list_cat_desktops = page.get_desktops_list()
    for list in list_cat_desktops:
        assert (list.is_displayed())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The macs window opens when a user clicks on a macs link on the category tab')
def test_macs(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_laptops_macs()
    assert ('Macs' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The mwindow opens when a user clicks on a windows link on the category tab')
def test_windows(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_laptops_windows()
    assert ('Windows' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The all laptops  opens when a user clicks on a show all laptops link on the category tab')
def test_show_all_laptops(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_laptops_show_all()
    assert ('Laptops & Notebooks' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.CRITICAL
@allure.step('subcategorys in laptops tab is visibel')
def test_display_category_laptops(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_laptops()
    list_cat_laptops = page.get_laptops_list()
    for list in list_cat_laptops:
        assert (list.is_displayed())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.CRITICAL
@allure.step('count subcategoty in laptops tab')
def test_count_category_laptops(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    list_cat_laptops = page.get_laptops_list()
    assert (len(list_cat_laptops) == quantity_laptops)


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The mice  opens when a user clicks on   mice link on the category tab')
def test_mice(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_components_mice()
    assert ('Mice and Trackballs' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The monitors  opens when a user clicks on   monitors link on the category tab')
def test_monitirs(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_components_monitors()
    assert ('Monitors' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The printers  opens when a user clicks on   printers link on the category tab')
def test_printers(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_components_printers()
    assert ('Printers' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The printers  opens when a user clicks on   printers link on the category tab')
def test_scanner(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_components_scanners()
    assert ('Scanners' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The webcamera  opens when a user clicks on   webcamera link on the category tab')
def test_webcamera(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_components_webcamera()
    assert ('Web Cameras' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The all componets  opens when a user clicks on a show all components  link on the category tab')
def test_all_components(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_components_show_all()
    assert ('Components' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.CRITICAL
@allure.step('subcategorys in components tab is visibel')
def test_display_category_components(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_components()
    list_cat_components = page.get_components_list()
    for list in list_cat_components:
        assert (list.is_displayed())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.CRITICAL
@allure.step('count subcategorys in components')
def test_count_category_components(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    list_cat_components = page.get_components_list()
    assert (len(list_cat_components) == quantity_components)


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The tablets  opens when a user clicks on tablets  link on the category tab')
def test_tablets(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_tablets()
    assert ('Tablets' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The phone  opens when a user clicks on phone  link on the category tab')
def test_phone(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_phones()
    assert ('Phones & PDAs' == page.title())


@pytest.mark.skip(reason="this person already got a job")
@pytest.allure.BLOCKER
@allure.step('The camera  opens when a user clicks on camera  link on the category tab')
def test_camera(init_driver):
    driver = init_driver
    driver.get(BASE_HOST)
    page = HomePage(driver)
    page.click_nav_cameras()
    assert ('Cameras' == page.title())
