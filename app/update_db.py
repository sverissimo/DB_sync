import requests


def update_db(sgti_data, table):
    # print(sgti_data[7])
    request_data = {'table': table, 'sgti_data': sgti_data}
    r = requests.post(
        'http://localhost:3001/sync/updateTable', json=request_data)
    print(r)
