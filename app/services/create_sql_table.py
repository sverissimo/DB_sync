from controller import api
from config import env


def create_sql_table(sql_file):
    path = env.SQL_SCRIPTS_FOLDER
    path_to_file = f"{path}\\{sql_file}"

    with open(path_to_file, "r") as f:
        query_string = f.read()
        query = {"query": query_string}

        print(f"Now reading {sql_file} script...")

        api.post("sync/createTable", query)

        return query
