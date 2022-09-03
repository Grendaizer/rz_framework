import time

from source.settings import ROZETKA_URL
from selenium.webdriver.common.by import By
from source.settings import USER_MAIL, USER_PASS
from source.bin.setting_page.home_page_settings import GET_DEVICE_TV_SELECTOR, GET_DEVICE_PAGE_SELECTOR,GET_PAGE_2,GET_PAGE_3,GET_DEVICE_TITLE


class Home_Page:

    def __init__(self, driver):
        self.driver = driver

    def open_rozetka_main_page(self):
        self.driver.get(ROZETKA_URL)

    def select_page_with_device(self):
        catalog = self.driver.find_element(By.CSS_SELECTOR, GET_DEVICE_TV_SELECTOR())
        catalog.click()
        device_page = self.driver.find_element(By.CSS_SELECTOR, GET_DEVICE_PAGE_SELECTOR())
        device_page.click()

    def delete_info_in_file(self):
        file = open("device_name.txt", 'w')
        time.sleep(1)
        file.close()

    def write_all_name_device_in_file(self):
        global file
        try:
            file = open("device_name.txt", 'a')
            for i in range(1, 61):
                selector = self.driver.find_element(By.CSS_SELECTOR, GET_DEVICE_TITLE(i))
                name = selector.text
                file.write(name+'\n')
        finally:
            file.close()


    def open_second_page(self):
        page = self.driver.find_element(By.CSS_SELECTOR,GET_PAGE_2())
        page.click()

    def open_third_page(self):
        page = self.driver.find_element(By.CSS_SELECTOR,GET_PAGE_3())
        page.click()