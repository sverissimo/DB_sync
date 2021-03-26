import requests
import os
from format_placa import format_placa


# Set headers
auth = os.getenv("AUTH_SYNC")
headers = {'authorization': auth}

file_names = {
    'xls_file': 'ConsultaVeiculos.xls',
    'sql_file': 'laudos.sql'
}

fields = [
    ('Número Laudo', 'id'),
    ('Placa', 'placa'),
    ('Código', 'codigo_empresa'),
    ('Empresa Laudo', 'empresa_laudo'),
    ('Validade Laudo', 'validade'),
]

steps = [7, 2, 29, 33]
veiculos = requests.get('http://localhost:3001/api/veiculos', headers=headers).json()
empresas_laudo = requests.get(
    'http://localhost:3001/api/empresasLaudo', headers=headers).json()


def formatData(data):

    laudos = []
    for d in data:
        if d['placa'][3] != '-':
            d['placa'] = format_placa(d['placa'])
        for v in veiculos:
            if d['placa'] == v['placa']:
                d['veiculo_id'] = v['veiculo_id']
        for e in empresas_laudo:
            if d['empresa_laudo'] == e['empresa']:
                d['empresa_id'] = e['id']
        del d['placa']
        del d['empresa_laudo']
        if d['id'] and d not in laudos:
            laudos.append(d)
            if d['id'] == '000008654-19':
                print(d)
    print('laudos data parsed.')
    return laudos
