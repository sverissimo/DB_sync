import re
from field_conversor import field_conversor
from format_cnpj import format_cnpj


def parse_data(collection, fields, formatData):

    parsed_data_SGTI = []
    newObj = {}

    for obj in collection:
        if (obj['Situação'] != 'Inativo'):
            for f in obj:

                if f == 'Cpf/Cnpj':
                    obj[f] = format_cnpj(obj[f])
                new_f = field_conversor(f, fields)

                if new_f is None or new_f == '':
                    continue

                if re.search('\'', obj[f]):
                    obj[f] = obj[f].replace('\'', '\'\'')

                if re.search('  ', obj[f]):
                    obj[f] = obj[f].replace('  ', ' ')

                if type(obj[f]) == str:
                    obj[f] = obj[f].strip()

                newObj = {**newObj, new_f: obj[f]}
            parsed_data_SGTI.append(newObj)
            newObj = {}
    final_data = formatData(parsed_data_SGTI)
    """ for x in final_data:
        print(x, '/n') """
    i = 1
    for k in final_data[-1]:
        print(i, k, final_data[-1][k])
        i += 1
    return final_data
