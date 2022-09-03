import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from source.bin.setting_page.device_page_setting import GET_PAGE_2, GET_PAGE_3, GET_DEVICE_TITLE


class Device_Page:

    def __init__(self, driver):
        self.driver = driver

    def delete_info_in_file(self):
        file = open("device_name.txt", 'w')
        time.sleep(1)
        file.close()

    def delete_top_device_info_in_file(self):
        file = open("top_name_price_device.txt", 'w')
        time.sleep(1)
        file.close()

    def select_top_device(self):
        device = []

    def wrile_name_price_top_device_in_file(self):
        pass

    def write_all_name_device_in_file(self):
        global file
        try:
            file = open("device_name.txt", 'a')
            for i in range(1, 61):
                selector = self.driver.find_element(By.CSS_SELECTOR, GET_DEVICE_TITLE(i))
                name = selector.text
                file.write(name + '\n')
        finally:
            file.close()

    def open_second_page(self):
        page = self.driver.find_element(By.CSS_SELECTOR, GET_PAGE_2())
        page.click()

    def open_third_page(self):
        page = self.driver.find_element(By.CSS_SELECTOR, GET_PAGE_3())
        page.click()
