from selenium.webdriver.common.by import By


class Device_Page:
    PAGE_TWO = 'li.pagination__item:nth-child(2) > a:nth-child(1)'
    PAGE_THREE = 'li.pagination__item:nth-child(3) > a:nth-child(1)'

    def __init__(self, driver):
        self.driver = driver

    def get_all_name_devices(self):
        L = []
        for i in range(1, 61):
            selector = self.driver.find_element(By.CSS_SELECTOR, self.GET_DEVICE_TITLE(i))
            L.append(selector.text)
        return L

    def open_second_page(self):
        page = self.driver.find_element(By.CSS_SELECTOR, self.GET_PAGE_2)
        page.click()

    def open_third_page(self):
        page = self.driver.find_element(By.CSS_SELECTOR, self.GET_PAGE_3)
        page.click()

    def GET_DEVICE_TITLE(self, x) -> str:
        DEVICE_TITLE = f"body > app-root > div > div > rz-category > div > main > rz-catalog > div > div > section > rz-grid > ul > li:nth-child({x}) > rz-catalog-tile > app-goods-tile-default > div > div.goods-tile__inner > a.goods-tile__heading.ng-star-inserted > span"
        return DEVICE_TITLE

    @property
    def GET_PAGE_2(self) -> str:
        return self.PAGE_TWO

    @property
    def GET_PAGE_3(self) -> str:
        return self.PAGE_THREE
