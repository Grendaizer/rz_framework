from source.bin.pages.rozetka_home_page import Home_Page

def test_rozetka_third(init_driver):
    driver = Home_Page(init_driver)
    driver.open_rozetka_main_page()
    driver.select_page_with_device()
    driver.delete_info_in_file()