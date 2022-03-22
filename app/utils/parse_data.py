import re
from utils.field_conversor import field_conversor

# Essa função faz um parsing básico e distribui para cada entidade fazer filtros específicos, depois retorna o resultado final para o update_DB


def parse_data(collection, model):

    parsed_data_SGTI = []
    newObj = {}
    name = model["name"]
    fields = model["fields"]
    formatData = model["formatData"]

    for obj in collection:
        #    if (obj['Situação'] != 'Inativo'):
        for f in obj:
            new_f = f
            if name != "old_vehicles":
                new_f = field_conversor(f, fields)

            if new_f is None or new_f == "":
                continue

            if re.search("'", obj[f]):
                obj[f] = obj[f].replace("'", "''")

            if re.search("  ", obj[f]):
                obj[f] = obj[f].replace("  ", " ")

            if type(obj[f]) == str:
                obj[f] = obj[f].strip()

            newObj = {**newObj, new_f: obj[f]}
        parsed_data_SGTI.append(newObj)
        newObj = {}
    final_data = formatData(parsed_data_SGTI)

    return final_data
