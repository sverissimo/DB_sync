from utils.parse_data import parse_data
from config import env
from models import veiculos
from controller import api

file_folder = f"{env.DB_SYNC_PATH_PY}\\app\\tests\\fixtures"
vehicle_file_path = f"{file_folder}\\veiculos_mock.json"

veiculo_model = {
    "name": "veiculos",
    "file_names": veiculos.file_names,
    "fields": veiculos.fields,
    "steps": veiculos.steps,
    "formatData": veiculos.formatData,
}
""" def open_json_file(file_path):
    with open(file=file_path, mode="r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data
        
json_data = open_json_file(vehicle_file_path) """


def test_parse_data_datatype():
    json_data = api.get("/api/veiculos")
    return_data = parse_data(json_data, veiculo_model)
    assert type(return_data) == list
    return


def test_parse_veiculos_value():
    json_data = api.get("/api/veiculos")
    return_data = parse_data(json_data, veiculo_model)
    assert return_data[0]["placa"] == "GXH-6110"
    assert return_data[0]["codigo_empresa"] == "9060"
    return return_data
