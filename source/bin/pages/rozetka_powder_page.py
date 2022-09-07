import time
from source.settings import ROZETKA_URL
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from source.bin.setting_page.powder_page_settings import \
    GET_HOUSEHOLD_PRODUCTS_PAGE, GET_WASHING_POWDER_PAGE, GET_POWDER_PRICE,\
    GET_POWDER_NAME, GET_WASHING_POWDER_PAGE_THREE, GET_WASHING_POWDER_PAGE_TWO, \
    GET_WASHING_POWDER_PAGE_FOUR, GET_WASHING_POWDER_PAGE_FIVE,GET_POWDER_OLD_PRICE


class Powder_Home_Page:
    def __init__(self, driver):
        self.driver = driver

    def open_rozetka_main_page(self):
        self.driver.get(ROZETKA_URL)

    def delete_info_in_file(self):
        file = open("name_price.txt", 'w')
        time.sleep(1)
        file.close()

    def open_powder_catalog(self):
        hhp_button = self.driver.find_element(By.CSS_SELECTOR, GET_HOUSEHOLD_PRODUCTS_PAGE)
        hhp_button.click()
        wash = self.driver.find_element(By.CSS_SELECTOR, GET_WASHING_POWDER_PAGE)
        wash.click()

    def open_second_page_catalog(self):
        page2 = self.driver.find_element(By.CSS_SELECTOR, GET_WASHING_POWDER_PAGE_TWO)
        page2.click()

    def open_third_page_catalog(self):
        page3 = self.driver.find_element(By.CSS_SELECTOR, GET_WASHING_POWDER_PAGE_THREE)
        page3.click()

    def open_four_page_catalog(self):
        page4 = self.driver.find_element(By.CSS_SELECTOR, GET_WASHING_POWDER_PAGE_FOUR)
        page4.click()

    def open_five_page_catalog(self):
        page5 = self.driver.find_element(By.CSS_SELECTOR, GET_WASHING_POWDER_PAGE_FIVE)
        page5.click()

    def write_name_and_price_to_file(self):
        global file
        try:
            file = open('name_price.txt', 'a')
            self.driver.refresh()
            time.sleep(2)
            for i in range(1, 61):
                price = self.driver.find_element(By.CSS_SELECTOR, GET_POWDER_PRICE(i)).text
                if price:
                    price = self.driver.find_element(By.CSS_SELECTOR, GET_POWDER_PRICE(i)).text
                else:
                    price = self.driver.find_element(By.CSS_SELECTOR,GET_POWDER_OLD_PRICE(i))
                name = self.driver.find_element(By.CSS_SELECTOR, GET_POWDER_NAME(i)).text
                D = {str(name): str(price)}
                a = {key: value for key, value in D.items() if int(value) > 100 if int(value) < 300}
                for id1, id2 in a.items():
                    file.write(id1 + ":" + id2 + "\n")
        except NoSuchElementException:
            pass
        finally:
            file.close()
