from sys import argv
from importlib import import_module

from services.get_sgti_data import get_sgti_data
from services.create_sql_table import create_sql_table
from services.update_db import update_db
from utils.file_to_list import file_to_list
from utils.parse_data import parse_data
from controller import api
from services.check_updates import check_data_updates
from config import env


def main(entity):

    module_path = "models." + entity
    module = import_module(module_path, ".")
    model = {
        "name": entity,
        "file_names": module.file_names,
        "fields": module.fields,
        "steps": module.steps,
        "formatData": module.formatData,
    }
    data = None
    sgti_file_folder = env.SGTI_FILE_FOLDER
    should_update = check_data_updates(model, sgti_file_folder)

    if should_update:
        data = get_sgti_data(model)
    else:
        xls_file = model["file_names"]["xls_file"]
        data = file_to_list(sgti_file_folder, xls_file, update_file=False)

    db_formatted_data = parse_data(data, model)

    # Veículos baixados ficam armazenados no MongoDB
    if model["name"] == "old_vehicles":
        api.post("sync/oldVehicles", db_formatted_data)
        print("Mongo updated.")
        exit()

    sql_file = module.file_names["sql_file"]
    create_sql_table(sql_file)
    update_db(db_formatted_data, table=entity)

    if entity == "veiculos":
        main("seguros")
        main("laudos")

        # Atualiza o status dos veículos com base nas datas de seguro e laudo e cria um restorePont do DB
        api.get("sync/forceDbUpdate")
        api.get("sync/createRestorePoint")
        exit()


# Usage: app.py <entity>
if __name__ == "__main__":
    entity = None
    try:
        entity = argv[1]
        main(entity)
    except IndexError:
        print(
            "You need to pass an argument specifying the module you are trying to sync."
        )
        exit()
