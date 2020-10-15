def format_cpf(cpf):
    cpf = cpf[:3] + '.' + cpf[3:]
    cpf = cpf[:7] + '.' + cpf[7:]
    cpf = cpf[:11] + '-' + cpf[11:]
    return cpf
