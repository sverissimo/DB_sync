from datetime import datetime


def compare_dates(data_emissao, data_vencimento):

    # sf = '%d/%m/%Y'
    # New dateFormat from new version of SGTI:
    sf = '%Y-%m-%d'
    emissao = datetime.strptime(data_emissao, sf).date()
    vencimento = datetime.strptime(data_vencimento, sf).date()
    current = datetime.now().date()

    if emissao > vencimento:
        return 'Inválido'
    if emissao > current:
        return 'Pendente'
    if vencimento < current:
        return 'Vencido'
    if vencimento >= current:
        return 'Vigente'


"""
from DB to python
f = '%Y-%m-%d %H:%M:%S.%f'
a = datetime.strptime('2020-09-01 13:09:41.4196', f)
"""
