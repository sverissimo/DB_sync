import re
from utils.field_conversor import field_conversor
from utils.sanitize import sanitize_value


def parse_data(collection, model):
    # Essa função faz um parsing básico e distribui para cada entidade fazer filtros específicos, depois retorna o resultado final para o update_DB

    parsed_data_SGTI = []
    newObj = {}
    name = model["name"]
    fields = model["fields"]
    formatData = model["formatData"]

    for obj in collection:

        for f in obj:
            new_f = f
            if name != "old_vehicles":
                new_f = field_conversor(f, fields)

            if new_f is None or new_f == "":
                continue

            obj[f] = sanitize_value(obj[f])

            newObj = {**newObj, new_f: obj[f]}
        parsed_data_SGTI.append(newObj)
        newObj = {}
    final_data = formatData(parsed_data_SGTI)

    return final_data
