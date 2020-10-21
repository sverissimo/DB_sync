import requests
from pathlib import Path

production_url = 'http://200.198.42.167/sync/createTable'
local = 'http://localhost:3001/sync/createTable'


def create_sql_table(sql_file):
    path_to_file = f'C:\\Users\\sandr\\Coding\\DB_sync\\SQL_scripts\\{sql_file}'
    create_empresas_table = open(path_to_file, 'r')
    empresas_query = create_empresas_table.read()

    query = {'query': empresas_query}
    print(query)
    r = requests.post(local, query)

    print(r.text, sql_file)
