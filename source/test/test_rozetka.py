from source.bin.pages.rozetka_home_page import Home_Page

def test_rozetka_first(init_driver):
    driver = Home_Page(init_driver)
    driver.open_rozetka_main_page()
    driver.select_page_with_device()
    driver.write_all_name_device_in_file()