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


def get_sgti_data(model):

    downloaded_file_folder = env.SGTI_FILE_FOLDER
    module_name = model["name"]
    file_name = model["file_names"]["xls_file"]
    file_path = f"{downloaded_file_folder}\\{file_name}"
    user = env.USER
    secret = env.PASS
    browser = webdriver.Chrome(ChromeDriverManager().install())

    login(browser, user, secret, Keys)

    # Remove o arquivo existente para não ter conflito de nome com o novo download
    if os.path.exists(file_path):
        os.remove(file_path)

    if module_name == "old_vehicles":
        name_conflict = downloaded_file_folder + "\ConsultaVeiculos.xls"
        if os.path.exists(name_conflict):
            os.remove(name_conflict)
        get_old_vehicles(browser, Keys)
        print("damn!")
    else:
        steps = model["steps"]
        download_sgti_data(browser, Keys, steps)
    sleep(1)

    data = file_to_list(downloaded_file_folder, file_name, update_file=True)
    return data
