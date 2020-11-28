import re

file_names = {
    'xls_file': 'ConsultaVeiculos.xls',
    'sql_file': 'veiculos.sql'
}

fields = [
    ('Indc. Idade', 'Indicador de Idade'),
    ('Dist. Minima', 'Distância Mínima'),
    ('Dist. Máxima', 'Distância Máxima')
]

steps = [7, 2]


def formatData(data):
    indexes = []
    print(len(data))
    for i, d in enumerate(data):
        if d['Situação'] != 'Baixado':
            indexes.append(i)
        for a, b in fields:
            d[b] = d[a]
            del d[a]

    filtered_data = [d for i, d in enumerate(data) if i not in indexes]

    print(len(filtered_data), len(indexes))
    print('veiculos data parsed.')
    return filtered_data
