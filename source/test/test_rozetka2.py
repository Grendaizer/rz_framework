from source.bin.pages.rozetka_powder_page import Powder_Home_Page
from source.bin.utils import delete_name_price_in_file,write_name_and_price_to_file
def test_rozetka_two(init_driver):
    powder_page = Powder_Home_Page(init_driver)
    powder_page.open_rozetka_main_page()
    powder_page.open_powder_catalog()
    delete_name_price_in_file()
    write_name_and_price_to_file(powder_page.get_all_name_price_devices())
    powder_page.open_second_page_catalog()
    write_name_and_price_to_file(powder_page.get_all_name_price_devices())
    powder_page.open_third_page_catalog()
    write_name_and_price_to_file(powder_page.get_all_name_price_devices())
    powder_page.open_four_page_catalog()
    write_name_and_price_to_file(powder_page.get_all_name_price_devices())
    powder_page.open_five_page_catalog()
    write_name_and_price_to_file(powder_page.get_all_name_price_devices())
