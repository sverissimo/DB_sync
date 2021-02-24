import requests

def update_mongo_db(host, headers, request_data):
    r = requests.post(host+'/sync/oldVehicles', json=request_data, headers=headers)
    print(r.text)
