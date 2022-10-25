import json
import pytest
from controller import api
from config import env


def mock_get(endpoint: str):

    db_sync_folder = env.DB_SYNC_PATH_PY
    file_name = ""
    # testes usam "/api/"" para ter acesso ao json do SGTI, componentes reais usam "api/" para ter acesso ao cadti
    if endpoint.find("/api/") != -1:
        file_name = endpoint.replace("/api/", "") + "_mock.json"
    else:
        file_name = endpoint.replace("api/", "") + "_cadti_mock.json"
    
    db_sync_folder = env.DB_SYNC_PATH_PY
    
    with open(
        file=f"{db_sync_folder}\\app\\tests\\fixtures\\{file_name}",
        mode="r",
        encoding="utf-8",
    ) as json_file:
        data = json.load(json_file)
        return data


def mock_post(*args, **kwargs):
    return "Dados inseridos"


@pytest.fixture(autouse=True)
def override_api(monkeypatch):
    monkeypatch.setattr(api, "get", mock_get)
    monkeypatch.setattr(api, "post", mock_post)


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")
