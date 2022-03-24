from typing import List
from controller import api
from utils.sanitize import sanitize_value


def create_missing_entry(table, column, raw_collection, data):
    insert_obj = {"table": table}
    collection: List[str] = list(map(lambda el: el[column], raw_collection))

    for d in data:
        if column in d:
            d[column] = sanitize_value(d[column])
            value = d[column]
        elif table == "empresa_laudo":
            value = d["empresa_laudo"]
        if value and value not in collection:
            collection.append(value)
            insert_obj["requestElement"] = {column: value}
            print(f" Found new value in SGTI, posted to table {table}: {value}")
            # print(insert_obj)
            api.post("api/addElement", insert_obj)
    return data
