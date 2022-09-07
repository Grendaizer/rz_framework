from source.bin.pages.rozetka_home_page import Home_Page

def test_rozetka_first(init_driver):
    homepage = Home_Page(init_driver)
    homepage.open_rozetka_main_page()
    homepage.select_page_with_device()
    homepage.delete_info_in_file()
    homepage.write_all_name_device_in_file()
    homepage.open_second_page()
    homepage.write_all_name_device_in_file()
    homepage.open_third_page()
    homepage.write_all_name_device_in_file()