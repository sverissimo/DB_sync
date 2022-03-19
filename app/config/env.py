from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ENV = getenv("ENV")
HOST = getenv("HOST")
USER = getenv("USER")
PASS = getenv("PASS")
AUTH_SYNC = getenv("AUTH_SYNC")
USER_FOLDER = getenv("USER_FOLDER")
DB_SYNC_PATH_PY = getenv("DB_SYNC_PATH_PY")
SGTI_FILE_FOLDER = getenv("SGTI_FILE_FOLDER")
