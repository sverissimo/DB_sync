import json
import os
import requests
from dotenv import load_dotenv
import send_mail

load_dotenv()

__AUTH = os.getenv("AUTH_SYNC")
HEADERS = {"authorization": __AUTH}
HOST = os.getenv("HOST")

proxies = {"http": None, "https": None} if os.getenv("ENV") == "development" else None


def get(endpoint: str):
    url = HOST + endpoint
    response = requests.get(url, headers=HEADERS, proxies=proxies, verify=False)
    response_type = response.headers.get("content-type")

    if "application/json" in response_type:
        return response.json()
    else:
        return response.text


def post(endpoint: str, data: json):
    url = HOST + endpoint

    try:
        response = requests.post(
            url, json=data, headers=HEADERS, proxies=proxies, verify=False
        )
        response_type = response.headers.get("content-type")

        if "application/json" in response_type:
            return response.json()
        else:
            return response.text

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        send_mail("Http Error")
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        send_mail("Error Connecting")
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        send_mail("Timeout Error")
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else happened...", err)
        send_mail("OOps: Something Else happened...")


def put(endpoint: str, data: json):
    url = HOST + endpoint
    response = requests.put(
        url, json=data, headers=HEADERS, proxies=proxies, verify=False
    )

    response_type = response.headers.get("content-type")

    if "application/json" in response_type:
        return response.json()
    else:
        return response.text
