from controller import api


def update_seguros(apolices):
    # Prepara o objeto no formato do endpoint para atualização de seguros, com table, table PK etc e o sgti_data que
    # vem do formatData de cada entidade
    updateDict = {"table": "veiculos", "tablePK": "veiculo_id", "column": "apolice"}

    for ap in apolices:
        updateDict["value"] = ap["apolice"]
        updateDict["placas"] = ap["placas"]
        if ap["apolice"] == "1002800079936":
            print(updateDict, ap)

        api.put("api/updateInsurances", updateDict)


def update_db(sgti_data, table):
    request_data = {"table": table, "sgti_data": sgti_data}

    if table == "seguros":
        request_data = {"table": table, "sgti_data": sgti_data["seguros"]}
        # Essas 2 linhas abaixo somente serão necessárias se o 'app.py seguros' for rodado, atualizando APENAS os
        # seguros. Senão n precisa pq a apolice do veiculo vem da mesma tabela.
        # apolices = sgti_data['apolices']
        # update_seguros(apolices)

    api.post("sync/updateTable", request_data)
    print(table)
