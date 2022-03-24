from utils.file_to_list import file_to_list
from config import env

file_folder = f"{env.DB_SYNC_PATH_PY}\\app\\tests\\fixtures"
vehicle_file_name = "veiculos_mock.xls"
socios_file_name = "socios_de_delegatarios_mock.xls"


def test_file_to_list_return_type():
    # Vehicle data simulation
    veiculos_list = file_to_list(file_folder, vehicle_file_name, True)
    assert type(veiculos_list) == list
    assert isinstance(veiculos_list, str) == False

    # Socios data simulation
    socios_list = file_to_list(file_folder, socios_file_name, True)
    assert type(socios_list) == list
    assert isinstance(socios_list, str) == False


def test_file_to_list_vehicles():
    veiculos_list = file_to_list(file_folder, vehicle_file_name, True)
    assert veiculos_list[0]["Placa"] == "GXH6110"
    assert veiculos_list[len(veiculos_list) - 1]["Placa"] == "GXH6214"


def test_file_to_list_socios():
    socios_list = file_to_list(file_folder, socios_file_name, True)
    last_socio_name = socios_list[len(socios_list) - 1]["Nome sócio"]

    assert socios_list[0]["Nome sócio"] == "10ª ALTERAÇÃO CONTRATUAL"
    assert last_socio_name == "MARIA APARECIDA MENDES ALVARES"
