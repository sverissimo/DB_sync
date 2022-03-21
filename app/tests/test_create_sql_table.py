from services.create_sql_table import create_sql_table
from controller import api


def mock_api_post(*args, **kwargs):
    return "createTable alright"


def test_valid_sql_file(monkeypatch):

    monkeypatch.setattr(api, "post", mock_api_post)
    sql_script = create_sql_table("veiculos.sql")

    search_index = sql_script["query"].find("CREATE TABLE")

    assert isinstance(search_index, int) == True
    assert search_index > 0
