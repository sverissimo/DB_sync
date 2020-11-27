import requests

def update_mongo_db(host, request_data):
    r = requests.post(host+'/sync/oldVehicles', json=request_data)
    print(r.text)
