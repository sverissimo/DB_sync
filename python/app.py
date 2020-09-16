import os
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

file_name = file_names['xls_file']
file_path = f'C:\\Users\\sandr\\Downloads\\{file_name}'
sql_file = file_names['sql_file']

""" # Remove existing file (standard xls from sgti)
if os.path.exists(file_path):
    os.remove(file_path)

# create browser instance and pass to login function
browser = webdriver.Chrome()
login(browser, Keys)

# navigates through SGTI to get xls file
get_sgti_data(browser, Keys, steps)
sleep(2)

# DROPS (if exists) and creates a SQL table in PostgreSql from a sgit xls (html) file
create_sql_table(sql_file)
sleep(2) """

# Change xls(sgti) file into a python list
collection = file_to_list(file_name)
# Parse the list into the correct format/dataTypes of Postgresql DB
table_to_postgres = parse_data(collection, fields, formatData)
# Post the update request.
# update_db(table_to_postgres)
