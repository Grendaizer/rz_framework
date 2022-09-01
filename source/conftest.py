import pytest
from selenium import webdriver


@pytest.fixture(autouse=False, scope='function')
def init_driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(time_to_wait=10)
    yield driver
    driver.quit()
