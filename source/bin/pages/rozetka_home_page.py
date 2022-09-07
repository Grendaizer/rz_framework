import time

from source.settings import ROZETKA_URL
from selenium.webdriver.common.by import By
from source.settings import USER_MAIL, USER_PASS
from source.bin.pages.rozetka_device_page import Device_Page


class Home_Page(Device_Page):
    DEVICE_TV_SELECTOR = '.menu-categories_type_main > li:nth-child(2) > a:nth-child(1)'
    DEVICE_PAGE_SELECTOR = 'rz-list-tile:nth-child(1) > div:nth-child(1) > a:nth-child(2)'

    def __init__(self, driver):
        self.driver = driver

    def open_rozetka_main_page(self):
        self.driver.get(ROZETKA_URL)

    def select_page_with_device(self):
        catalog = self.driver.find_element(By.CSS_SELECTOR, self.GET_DEVICE_TV_SELECTOR)
        catalog.click()
        device_page = self.driver.find_element(By.CSS_SELECTOR, self.GET_DEVICE_PAGE_SELECTOR)
        device_page.click()

    @property
    def GET_DEVICE_TV_SELECTOR(self) -> str:
        return self.DEVICE_TV_SELECTOR

    @property
    def GET_DEVICE_PAGE_SELECTOR(self) -> str:
        return self.DEVICE_PAGE_SELECTOR
