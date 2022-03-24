from controller import api
from utils.format_placa import format_placa
from services.create_missing_entry import create_missing_entry

file_names = {"xls_file": "ConsultaVeiculos.xls", "sql_file": "laudos.sql"}

fields = [
    ("Número Laudo", "id"),
    ("Placa", "placa"),
    ("RENAVAM", "renavam"),
    ("Código", "codigo_empresa"),
    ("Empresa Laudo", "empresa_laudo"),
    ("Validade Laudo", "validade"),
]

# oldsteps = [7, 2, 29, 33]
steps = [4, 3, 3, 25, 29]


def formatData(data):
    veiculos = api.get("api/veiculos")
    empresas_laudo = api.get("api/empresasLaudo")

    # Retorna uma lista de dicts no formato [{apolice: <nApolice>, placas:[<lista de placas>]}]
    print(" formatData started -- laudos")

    # Se houver alguma seguradora nova, inserir no DB do CadTI antes p pegar o id depois
    data = create_missing_entry("empresa_laudo", "empresa", empresas_laudo, data)
    updated_empresas_laudo = api.get("api/empresasLaudo")

    laudos = []
    for d in data:
        if d["placa"][3] != "-":
            d["placa"] = format_placa(d["placa"])
        for v in veiculos:
            if d["placa"] == v["placa"] or d["renavam"] == v["renavam"]:
                d["veiculo_id"] = v["veiculo_id"]
        for e in updated_empresas_laudo:
            if d["empresa_laudo"] == e["empresa"]:
                d["empresa_id"] = e["id"]
        del d["placa"]
        del d["empresa_laudo"]
        del d["renavam"]
        if d["id"] and d not in laudos:
            laudos.append(d)

    filtered_laudos = list(filter(lambda laudo: "veiculo_id" in laudo, laudos))

    print(" laudos data parsed.")
    return filtered_laudos
