import re
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

steps = [7, 1, 4, 2]

del_key_words = ['ALTERAÇÃO', 'ALT\\.', 'JUCEMG', 'JUCESP', 'LICITAR', 'DESARQUIVAMENTO',
                 '\\(JU', 'DESATIVADA', 'CONTRATO', 'CADASTRO']


def formatData(data):
    i = 0
    for d in data:
        if len(d['cpf_socio']) > 0:
            d['cpf_socio'] = format_cpf(d['cpf_socio'])

        for w in del_key_words:
            if re.search(w, d['nome_socio']):
                i = i + 1
                print(i, d['nome_socio'])
                if d in data:
                    data.remove(d)
    i = 0
    for d in data:
        for w in del_key_words:
            if re.search(w, d['nome_socio']):
                i = i + 1
                print(i, d['nome_socio'])
                if d in data:
                    data.remove(d)

    print(len(data))
    return data
