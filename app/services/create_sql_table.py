import os
from controller import api


def create_sql_table(sql_file):
    path = os.getenv("DB_SYNC_PATH_PY")
    print("path", path)
    path_to_file = f"{path}\\SQL_scripts\\{sql_file}"
    create_empresas_table = open(path_to_file, "r")
    empresas_query = create_empresas_table.read()

    query = {"query": empresas_query}
    # print(query)

    api.post("sync/createTable", query)
    print(sql_file)
