import time


def delete_text_in_file():
    file = open("device_name.txt", 'w')
    time.sleep(1)
    file.close()


def write_all_name_device_in_file(name_device):
    global file
    try:
        file = open("device_name.txt", 'a')
        for var in name_device:
            file.write(var + '\n')
    finally:
        file.close()
