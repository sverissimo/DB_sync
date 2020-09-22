import requests

file_names = {
    'xls_file': 'ConsultaVeiculos.xls',
    'sql_file': 'laudos.sql'
}

fields = [
    ('Placa', 'placa'),
    ('Delegatário', 'delegatario'),
    ('Empresa Laudo', 'empresa_laudo'),
    ('Número Laudo', 'numero_laudo'),
    ('Validade Laudo', 'validade'),
]


steps = [7, 2, 29, 33]

empresas = requests.get('http://localhost:3001/api/empresas').json()
veiculos = requests.get('http://localhost:3001/api/veiculos').json()


# def formatData(data):
