from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def get_old_vehicles(browser, Keys):
    steps = [7, 2]
    actions = ActionChains(browser)
    tab = Keys.TAB
    space = Keys.SPACE
    enter = Keys.ENTER
    def press_key(key):
        actions.send_keys((key))

    sleep(2)
    for _ in range(steps[0]):
        press_key(tab)
    press_key(enter)
    actions.perform()
    sleep(1)

    for _ in range(steps[1]):
        press_key(tab)
    press_key(enter)
    actions.perform()
    sleep(2)

    include_old_vehicles = browser.find_element_by_name("tpRldc:sbc2")
    search = browser.find_element_by_id("tpRldc:cb2")
    include_old_vehicles.send_keys(space)
    search.send_keys(enter)
    sleep(8)

    download = browser.find_element_by_id("tpRldc:pc1:ctb1").find_element_by_tag_name("a")
    print(download)
    download.send_keys(enter)
    sleep(10)
    browser.close()
