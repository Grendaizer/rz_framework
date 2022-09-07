from source.bin.pages.rozetka_home_page import Home_Page
from source.bin.utils import delete_text_in_file, write_all_name_device_in_file


def test_rozetka_first(init_driver):
    page = Home_Page(init_driver)
    delete_text_in_file()
    page.open_rozetka_main_page()
    page.select_page_with_device()
    write_all_name_device_in_file(page.get_all_name_devices())
    page.open_second_page()
    write_all_name_device_in_file(page.get_all_name_devices())
    page.open_third_page()
    write_all_name_device_in_file(page.get_all_name_devices())
