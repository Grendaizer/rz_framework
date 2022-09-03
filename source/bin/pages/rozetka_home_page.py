import time

from source.settings import ROZETKA_URL
from selenium.webdriver.common.by import By
from source.settings import USER_MAIL, USER_PASS
from source.bin.pages.rozetka_device_page import Device_Page
from source.bin.setting_page.home_page_settings import GET_DEVICE_TV_SELECTOR, GET_DEVICE_PAGE_SELECTOR


class Home_Page(Device_Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_rozetka_main_page(self):
        self.driver.get(ROZETKA_URL)

    def select_page_with_device(self):
        catalog = self.driver.find_element(By.CSS_SELECTOR, GET_DEVICE_TV_SELECTOR())
        catalog.click()
        device_page = self.driver.find_element(By.CSS_SELECTOR, GET_DEVICE_PAGE_SELECTOR())
        device_page.click()