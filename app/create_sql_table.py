import requests
from pathlib import Path


def create_sql_table(sql_file):
    path_to_file = f'C:\\Users\\sandr\\OneDrive\\DB_sync\\SQL_scripts\\{sql_file}'
    create_empresas_table = open(path_to_file, 'r')
    empresas_query = create_empresas_table.read()

    query = {'query': empresas_query}
    print(query)
    r = requests.post('http://localhost:3001/sync/createTable', query)

    print(r.text)