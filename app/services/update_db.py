from controller import api


def update_db(sgti_data, table):

    request_data = {"table": table, "sgti_data": sgti_data}

    api.post("sync/updateTable", request_data)
    print(f"-- {table} updated.")
