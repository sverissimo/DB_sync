import os
import datetime
from sys import argv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from importlib import import_module

from login import login
from get_sgti_data import get_sgti_data
from time import sleep
from create_sql_table import create_sql_table
from file_to_list import file_to_list
from parse_data import parse_data
from update_db import update_db

# Get input from user to import module
module_name = argv[1]

module_path = 'entities.' + module_name

module = import_module(module_path, '.')

# Declare variables
file_names = module.file_names
fields = module.fields
steps = module.steps
formatData = module.formatData

xls_file = file_names['xls_file']
xls_path = f'C:\\Users\\sandr\\Downloads\\{xls_file}'

# Check if file is older than 1 day:
one_day_old = True

if os.path.exists(xls_path):
    xls_timestamp = os.path.getmtime(xls_path)
    m_time = datetime.datetime.fromtimestamp(xls_timestamp)
    today = datetime.datetime.now()

    one_day_old = today - m_time > datetime.timedelta(1)
    print(one_day_old)

# If older than 1 day, get new file from SGTI
if one_day_old:
    # Remove existing file (standard xls from sgti)
    if os.path.exists(xls_path):
        os.remove(xls_path)

    # create browser instance and pass to login function
    browser = webdriver.Chrome()
    login(browser, Keys)

    # navigates through SGTI to get xls file
    get_sgti_data(browser, Keys, steps)
    sleep(2)

# Change xls(sgti) file into a python list and updates if more than 1 dayold
#collection = file_to_list(xls_file, one_day_old)
collection = file_to_list(xls_file, one_day_old)

# Se o módulo for veículos, essa lista é para fazer 3 atualizações no loop no final dessa função, referentes às 3 tabelas do Postgresql para atualizar.
# Optei por loop porque o arquivo do SGTI referente a veiculos, seguros e laudos é a mesma, depois é só rodar as validações e atualizações de tabela.
modules_to_update = []
if module_name == 'veiculos':
    modules_to_update = ['veiculos', 'seguros', 'laudos']
else:
    modules_to_update = [module_name]


for m in modules_to_update:
    # Declara e inicializa variáveis:
    module_path = 'entities.' + m
    module = import_module(module_path, '.')

    fields = module.fields
    formatData = module.formatData
    sql_file = module.file_names['sql_file']

    # Parse the list into the correct format/dataTypes of Postgresql DB
    table_to_postgres = parse_data(collection, fields, formatData)

    # DROPS (if exists) and creates a SQL table in PostgreSql from a sgit xls (html) file
    create_sql_table(sql_file)
    sleep(1)
    # Post the update request.
    update_db(table_to_postgres, m)
