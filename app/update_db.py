import requests

production_url = 'http://200.198.42.167/sync/updateTable'
local = 'http://localhost:3001/sync/updateTable'


def update_seguros(apolices, host, headers):
    # Prepara o objeto no formato do endpoint para atualização de seguros, com table, table PK etc e o sgti_data que
    # vem do formatData de cada entidade
    updateDict = {
        'table': 'veiculos',
        'tablePK': 'veiculo_id',
        'column': 'apolice'
    }

    # print(updateDict)
    # i = 1
    for ap in apolices:
        updateDict['value'] = ap['apolice']
        updateDict['placas'] = ap['placas']
        if ap['apolice'] == '1002800079936':
            print(updateDict, ap)

        requests.put(
            host+'/api/updateInsurances', json=updateDict, headers=headers)
    # print(i, r.json())
    # i += 1


def update_db(sgti_data, table, host, headers):
    request_data = {'table': table, 'sgti_data': sgti_data}

    if table == 'seguros':
        request_data = {'table': table, 'sgti_data': sgti_data['seguros']}
        # Essas 2 linhas abaixo somente serão necessárias se o 'app.py seguros' for rodado, atualizando APENAS os
        # seguros. Senão n precisa pq a apolice do veiculo vem da mesma tabela.
        # apolices = sgti_data['apolices']
        # update_seguros(apolices, host, headers)

    r = requests.post(host+'/sync/updateTable', json=request_data, headers=headers)
    print(r.text, table)
    new_backup = requests.get(host+'/sync/createRestorePoint', headers=headers)
    print(new_backup.text)
