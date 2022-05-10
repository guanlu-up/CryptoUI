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


def fill_space(text, length=0):
    """在文本的右侧填充空格;
    在UI界面中,ASCII码占2个空格, 中文占4个空格;"""
    # '\u4e01' - '\u9fd5' 表示中文文字范围; '\uff01' - '\uff20'表示中文标点符号范围
    cn_len = sum(1 for t in text if '\u4e01' <= t <= '\u9fd5' or '\uff01' <= t <= '\uff20')
    ascii_len = sum(1 for t in text if t.isascii())
    reduce = (cn_len * 4) + (ascii_len * 2)
    real_length = length - reduce
    if real_length < 0:
        return text
    return "{}{}".format(text, " " * real_length)
