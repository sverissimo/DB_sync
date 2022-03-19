import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from sgti_api.login import login
from sgti_api.get_old_vehicles import get_old_vehicles
from sgti_api.download_sgti_data import download_sgti_data
from utils.file_to_list import file_to_list
from config import env


def get_sgti_data(model, include_old=False):

    downloaded_file_folder = env.SGTI_FILE_FOLDER

    file_name = model["file_names"]["xls_file"]
    file_path = f"{downloaded_file_folder}\\{file_name}"
    print("file_path: ", file_path)

    if os.path.exists(file_path):
        os.remove(file_path)

    browser = webdriver.Chrome(ChromeDriverManager().install())
    """ user = os.getenv("USER")
    secret = os.getenv("PASS") """
    user = env.USER
    secret = env.PASS
    login(browser, user, secret, Keys)

    if include_old:
        get_old_vehicles(browser, Keys)
        print("shit")
        # exit()
    else:
        steps = model["steps"]
        download_sgti_data(browser, Keys, steps)
    sleep(2)

    data = file_to_list(downloaded_file_folder, file_name, update_file=True)
    return data
