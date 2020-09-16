import requests

file_names = {
    'xls_file': 'ConsultaVeiculos.xls',
    'sql_file': 'seguros.sql'
}

fields = [
    ('Apólice', 'apolice'),
    ('Seguradora', 'seguradora'),
    ('Data Inicio', 'data_emissao'),
    ('Data Fim', 'vencimento'),
    ('Delegatário', 'delegatario'),
]

steps = [7, 2, 29, 33]


def formatData(data):
    print(data)
