import os
import json

DEFAULT_DIR = os.path.expanduser('~')
ROOT_DIR = os.path.dirname(__file__)
JSON_SAVE_PATH = os.path.join(ROOT_DIR, ".accounts.json")
CONFIG_PATH = os.path.join(ROOT_DIR, "config.json")
ENCRYPT_PATH = os.path.join(ROOT_DIR, 'bin', 'GoEncryption.exe')
DECRYPT_PATH = os.path.join(ROOT_DIR, 'bin', 'GoDecryption.exe')
PRIVATE_KEYSTORE = os.path.join(ROOT_DIR, 'bin', 'private_keystore.jks')
PUBLIC_KEYSTORE = os.path.join(ROOT_DIR, 'bin', 'public_keystore.jks')

with open(CONFIG_PATH, 'r', encoding='utf-8') as file_io:
    config = json.load(file_io)

COLUMN2INDEX = config.get("column2index")
