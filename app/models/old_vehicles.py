file_names = {"xls_file": "OldVehicles.xls", "sql_file": "veiculos.sql"}

# Os demais fields ficam com a formatação da planilha, armazenados no MongoDB
fields = [
    ("Indc. Idade", "Indicador de Idade"),
    ("Dist. Minima", "Distância Mínima"),
    ("Dist. Máxima", "Distância Máxima"),
]

steps = [7, 2]


def formatData(data):
    indexes = []
    print(len(data))
    for i, d in enumerate(data):
        if d["Situação"] != "Baixado":
            indexes.append(i)
        for a, b in fields:
            d[b] = d[a]
            del d[a]

    filtered_data = [d for i, d in enumerate(data) if i not in indexes]

    print(f"{len(filtered_data)} shut down, {len(indexes)} vehicles still active.")
    print("Old vehicles data parsed.")
    return filtered_data
