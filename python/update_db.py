import requests


def update_db(sgti_data):
    print(sgti_data[7])
    sgti_data = {'sgti_data': sgti_data}
    r = requests.post('http://localhost:3001/sync/updateTable', json=sgti_data)
    print(r)
