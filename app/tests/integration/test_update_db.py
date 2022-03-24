from tests.unit.test_veiculo_parse_data import test_parse_veiculos_value
from tests.unit.test_seguro_parse_data import test_parse_seguros_value
from tests.unit.test_laudo_parse_data import test_parse_laudos_value


def test_veiculo_update_db():
    veiculo_data = test_parse_veiculos_value()
    assert {"placa", "modelo_chassi"} <= veiculo_data[0].keys()
    assert "Renavam" not in veiculo_data[0]


def test_seguro_update_db():
    seguro_data = test_parse_seguros_value()
    assert "apolice" in seguro_data[0]
    assert "data_emissao" in seguro_data[0]
    assert "codigo_empresa" in seguro_data[0]
    assert "vencimento" in seguro_data[0]

    assert "Apólice" not in seguro_data[0]
    assert "placa" not in seguro_data[0]


def test_laudo_update():
    laudo_data = test_parse_laudos_value()
    assert {"validade", "veiculo_id", "empresa_id"} <= laudo_data[0].keys()
