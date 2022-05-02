from subprocess import Popen, PIPE
from basedata import (
    ENCRYPT_PATH,
    DECRYPT_PATH,
)


def encryption(value: str, keystore_path: str):
    stdin = Popen(
        f'{ENCRYPT_PATH} -path "{keystore_path}" -data "{value}"',
        shell=True, stdout=PIPE
    )
    ciphertext, error = stdin.communicate()
    return ciphertext.decode('utf-8')


def decryption(ciphertext: str, keystore_path: str):
    stdin = Popen(
        f'{DECRYPT_PATH} -path "{keystore_path}" -data "{ciphertext}"',
        shell=True, stdout=PIPE
    )
    plaintext, error = stdin.communicate()
    return plaintext.decode('utf-8')


if __name__ == '__main__':
    pass
