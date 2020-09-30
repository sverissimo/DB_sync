from format_cnpj import format_cnpj

file_names = {
    'xls_file': 'Delegatarios.xls',
    'sql_file': 'empresas.sql'
}

fields = [
    ('Código', 'old_id'),
    ('Razão Social', 'razao_social'),
    ('Situação', 'situacao'),
    ('Data Vencimento', 'vencimento_contrato'),
    ('Cpf/Cnpj', 'cnpj'),
    ('Insc. Estadual', 'inscricao_estadual'),
    ('Endereço', 'rua'),
    ('Município', 'cidade'),
    ('UF', 'uf'),
    ('Telefone', 'telefone'),
    ('Email', 'email'),
    ('Número', 'numero'),
    ('Bairro', 'bairro'),
    ('CEP', 'cep'),
]

steps = [7, 0, 13, 15]


def formatData(data):
    for d in data:
        d['cnpj'] = format_cnpj(d['cnpj'])

        d['razao_social'] = d['razao_social'].replace(
            'LOPES E CIA LTDA.', 'LOPES & CIA LTDA')
    print(len(data))
    return data
