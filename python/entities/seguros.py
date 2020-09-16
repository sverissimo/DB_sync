file_names = {
    'xls_file': 'Seguros.xls',
    'sql_file': 'seguros.sql'
}

fields = [
    ('Apólice', 'apolice'),
    ('Seguradora', 'seguradora_id'),
    ('Data Início', 'data_emissao'),
    ('Data fim', 'vencimento'),
    ('Delegatário', 'delegatario'),

    """ situacao text COLLATE pg_catalog."default", """
]
