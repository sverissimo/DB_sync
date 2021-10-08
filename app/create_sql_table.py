import requests
from pathlib import Path
from send_mail import send_mail


def create_sql_table(user_folder, sql_file, host, headers):
    path_to_file = f'../SQL_scripts/{sql_file}'
    create_empresas_table = open(path_to_file, 'r')
    empresas_query = create_empresas_table.read()

    query = {'query': empresas_query}
    print(query)
    try:
        r = requests.post(host + '/sync/createTable', query, headers=headers)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        send_mail(host, headers, "Http Error")
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        send_mail(host, headers, "Error Connecting")
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        send_mail(host, headers, "Timeout Error")
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else happened...", err)
        send_mail(host, headers, "OOps: Something Else happened...")

    print(r.text, sql_file)
