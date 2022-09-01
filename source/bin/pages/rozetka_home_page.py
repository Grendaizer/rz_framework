from source.settings import ROZETKA_URL
from selenium.webdriver.common.by import By
from source.settings import USER_MAIL, USER_PASS
from source.bin.setting_page.home_page_settings import GET_DEVICE_TV_SELECTOR, GET_DEVICE_PAGE_SELECTOR


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

    def write_all_name_device_in_file(self):
        global file
        try:
            file = open("device_name.txt", 'a')
            for i in range(1, 61):
                DEVICE_TITLE = f"body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-grid > ul > li:nth-child({i}) > rz-catalog-tile > app-goods-tile-default > div > div.goods-tile__inner > a.goods-tile__heading.ng-star-inserted > span"
                selector = self.driver.find_element(By.CSS_SELECTOR, DEVICE_TITLE)
                name = selector.text
                file.write(name+'\n')
        finally:
            file.close()
