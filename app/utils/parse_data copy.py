from utils.field_conversor import field_conversor

# Essa função faz um parsing básico e distribui para cada entidade fazer filtros específicos, depois retorna o resultado final para o update_DB
def parse_data(collection, model):

    parsed_data_SGTI = []
    newObj = {}
    name = model["name"]
    fields = model["fields"]
    formatData = model["formatData"]

    for obj in collection:
        for field in obj:
            if field is None or field == "":
                continue

            new_field = field
            if name != "old_vehicles":
                new_field = field_conversor(field, fields)

            if type(obj[field]) == str:
                obj[field] = obj[field].replace("'", "''")
                stripped_string = obj[field].strip()
                new_value = " ".join(stripped_string.split())

            newObj = {**newObj, new_field: new_value}
        parsed_data_SGTI.append(newObj)
        newObj = {}
    final_data = formatData(parsed_data_SGTI)

    return final_data
