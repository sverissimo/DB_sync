import re
from field_conversor import field_conversor
from format_cnpj import format_cnpj


def parse_data(collection, fields, formatData):

    parsed_data_SGTI = []
    newObj = {}

    for obj in collection:
        if (obj['Situação'] != 'Inativo'):
            for f in obj:

                if(f == 'Cpf/Cnpj'):
                    obj[f] = format_cnpj(obj[f])
                new_f = field_conversor(f, fields)

                if(new_f is None or new_f == ''):
                    continue

                if(re.search('\'', obj[f])):
                    obj[f] = obj[f].replace('\'', '\'\'')

                if(re.search('  ', obj[f])):
                    obj[f] = obj[f].replace('  ', ' ')

                newObj = {**newObj, new_f: obj[f]}
            parsed_data_SGTI.append(newObj)
            newObj = {}
    formatData(parsed_data_SGTI)
    return parsed_data_SGTI
