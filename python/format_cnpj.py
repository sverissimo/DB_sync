def format_cnpj(cnpj):
    if ('Cnpj:' in cnpj):
        cnpj = cnpj[:8] + '.' + cnpj[8:]
        cnpj = cnpj[:12] + '.' + cnpj[12:]
        cnpj = cnpj[:16] + '/' + cnpj[16:]
        cnpj = cnpj[:21] + '-' + cnpj[21:]
    cnpj = cnpj.replace('Cnpj: ', '').replace('Cpf: ', '')
    return cnpj