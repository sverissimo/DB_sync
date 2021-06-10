from format_cnpj import format_cnpj

file_names = {
    'xls_file': 'Delegatarios.xls',
    'sql_file': 'empresas.sql'
}

fields = [
    ('Código', 'codigo_empresa'),
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

steps = [4, 3, 1, 9, 11]


def formatData(data):
    for d in data:
        d['cnpj'] = format_cnpj(d['cnpj'])

        d['razao_social'] = (
            d['razao_social']
            .replace('LOPES E CIA LTDA.', 'LOPES & CIA LTDA')
            .replace('(Desativada)', '')
                             )
        d['situacao'] = d['situacao'].replace('Inativo', 'Desativada')

    print(len(data))
    return data
