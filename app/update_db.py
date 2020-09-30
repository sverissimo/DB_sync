import requests


def update_seguros(apolices):
    # Prepara o objeto no formato do endpoint para atualização de seguros, com table, table PK etc e o sgti_data que vem do formatData de cada entidade
    updateDict = {
        'table': 'veiculo',
        'tablePK': 'veiculo_id',
        'column': 'apolice'
    }

    # print(updateDict)
    #i = 1
    for ap in apolices:
        updateDict['value'] = ap['apolice']
        updateDict['placas'] = ap['placas']
        if ap['apolice'] == '1002800079936':
            print(updateDict, ap)

        r = requests.put(
            'http://localhost:3001/api/updateInsurances', json=updateDict)
    #print(i, r.json())
    #i += 1


def update_db(sgti_data, table):
    request_data = {'table': table, 'sgti_data': sgti_data}

    if table == 'seguros':
        request_data = {'table': table, 'sgti_data': sgti_data['seguros']}
        apolices = sgti_data['apolices']
        update_seguros(apolices)

    if table == 'laudos':
        table = 'laudo'
        print(table)

    r = requests.post(
        'http://localhost:3001/sync/updateTable', json=request_data)
    print(r.text, table)
