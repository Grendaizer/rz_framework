from source.bin.pages.rozetka_powder_page import Powder_Home_Page

def test_rozetka_two(init_driver):
    powder_page = Powder_Home_Page(init_driver)
    powder_page.open_rozetka_main_page()
    powder_page.open_powder_catalog()
    powder_page.delete_info_in_file()
    powder_page.write_name_and_price_to_file()
    powder_page.open_second_page_catalog()
    powder_page.write_name_and_price_to_file()
    powder_page.open_third_page_catalog()
    powder_page.write_name_and_price_to_file()
    powder_page.open_four_page_catalog()
    powder_page.write_name_and_price_to_file()
    powder_page.open_five_page_catalog()
    powder_page.write_name_and_price_to_file()
