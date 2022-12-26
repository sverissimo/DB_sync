from time import sleep
from controller import api
from services.create_missing_entry import create_missing_entry
from utils.compare_dates import compare_dates

file_names = {"xls_file": "ConsultaVeiculos.xls", "sql_file": "seguros.sql"}

fields = [
    ("Apólice", "apolice"),
    ("Seguradora", "seguradora"),
    ("Data Inicio", "data_emissao"),
    ("Data Fim", "vencimento"),
    ("Delegatário", "delegatario"),
    ("Código", "codigo_empresa"),
]

# oldsteps = [7, 2, 29, 33]
steps = [4, 3, 3, 25, 29]
filtered_insurances: list = []


def get_seguradoras():
    return api.get("api/seguradoras")


def formatData(data):

    print(" formatData started -- seguros")

    # Se houver alguma seguradora nova, inserir no DB do CadTI antes p pegar o id depois
    seguradoras = get_seguradoras()
    data = create_missing_entry("seguradoras", "seguradora", seguradoras, data)
    updated_seguradoras = get_seguradoras()

    for d in data:
        seguradora = d["seguradora"]
        for s in updated_seguradoras:
            if seguradora == s["seguradora"]:
                d["seguradora_id"] = s["id"]

        d["situacao"] = compare_dates(d["data_emissao"], d["vencimento"])
        del d["seguradora"]
        del d["delegatario"]
        count = 0
        if d not in filtered_insurances:
            for i in filtered_insurances:
                if i["apolice"] == d["apolice"]:
                    count = 1
            if count == 0:
                filtered_insurances.append(d)
        count = 0

    for i in filtered_insurances:
        if "seguradora_id" not in i:
            i["seguradora_id"] = "NULL"

    return filtered_insurances
