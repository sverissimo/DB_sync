import os
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from config import env


def get_old_vehicles(browser, Keys):
    steps = [4, 3, 3]
    actions = ActionChains(browser)
    space = Keys.SPACE
    enter = Keys.ENTER

    # Navbar menu
    actions = ActionChains(browser)
    sleep(2)
    for _ in range(steps[0]):
        actions = actions.send_keys(Keys.TAB)
    actions.perform()

    # Consultas
    actions = ActionChains(browser)
    sleep(1)
    for _ in range(steps[1]):
        actions = actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()

    # Veiculos
    actions = ActionChains(browser)
    sleep(1)
    for _ in range(steps[2]):
        actions = actions.send_keys(Keys.ARROW_DOWN)
    actions = actions.send_keys(Keys.RETURN)
    actions.perform()
    print("consultas>>veiculos")

    sleep(3)
    # include_old_vehicles = browser.find_element_by_name("tpRldc:sbc2")
    include_old_vehicles = browser.find_element_by_id("tpRldc:sbc2::content")

    search = browser.find_element_by_id("tpRldc:cb2")
    include_old_vehicles.send_keys(space)
    search.send_keys(enter)
    sleep(5)

    download = browser.find_element_by_id("tpRldc:pc1:ctb1").find_element_by_tag_name(
        "a"
    )
    print("downloading... (this might take a while)")
    download.send_keys(enter)
    file_path = env.SGTI_FILE_FOLDER + "\ConsultaVeiculos.xls"

    while not os.path.exists(file_path):
        sleep(1)

    if os.path.isfile(file_path):
        new_file_path = env.SGTI_FILE_FOLDER + "\OldVehicles.xls"
        os.rename(file_path, new_file_path)

    browser.close()
