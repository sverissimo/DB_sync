import os
import datetime
from sys import argv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from importlib import import_module
from time import sleep
from dotenv import load_dotenv

from login import login
from get_sgti_data import get_sgti_data
from get_old_vehicles import get_old_vehicles
from create_sql_table import create_sql_table
from file_to_list import file_to_list
from parse_data import parse_data
from update_db import update_db
import api


load_dotenv()

# Usage: app.py <module_name> <environment> <include_old>
# Get input from user to import module
module_name = argv[1]
module_path = "entities." + module_name


module = import_module(module_path, ".")

# Declare variables
file_names = module.file_names
fields = module.fields
steps = module.steps
formatData = module.formatData

xls_file = file_names["xls_file"]
user_folder = os.getenv("USER_FOLDER")
xls_path = f"C:\\Users\\{user_folder}\\Downloads\\{xls_file}"

# set host (local / production)
production_url = "http://200.198.42.167"
local = "http://localhost:3001"

# Set headers
auth = os.getenv("AUTH_SYNC")
headers = {"authorization": auth}

proxies = {"http": None, "https": None}

host = local
include_old = False
if len(argv) > 2:
    if argv[2] == "production":
        host = production_url
if len(argv) > 3:
    if argv[3] == "include_old":
        include_old = True

print(host, "include_old; ", include_old)

# Check if file is older than 1 day:
one_day_old = True

if os.path.exists(xls_path):
    xls_timestamp = os.path.getmtime(xls_path)
    m_time = datetime.datetime.fromtimestamp(xls_timestamp)
    today = datetime.datetime.now()

    one_day_old = today - m_time > datetime.timedelta(hours=8)
    print(one_day_old)

# If older than 1 day, get new file from SGTI
if one_day_old:
    # Remove existing file (standard xls from sgti)
    if os.path.exists(xls_path):
        os.remove(xls_path)

    # create browser instance and pass to login function
    # browser = webdriver.Chrome()
    browser = webdriver.Chrome(ChromeDriverManager().install())
    login(browser, Keys)

    # navigates through SGTI to get xls file
    if include_old:
        get_old_vehicles(browser, Keys)
        print("shit")
        # exit()
    else:
        get_sgti_data(browser, Keys, steps)
    sleep(2)

# Change xls(sgti) file into a python list and updates if more than 1 dayold
# collection = file_to_list(xls_file, one_day_old)
collection = file_to_list(user_folder, xls_file, one_day_old)

# Se o módulo for veículos, essa lista é para fazer 3 atualizações no loop no final dessa função, referentes às
# 3 tabelas do Postgresql para atualizar.
# Optei por loop porque o arquivo do SGTI referente a veiculos, seguros e laudos é a mesma, depois é só rodar
# as validações e atualizações de tabela.

if module_name == "veiculos":
    tables_to_update = ["veiculos", "seguros", "laudos"]
else:
    tables_to_update = [module_name]

for table_name in tables_to_update:
    # Declara e inicializa variáveis:
    module_path = "entities." + table_name
    module = import_module(module_path, ".")

    fields = module.fields
    formatData = module.formatData
    sql_file = module.file_names["sql_file"]

    # Parse the list into the correct format/dataTypes of Postgresql DB
    table_to_postgres = parse_data(collection, fields, formatData, include_old)

    if include_old:
        print("updating mongo...")
        api.post("/sync/oldVehicles", table_to_postgres)
        # update_mongo_db(host, headers, table_to_postgres)
        print("Mongo updated.")
        exit()

    # DROPS (if exists) and creates a SQL table in PostgreSql from a sgti xls (html) file

    create_sql_table(sql_file)
    sleep(1)
    # Post the update request.
    update_db(table_to_postgres, table_name)

# Atualiza o status dos veículos com base nas datas de seguro e laudo e cria um restorePont do DB
if module_name == "veiculos":
    api.get("sync/forceDbUpdate")
    api.get("sync/createRestorePoint")
