import os
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, Qt
from PySide2.QtWidgets import (
    QApplication,
    QFileDialog,
    QMessageBox,
    QTableWidgetItem,
    QComboBox
)
from account_action import AccountAction
import basedata


def read_ui_file(uipath):
    qfile = QFile(uipath)
    qfile.open(QFile.ReadOnly)
    qfile.close()
    return qfile


class CryptoClient(object):
    """ 账户加密客户端工具;"""

    def __init__(self, uipath: str):
        """ UI界面使用Designer构建;
        UI界面中具体Widgets组件对象名称参考 widgets.md

        :param uipath: ui文件路径
        """
        self.ui = QUiLoader().load(read_ui_file(uipath))
        self.initialization()
        self._crypto_value = {}
        self.public_keystore = None

    def initialization(self):
        """初始化界面 Widgets"""
        self._init_push_button()
        self._init_line_text()
        self._init_radio_button()
        self._init_combo_box()
        self._init_table_widget()
        self._init_check_box()

    def show(self):
        """展示UI界面"""
        self.ui.show()

    def _init_push_button(self):
        """初始化 PushButton控件"""
        self.ui.cryptoTabBrowseButton.clicked.connect(
            self._select_public_key_file)
        self.ui.cryptoTabAddRow.clicked.connect(
            self._table_widget_add_row)
        self.ui.cryptoTabRemoveRow.clicked.connect(
            self._table_widget_reduce_row)
        self.ui.cryptoTabClearRow.clicked.connect(
            self._table_widget_clear_rows)
        self.ui.cryptoTabEncryptButton.clicked.connect(
            self._submit_crypto)
        self.ui.modifyTabClearNewValue.clicked.connect(
            self.ui.modifyTabNewValue.clear)
        self.ui.modifyTabSubmitButton.clicked.connect(
            self._submit_modify_button)
        self.ui.modifyTabQueryAccounts.clicked.connect(
            self.display_account_number
        )

    def _init_table_widget(self):
        """初始化; TableWidget控件"""
        self.ui.cryptoTabAccountTable.cellChanged.connect(
            self._encrypt_cells_password)

    def _init_line_text(self):
        """初始化 LineText控件"""

    def _init_radio_button(self):
        """初始化 RadioButton控件"""

    def _init_combo_box(self):
        """初始化 ComboBox控件"""
        # self.ui.modifyTabTypeComboBox.currentIndexChanged.connect()

    def _init_check_box(self):
        """初始化 CheckBox控件"""
        self.ui.modifyTabConfirmProtocol.stateChanged.connect(
            self._modify_tab_change_submit_state)

    def _submit_modify_button(self):
        """modifyTab; 提交修改Button"""
        self.public_keystore = self.ui.cryptoTabFileEdit.text()
        if not os.path.exists(self.public_keystore):
            return QMessageBox.warning(
                self.ui, "警告", "您还未选择公钥文件,或选择的文件无效!")
        modify_type = self.ui.modifyTabTypeComboBox.currentText()
        account_no = self.ui.modifyTabTargetAccount.text()
        new_value = self.ui.modifyTabNewValue.text()
        login_password = self.ui.modifyTabLoginPassword.text()
        key_password = self.ui.modifyTabUKeyPassword.text()
        action = AccountAction(self.public_keystore)
        if not action.verification_account(account_no, login_password, key_password):
            return QMessageBox.warning(
                self.ui, "警告", "当前输入的账户或密码无效,请检查!")
        action.modify_account(account_no, modify_type, new_value)
        self.ui.modifyTabNewValue.clear()
        self.ui.modifyTabLoginPassword.clear()
        self.ui.modifyTabUKeyPassword.clear()
        QMessageBox.about(
            self.ui, "提示", "修改成功!")

    def display_account_number(self):
        """在小窗口中展示当前JSON文件中所有的账号"""
        action = AccountAction(self.public_keystore)
        accounts_no = action.query_account_number_all()
        sub_window.set_window_title("银行账户")
        sub_window.set_content("\n".join(accounts_no))
        sub_window.show()

    def _modify_tab_change_submit_state(self):
        if self.ui.modifyTabConfirmProtocol.isChecked():
            self.ui.modifyTabSubmitButton.setEnabled(True)
        else:
            self.ui.modifyTabSubmitButton.setEnabled(False)

    def _select_public_key_file(self):
        """选择公钥文件"""
        filepath, _ = QFileDialog.getOpenFileName(self.ui, "选择公钥文件", basedata.DEFAULT_DIR)
        if not os.path.exists(filepath):
            return None
        self.ui.cryptoTabFileEdit.setText(filepath)

    def _table_widget_add_row(self):
        """TableWidget增加新行"""
        current_rows = self.ui.cryptoTabAccountTable.rowCount()
        self.ui.cryptoTabAccountTable.insertRow(current_rows)
        # 在新添加的行中循环将每个列的item设置为居中显示并填入空字符串
        for column in basedata.COLUMN2INDEX.values():
            item = QTableWidgetItem("")
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.cryptoTabAccountTable.setItem(current_rows, column, item)

    def _table_widget_reduce_row(self):
        """TableWidget移除当前选中的行"""
        current_row = self.ui.cryptoTabAccountTable.currentRow()
        self.ui.cryptoTabAccountTable.removeRow(current_row)

    def _table_widget_clear_rows(self):
        """TableWidget清空当前所有行的内容"""
        self.ui.cryptoTabAccountTable.setRowCount(0)
        self._table_widget_add_row()

    def _get_crypto_value(self, key, default=""):
        """获取私有属性_crypto_value中的值,获取完后会将key删除;"""
        value_ = self._crypto_value.get(key, None)
        if value_ is None:
            return default
        del self._crypto_value[key]
        return value_

    def _encrypt_cells_password(self, row, column):
        """当单元格内容发生改变时需要出发此方法;
        此函数是将指定列的单元格内容进行加密展示,用于密码单元格;"""
        columns = basedata.COLUMN2INDEX
        if column not in [columns.get("U盾密码"), columns.get("登录密码")]:
            return None
        value = self.ui.cryptoTabAccountTable.item(row, column).text()
        # 对单元格的内容进行判断,防止循环调用
        if not value:
            self._crypto_value[f"{row}{column}"] = ""
            return None
        if ("*" * len(value)) == value:
            return None
        self._crypto_value[f"{row}{column}"] = value
        encrypt_value = QTableWidgetItem("*" * len(value))
        self.ui.cryptoTabAccountTable.setItem(row, column, encrypt_value)

    def _get_table_widget_content(self):
        rows = self.ui.cryptoTabAccountTable.rowCount()
        total = list()
        for row in range(rows):
            current_dict = dict()
            for name, column in basedata.COLUMN2INDEX.items():
                if name == "登录密码" or name == "U盾密码":
                    current_dict[name] = self._get_crypto_value(f"{row}{column}")
                    continue
                item = self.ui.cryptoTabAccountTable.item(row, column)
                current_dict[name] = item.text()
            if any(current_dict.values()):
                total.append(current_dict)
        return total

    def _submit_crypto(self):
        """cryptoTab;提交加密"""
        self.public_keystore = self.ui.cryptoTabFileEdit.text()
        if not os.path.exists(self.public_keystore):
            return QMessageBox.warning(
                self.ui, "警告", "您还未选择公钥文件,或选择的文件无效!")
        all_content = self._get_table_widget_content()
        self._table_widget_clear_rows()
        if not all_content:
            return QMessageBox.warning(self.ui, "警告", "请先输入账户信息!")
        action = AccountAction(self.public_keystore)
        action.expand_account(all_content)
        QMessageBox.about(self.ui, "提示", "加密完成!")


class DisplayWindow(object):
    """用于展示文本内容的小窗口"""

    def __init__(self, uipath=None):
        path = uipath or "ui/display_information.ui"
        qfile = read_ui_file(path)
        self.window = QUiLoader().load(qfile)
        self.initialization()

    def initialization(self):
        self.window.returnButton.clicked.connect(
            self.window.close)

    def show(self):
        self.window.show()

    def close(self):
        self.window.close()

    def set_content(self, text):
        self.window.contentBrowser.setPlainText(text)

    def set_window_title(self, title):
        self.window.setWindowTitle(title)


if __name__ == '__main__':
    app = QApplication()
    client = CryptoClient("ui/account_crypto.ui")
    sub_window = DisplayWindow("ui/display_information.ui")
    client.show()
    app.exec_()
