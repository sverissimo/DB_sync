from utils.parse_data import parse_data
from models import laudos
from controller import api

laudo_model = {
    "name": laudos,
    "file_names": laudos.file_names,
    "fields": laudos.fields,
    "steps": laudos.steps,
    "formatData": laudos.formatData,
}


def test_parse_laudos_value():

    # api is mocked in conftest.py, returns veiculos_mock.json
    json_data = api.get("/api/veiculos")

    return_data = parse_data(json_data, laudo_model)
    first_entry = return_data[0]
    assert first_entry["id"] == "004517"
    assert first_entry["validade"] == "01/04/2022"
    assert "veiculo_id" in first_entry
    assert "Número Laudo" not in first_entry
    return return_data
