from source.bin.pages.rozetka_powder_page import Powder_Home_Page

def test_rozetka_two(init_driver):
    driver = Powder_Home_Page(init_driver)
    driver.open_rozetka_main_page()
    driver.open_powder_catalog()
    driver.delete_info_in_file()
    driver.write_name_and_price_to_file()
    driver.open_second_page_catalog()
    driver.write_name_and_price_to_file()
    driver.open_third_page_catalog()
    driver.write_name_and_price_to_file()
    driver.open_four_page_catalog()
    driver.write_name_and_price_to_file()
    driver.open_five_page_catalog()
    driver.write_name_and_price_to_file()
