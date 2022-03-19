from sys import argv
from importlib import import_module
from time import sleep

from services.get_sgti_data import get_sgti_data
from services.create_sql_table import create_sql_table
from services.update_db import update_db
from utils.file_to_list import file_to_list
from utils.parse_data import parse_data
from controller import api
from services.check_updates import check_data_updates
from config import env


def main(entity, include_old_vehicles):

    module_path = "models." + entity
    module = import_module(module_path, ".")

    model = {
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

    collection = data

    fields = module.fields
    formatData = module.formatData

    # Se o módulo for veículos, essa lista é para fazer 3 atualizações no loop no final dessa função, referentes às
    # 3 tabelas do Postgresql para atualizar.
    # Optei por loop porque o arquivo do SGTI referente a veiculos, seguros e laudos é a mesma, depois é só rodar
    # as validações e atualizações de tabela.

    if entity == "veiculos":
        tables_to_update = ["veiculos", "seguros", "laudos"]
    else:
        tables_to_update = [entity]

    for table_name in tables_to_update:
        # Declara e inicializa variáveis:
        module_path = "models." + table_name
        module = import_module(module_path, ".")

        fields = module.fields
        formatData = module.formatData
        sql_file = module.file_names["sql_file"]

        # Parse the list into the correct format/dataTypes of Postgresql DB
        table_to_postgres = parse_data(
            collection, fields, formatData, include_old_vehicles
        )

        if include_old_vehicles:
            print("updating mongo...")
            api.post("/sync/oldVehicles", table_to_postgres)
            print("Mongo updated.")
            exit()

        # DROPS (if exists) and creates a SQL table in PostgreSql from a sgti xls (html) file

        create_sql_table(sql_file)
        sleep(1)
        # Post the update request.
        update_db(table_to_postgres, table_name)

    # Atualiza o status dos veículos com base nas datas de seguro e laudo e cria um restorePont do DB
    if entity == "veiculos":
        api.get("sync/forceDbUpdate")
        api.get("sync/createRestorePoint")


# Usage: app.py <entity> <include_old_vehicles?>
if __name__ == "__main__":
    entity = None
    try:
        entity = argv[1]
        include_old_vehicles = False
        if len(argv) < 2:
            argv[2] = "None"
            if argv[2] == "include_old_vehicles":
                include_old_vehicles = True
        main(entity, include_old_vehicles)
    except IndexError:
        print(
            "You need to pass an argument specifying the module you are trying to sync."
        )
        exit()
