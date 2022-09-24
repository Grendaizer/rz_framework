from source.settings import ROZETKA_URL
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from source.bin.setting_page.powder_page_settings import GET_POWDER_PRICE, \
    GET_POWDER_NAME, GET_WASHING_POWDER_PAGE_THREE, GET_WASHING_POWDER_PAGE_TWO, \
    GET_WASHING_POWDER_PAGE_FOUR, GET_WASHING_POWDER_PAGE_FIVE, GET_POWDER_OLD_PRICE


class Powder_Home_Page:
    def __init__(self, driver):
        self.driver = driver

    HOUSEHOLD_PRODUCTS = '.menu-categories_type_main > li:nth-child(5) > a:nth-child(1)'
    WASHING_POWDER = 'rz-widget-list.ng-star-inserted:nth-child(3) > section:nth-child(1) > ul:nth-child(2) > li:nth-child(5) > rz-list-tile:nth-child(1) > div:nth-child(1) > ul:nth-child(3) > li:nth-child(2) > a:nth-child(1)'

    def get_all_name_price_devices(self):
        global D
        self.driver.refresh()
        try:
            for i in range(1, 61):
                price = self.driver.find_element(By.CSS_SELECTOR, GET_POWDER_PRICE(i)).text
                if price:
                    price = self.driver.find_element(By.CSS_SELECTOR, GET_POWDER_PRICE(i)).text
                else:
                    price = self.driver.find_element(By.CSS_SELECTOR, GET_POWDER_OLD_PRICE(i))
                name = self.driver.find_element(By.CSS_SELECTOR, GET_POWDER_NAME(i)).text
                D = {str(name): str(price)}
        except NoSuchElementException:
            pass
        return D

    def open_rozetka_main_page(self):
        self.driver.get(ROZETKA_URL)

    def open_powder_catalog(self):
        hhp_button = self.driver.find_element(By.CSS_SELECTOR, self.GET_HOUSEHOLD_PRODUCTS_PAGE())
        hhp_button.click()
        wash = self.driver.find_element(By.CSS_SELECTOR, self.GET_WASHING_POWDER_PAGE())
        wash.click()

    def open_second_page_catalog(self):
        page2 = self.driver.find_element(By.CSS_SELECTOR, GET_WASHING_POWDER_PAGE_TWO())
        page2.click()

    def open_third_page_catalog(self):
        page3 = self.driver.find_element(By.CSS_SELECTOR, GET_WASHING_POWDER_PAGE_THREE())
        page3.click()

    def open_four_page_catalog(self):
        page4 = self.driver.find_element(By.CSS_SELECTOR, GET_WASHING_POWDER_PAGE_FOUR())
        page4.click()

    def open_five_page_catalog(self):
        page5 = self.driver.find_element(By.CSS_SELECTOR, GET_WASHING_POWDER_PAGE_FIVE())
        page5.click()

    def GET_HOUSEHOLD_PRODUCTS_PAGE(self) -> str:
        return self.HOUSEHOLD_PRODUCTS

    def GET_WASHING_POWDER_PAGE(self) -> str:
        return self.WASHING_POWDER
