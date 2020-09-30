import requests
from compare_dates import compare_dates


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
    ('Placa', 'placa')
]

steps = [7, 2, 29, 33]

empresas = requests.get('http://localhost:3001/api/empresas').json()
seguradoras = requests.get('http://localhost:3001/api/seguradoras').json()

filtered_insurances = []
apolices = []


def formatData(data):
    # Retorna uma lista de dicts no formato [{apolice: <nApolice>, placas:[<lista de placas>]}]
    print('formatData started')
    print(data[0])
    for d in data:
        d['seguradora'] = d['seguradora'].strip()
        d['seguradora'] = d['seguradora'].replace('S/A', 'S.A.')
        d['seguradora'] = d['seguradora'].replace('SA', 'S.A.')
        d['seguradora'] = d['seguradora'].replace('  ', ' ')

        for e in empresas:
            if d['delegatario'] == e['razao_social']:
                d['delegatario_id'] = e['delegatario_id']

        for s in seguradoras:
            if d['seguradora'] == s['seguradora']:
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
        if 'seguradora_id' not in i or 'delegatario_id' not in i:
            i['seguradora_id'] = 'NULL'
            print(i)

        vehicles = []
        for d in data:
            if i['apolice'] == d['apolice']:
                vehicles.append(d['placa'])

        apolices.append({'apolice': i['apolice'], 'placas': vehicles})
        vehicles = []
        del i['placa']

    data_to_return = {'apolices': apolices, 'seguros': filtered_insurances}

    return data_to_return
