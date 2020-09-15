empresas = [
    ('Código', 'old_id'),
    ('Razão Social', 'razao_social'),
    ('Situação', 'situacao'),
    ('Data Vencimento', 'vencimento_contrato'),
    ('Cpf/Cnpj', 'cnpj'),
    ('Insc. Estadual', ''),
    ('Endereço', 'rua'),
    ('Município', 'cidade'),
    ('UF', 'uf'),
    ('Telefone', 'telefone'),
    ('Email', 'email'),
    ('Número', 'numero'),
    ('Bairro', 'bairro'),
    ('CEP', 'cep'),
]

def field_conversor(f):
    for i, j in empresas:        
        if(f == i):
            return j