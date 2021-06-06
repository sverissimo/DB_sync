import os
import requests
from time import sleep
from create_missing_entry import create_missing_entry
from compare_dates import compare_dates


# Set headers
auth = os.getenv("AUTH_SYNC")
headers = {'authorization': auth}

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
    ('Código', 'codigo_empresa'),
    ('Placa', 'placa')
]

steps = [7, 2, 29, 33]

seguradoras = requests.get('http://localhost:3001/api/seguradoras', headers=headers).json()

filtered_insurances = []
apolices = []


def formatData(data):
    # Retorna uma lista de dicts no formato [{apolice: <nApolice>, placas:[<lista de placas>]}]
    print('formatData started -- seguros')

    # Se houver alguma seguradora nova, inserir no DB do CadTI antes p pegar o id depois
    data = create_missing_entry('seguradora', 'seguradora', seguradoras, data)
    updated_seguradoras = requests.get('http://localhost:3001/api/seguradoras', headers=headers).json()

    for d in data:
        seguradora = d['seguradora']
        for s in updated_seguradoras:
            if seguradora == s['seguradora']:
                d['seguradora_id'] = s['id']

        d['situacao'] = compare_dates(d['data_emissao'], d['vencimento'])
        del d['seguradora']
        del d['delegatario']
        count = 0
        if d not in filtered_insurances:
            for i in filtered_insurances:
                if i['apolice'] == d['apolice']:
                    count = 1
            if count == 0:
                filtered_insurances.append(d)
        count = 0

    for i in filtered_insurances:
        if 'seguradora_id' not in i:
            i['seguradora_id'] = 'NULL'
            # print(i)

        vehicles = []
        for d in data:
            if i['apolice'] == d['apolice']:
                vehicles.append(d['placa'])

        apolices.append({'apolice': i['apolice'], 'placas': vehicles})
        vehicles = []
        del i['placa']

    data_to_return = {'apolices': apolices, 'seguros': filtered_insurances}
    return data_to_return
