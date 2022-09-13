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


def delete_name_price_in_file():
    file = open("name_price.txt", 'w')
    time.sleep(1)
    file.close()


def write_name_and_price_to_file(name_price_dict):
    global file
    try:
        D = name_price_dict
        file = open('name_price.txt', 'a')
        time.sleep(2)
        a = {key: value for key, value in D.items() if int(value) > 100 if int(value) < 300}
        for id1, id2 in a.items():
            file.write(id1 + ":" + id2 + "\n")
    finally:
        file.close()
