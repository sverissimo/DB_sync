from utils.parse_data import parse_data
from models import seguros
from controller import api

seguro_model = {
    "name": seguros,
    "file_names": seguros.file_names,
    "fields": seguros.fields,
    "steps": seguros.steps,
    "formatData": seguros.formatData,
}


def test_parse_seguros_value():

    # api is mocked in conftest.py, returns veiculos_mock.json
    json_data = api.get("/api/veiculos")

    return_data = parse_data(json_data, seguro_model)
    assert return_data[0]["apolice"] == "1002306082568"
    assert return_data[0]["codigo_empresa"] == "9060"
    assert return_data[0]["vencimento"] == "2022-10-04"
    return return_data
