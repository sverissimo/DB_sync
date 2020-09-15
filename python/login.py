import os
from dotenv import load_dotenv, find_dotenv


def login(browser, Keys):

    load_dotenv(find_dotenv())
    user = os.getenv("USER")
    secret = os.getenv("PASS")

    browser.get("http://www.sgti.setop.mg.gov.br")
    #tst = browser.find_elements(id='j_username')
    login = browser.find_element_by_id('j_username')
    login.clear()
    login.send_keys(user)

    senha = browser.find_element_by_id('j_password')
    senha.clear()
    senha.send_keys(secret)
    senha.send_keys(Keys.RETURN)
