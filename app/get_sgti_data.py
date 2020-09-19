from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def get_sgti_data(browser, Keys, steps):
    actions = ActionChains(browser)

    sleep(2)
    for _ in range(steps[0]):
        actions = actions.send_keys(Keys.TAB)
    actions.perform()
    print('consultas')

    actions = ActionChains(browser)
    sleep(1)
    actions = actions.send_keys(Keys.RETURN)
    actions.perform()

    sleep(1)
    actions = ActionChains(browser)
    if steps[1] > 0:
        for _ in range(steps[1]):
            actions = actions.send_keys(Keys.TAB)
    actions = actions.send_keys(Keys.RETURN)
    actions.perform()

    sleep(1)
    actions = ActionChains(browser)
    for _ in range(steps[2]):
        actions = actions.send_keys(Keys.TAB)
    print('entity')
    actions.perform()

    sleep(1)
    actions = ActionChains(browser)
    actions = actions.send_keys(Keys.RETURN)
    actions.perform()

    sleep(1)
    for _ in range(steps[3]):

        actions = actions.send_keys(Keys.TAB)
    actions.perform()
    print('downloaded.')

    sleep(2)
    actions = ActionChains(browser)
    actions = actions.send_keys(Keys.RETURN)
    actions.perform()

    """
    for _ in range(13):
        print('13')
        actions = actions.send_keys(Keys.TAB)
    actions.perform()


    browser.type('1234', id='j_password')
    browser.click(id='submitButton')

    sleep(4)
    for i in range(3):
        print(i)
        browser.press(browser.Key.TAB)

    sleep(2)
    browser.press(browser.Key.TAB)

    #driver.press(driver.Key.SHIFT+ driver.Key.TAB)
    """
