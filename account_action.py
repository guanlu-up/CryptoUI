from typing import Union, List, Dict
import os
import json

import versatile
import basedata


class AccountAction(object):
    """对存储账户信息的JSON文件进行封装一些通用方法;
    使用JSON文件用作存储账户信息的数据库"""

    def __init__(self, public_keystore, jsonpath: Union[str, None] = None):
        """ 初始化需要操作的文件路径,需要从参数中传入;
        :param public_keystore: 存储公钥的keystore文件路径
        :param jsonpath: 存储账户信息的JSON文件路径
        """
        self.public_keystore = public_keystore
        self.jsonpath = jsonpath or basedata.JSON_SAVE_PATH

    def expand_account(self, accounts: List[Dict]):
        """增加账户信息到JSON文件中; 当不确定JSON文件是否存在时使用此方法"""
        if not os.path.exists(self.jsonpath):
            return self._write_jsonpath(accounts)
        self.update_account(accounts)

    def modify_account(self, account_no: str, modify_key: str, value: str):
        """ 修改账户信息
        :param modify_key: 要修改的key -> ["登录密码", "U盾密码", "客户号", "操作员号"]
        :param account_no: 账号
        :param value: 新值
        """
        accounts = self.query_account_all()
        for account in accounts:
            if account["银行账户"] != account_no:
                continue
            if modify_key in ["登录密码", "U盾密码"]:
                value = versatile.encryption(value, self.public_keystore)
            account[modify_key] = value
            break
        with open(self.jsonpath, "w", encoding="utf-8") as fileIO:
            json.dump(accounts, fileIO)

    def query_account_all(self):
        """查询所有账户信息"""
        if not os.path.exists(self.jsonpath):
            return list(dict())
        with open(self.jsonpath, "r", encoding="utf-8") as fileIO:
            content: List[Dict] = json.load(fileIO)
        return content

    def query_account_number_all(self):
        """返回JSON文件中所有的账号"""
        accounts = self.query_account_all()
        return [account["银行账户"] for account in accounts]

    def condition_query(self, query_range, query_key, match_mode, match_value):
        """ 按照指定条件查询账户
        :param query_range: 查询范围 -> ["查询单个", "查询全部"]
        :param query_key: 查询的key -> ["银行名称", "银行账户", "账户名称", "全部"]
        :param match_mode: 匹配模式 -> ["模糊匹配", "完整匹配"]
        :param match_value: 匹配目标的值
        :return: List[Dict]
        """
        accounts = self.query_account_all()
        if query_key == "全部":
            return accounts
        filter_ = list()
        for account in accounts:
            if match_mode == "模糊匹配":
                if match_value in account[query_key]:
                    filter_.append(account)
            elif match_mode == "完整匹配":
                if match_value == account[query_key]:
                    filter_.append(account)
        if query_range == "查询单个" and filter_:
            return [filter_[0]]
        return filter_

    def update_account(self, accounts: List[Dict]):
        """对传入的账户进行加密后更新到JSON文件中; 当确认存在JSON文件时使用此方法"""
        history_accounts = self.query_account_all()
        encrypted = self._encryption(accounts)
        history_account_no = [acc["银行账户"] for acc in history_accounts]
        # 找出相同的账户
        same_number = [account["银行账户"] for account in encrypted
                       if account["银行账户"] in history_account_no]
        # 从历史账户中移除相同的账户
        account_filtered = self._drop_specified_account(history_accounts, same_number)
        account_filtered.extend(encrypted)
        # 重新写入到JSON文件
        with open(self.jsonpath, "w", encoding="utf-8") as fileIO:
            json.dump(account_filtered, fileIO)

    def remove_account(self, account_no: str):
        """根据账号移除JSON文件中的账户"""
        accounts = self.query_account_all()
        for account in accounts:
            if account["银行账户"] == account_no:
                accounts.remove(account)
                break
        # 重新写入到JSON文件
        with open(self.jsonpath, "w", encoding="utf-8") as fileIO:
            json.dump(accounts, fileIO)

    def verification_account(self, account_no: str, login_pwd: str, key_pwd: str):
        """验证账户的登录密码和U盾密码是否和JSON文件里一致"""
        accounts = self.query_account_all()
        for account in accounts:
            if account["银行账户"] != account_no:
                continue
            login_ciphertext = versatile.encryption(login_pwd, self.public_keystore)
            key_ciphertext = versatile.encryption(key_pwd, self.public_keystore)
            return all((login_ciphertext == account["登录密码"],
                        key_ciphertext == account["U盾密码"]))
        return False

    def _write_jsonpath(self, accounts: List[Dict]):
        """将所有账户信息加密后输出到JSON文件"""
        encrypted = self._encryption(accounts)
        with open(self.jsonpath, "w", encoding="utf-8") as fileIO:
            json.dump(encrypted, fileIO)

    def _encryption(self, accounts):
        for account in accounts:
            for key in ["登录密码", "U盾密码"]:
                account[key] = versatile.encryption(
                    account[key], self.public_keystore
                )
        return accounts

    @staticmethod
    def _drop_specified_account(accounts, same_number):
        for number in same_number:
            for account in accounts:
                if account["银行账户"] == number:
                    accounts.remove(account)
        return accounts
