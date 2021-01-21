import re
import json
from format_cpf import format_cpf

file_names = {
    'xls_file': 'SociosDeDelegatarios.xls',
    'sql_file': 'socios.sql'
}

fields = [
    ('Nome sócio', 'nome_socio'),
    ('Cpf sócio', 'cpf_socio'),
    ('Código delegatário', 'codigo_empresa'),

]

steps = [7, 1, 11, 13]
# Termos considerados lixo na tabela do SGTI para apagar
del_key_words = ['ALTERAÇÃO', 'ALT\\.', 'JUCEMG', 'JUCESP', 'LICITAR', 'DESARQUIVAMENTO',
                 '\\(JU', 'DESATIVADA', 'CONTRATO', 'CADASTRO']


def formatData(data):
    i = 0
    seen = set()
    seen2 = []
    seen_add = seen.add
    # Loop para identificar os nomes repetidos (referência é o cpf) da tabela e apagar o lixo
    for d in data:
        if len(d['cpf_socio']) > 0:
            if d['cpf_socio'] in seen and d not in seen2:
                seen2.append(d)
            else:
                seen_add(d['cpf_socio'])
            d['cpf_socio'] = format_cpf(d['cpf_socio'])
        # Apaga lixo nos dados do SGTI
        for w in del_key_words:
            if re.search(w, d['nome_socio']):
                i = i + 1
                # print(i, d['nome_socio'])
                if d in data:
                    data.remove(d)

    # Loop para remover os nomes lixo da tabela
    i = 0
    for d in data:
        for w in del_key_words:
            if re.search(w, d['nome_socio']):
                i = i + 1
                print(i, d['nome_socio'])
                if d in data:
                    data.remove(d)
    print(len(data))

    # Acrescenta todas as empresas - pode pegar pega várias linhas do SGTI de 1 cpf -, salva na varriável empresas
    # no formato [{"codigoEmpresa": 1, "share":2}] e depois salva o d['empresas'] = empresas
    for s in seen2:
        empresas = []
        i = 0
        for d in data:
            if d['cpf_socio'] == s['cpf_socio']:
                i += 1
                empresas.append({"codigoEmpresa": int(d['codigo_empresa'])})
                d['empresas'] = empresas

    # Formata a list empresas em json string para inserir no postgresql
    output, temp = [], []
    for d in data:
        if 'empresas' in d:
            d['empresas'] = json.dumps(d['empresas'])
        else:
            empresas = [{"codigoEmpresa": int(d['codigo_empresa'])}]
            empresas = json.dumps(empresas)
            d['empresas'] = empresas
        # Insere também os nomes sem cpf da tabela SGTI
        if (d['cpf_socio'] == '' and d['nome_socio'] not in temp) or d['cpf_socio'] not in temp:
            temp.append(d['cpf_socio'])
            temp.append(d['nome_socio'])
            output.append(d)

    output.sort(key=lambda el: el['nome_socio'])
    return output
