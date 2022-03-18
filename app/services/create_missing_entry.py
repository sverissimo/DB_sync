from typing import List, Any
import os
from controller import api

# Set headers
auth = os.getenv("AUTH_SYNC")
headers = {"authorization": auth}


def sanitize(value):
    # Sanitize dos strings de nome de seguradora padronizando/trim e evitando caracteres especiais
    value = value.strip()
    value = value.replace("S/A", "S.A.")
    value = value.replace("SA", "S.A.")
    value = value.replace("  ", " ")
    return value


def create_missing_entry(table: str, column: str, raw_collection: Any, data: List[Any]):
    insert_obj = {"table": table}
    collection: List[str] = list(map(lambda el: el[column], raw_collection))

    for d in data:
        if column in d:
            d[column] = sanitize(d[column])
            value = d[column]
        elif table == "empresa_laudo":
            value = d["empresa_laudo"]
        if value and value not in collection:
            collection.append(value)
            insert_obj["requestElement"] = {column: value}
            print(value)
            print(insert_obj)
            api.post("api/addElement", insert_obj)
    return data
