# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'account_crypto.ui'
#
# Created by: Qt User Interface Compiler version 5.15.2
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1045, 780)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_13 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamily(u"Sitka Subheading")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.cryptoTab = QWidget()
        self.cryptoTab.setObjectName(u"cryptoTab")
        self.verticalLayout_3 = QVBoxLayout(self.cryptoTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.cryptoTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 993, 641))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 200, -1)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.cryptoTabFileEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.cryptoTabFileEdit.setObjectName(u"cryptoTabFileEdit")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(12)
        self.cryptoTabFileEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.cryptoTabFileEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.cryptoTabBrowseButton = QPushButton(self.scrollAreaWidgetContents)
        self.cryptoTabBrowseButton.setObjectName(u"cryptoTabBrowseButton")

        self.horizontalLayout.addWidget(self.cryptoTabBrowseButton)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout_15.addLayout(self.horizontalLayout)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cryptoTabAddRow = QPushButton(self.groupBox)
        self.cryptoTabAddRow.setObjectName(u"cryptoTabAddRow")
        font2 = QFont()
        font2.setFamily(u"Sitka Subheading")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.cryptoTabAddRow.setFont(font2)

        self.horizontalLayout_2.addWidget(self.cryptoTabAddRow)

        self.cryptoTabRemoveRow = QPushButton(self.groupBox)
        self.cryptoTabRemoveRow.setObjectName(u"cryptoTabRemoveRow")
        self.cryptoTabRemoveRow.setFont(font2)

        self.horizontalLayout_2.addWidget(self.cryptoTabRemoveRow)

        self.cryptoTabClearRow = QPushButton(self.groupBox)
        self.cryptoTabClearRow.setObjectName(u"cryptoTabClearRow")

        self.horizontalLayout_2.addWidget(self.cryptoTabClearRow)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_15.addWidget(self.groupBox)

        self.cryptoTabAccountTable = QTableWidget(self.scrollAreaWidgetContents)
        if (self.cryptoTabAccountTable.columnCount() < 7):
            self.cryptoTabAccountTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.cryptoTabAccountTable.rowCount() < 1):
            self.cryptoTabAccountTable.setRowCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setItem(0, 2, __qtablewidgetitem10)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        font3 = QFont()
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem11.setFont(font3)
        __qtablewidgetitem11.setBackground(brush1)
        __qtablewidgetitem11.setForeground(brush)
        self.cryptoTabAccountTable.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setItem(0, 5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter)
        self.cryptoTabAccountTable.setItem(0, 6, __qtablewidgetitem14)
        self.cryptoTabAccountTable.setObjectName(u"cryptoTabAccountTable")
        self.cryptoTabAccountTable.setFont(font1)
        self.cryptoTabAccountTable.setTextElideMode(Qt.ElideMiddle)
        self.cryptoTabAccountTable.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.cryptoTabAccountTable.horizontalHeader().setDefaultSectionSize(180)
        self.cryptoTabAccountTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_15.addWidget(self.cryptoTabAccountTable)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.cryptoTabEncryptButton = QPushButton(self.scrollAreaWidgetContents)
        self.cryptoTabEncryptButton.setObjectName(u"cryptoTabEncryptButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cryptoTabEncryptButton.sizePolicy().hasHeightForWidth())
        self.cryptoTabEncryptButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.cryptoTabEncryptButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_15.addLayout(self.verticalLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.cryptoTab, "")
        self.modifyTab = QWidget()
        self.modifyTab.setObjectName(u"modifyTab")
        self.verticalLayout_8 = QVBoxLayout(self.modifyTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_2 = QScrollArea(self.modifyTab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 993, 641))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_2.setFont(font4)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.modifyTabTypeComboBox = QComboBox(self.scrollAreaWidgetContents_2)
        self.modifyTabTypeComboBox.addItem("")
        self.modifyTabTypeComboBox.addItem("")
        self.modifyTabTypeComboBox.addItem("")
        self.modifyTabTypeComboBox.addItem("")
        self.modifyTabTypeComboBox.setObjectName(u"modifyTabTypeComboBox")
        self.modifyTabTypeComboBox.setFont(font1)

        self.horizontalLayout_4.addWidget(self.modifyTabTypeComboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_14.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.modifyTabTargetAccount = QLineEdit(self.scrollAreaWidgetContents_2)
        self.modifyTabTargetAccount.setObjectName(u"modifyTabTargetAccount")
        self.modifyTabTargetAccount.setFont(font1)

        self.horizontalLayout_5.addWidget(self.modifyTabTargetAccount)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.modifyTabQueryAccounts = QPushButton(self.scrollAreaWidgetContents_2)
        self.modifyTabQueryAccounts.setObjectName(u"modifyTabQueryAccounts")

        self.horizontalLayout_5.addWidget(self.modifyTabQueryAccounts)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)
        self.horizontalLayout_5.setStretch(2, 1)
        self.horizontalLayout_5.setStretch(3, 1)
        self.horizontalLayout_5.setStretch(4, 3)

        self.verticalLayout_14.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.modifyTabNewValue = QLineEdit(self.scrollAreaWidgetContents_2)
        self.modifyTabNewValue.setObjectName(u"modifyTabNewValue")
        self.modifyTabNewValue.setFont(font1)

        self.horizontalLayout_6.addWidget(self.modifyTabNewValue)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.modifyTabClearNewValue = QPushButton(self.scrollAreaWidgetContents_2)
        self.modifyTabClearNewValue.setObjectName(u"modifyTabClearNewValue")

        self.horizontalLayout_6.addWidget(self.modifyTabClearNewValue)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 1)
        self.horizontalLayout_6.setStretch(4, 3)

        self.verticalLayout_14.addLayout(self.horizontalLayout_6)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font2)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Sitka Subheading")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_6.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.modifyTabLoginPassword = QLineEdit(self.groupBox_2)
        self.modifyTabLoginPassword.setObjectName(u"modifyTabLoginPassword")
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.modifyTabLoginPassword.setFont(font6)
        self.modifyTabLoginPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.modifyTabLoginPassword)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.modifyTabUKeyPassword = QLineEdit(self.groupBox_2)
        self.modifyTabUKeyPassword.setObjectName(u"modifyTabUKeyPassword")
        self.modifyTabUKeyPassword.setFont(font6)
        self.modifyTabUKeyPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.modifyTabUKeyPassword)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_8)


        self.verticalLayout_14.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font2)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(55, -1, 55, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textBrowser_3 = QTextBrowser(self.groupBox_5)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setFont(font5)

        self.verticalLayout_4.addWidget(self.textBrowser_3)

        self.modifyTabConfirmProtocol = QCheckBox(self.groupBox_5)
        self.modifyTabConfirmProtocol.setObjectName(u"modifyTabConfirmProtocol")
        self.modifyTabConfirmProtocol.setFont(font5)

        self.verticalLayout_4.addWidget(self.modifyTabConfirmProtocol)

        self.verticalSpacer_3 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(400, -1, -1, -1)
        self.modifyTabSubmitButton = QPushButton(self.groupBox_5)
        self.modifyTabSubmitButton.setObjectName(u"modifyTabSubmitButton")
        self.modifyTabSubmitButton.setEnabled(False)
        sizePolicy.setHeightForWidth(self.modifyTabSubmitButton.sizePolicy().hasHeightForWidth())
        self.modifyTabSubmitButton.setSizePolicy(sizePolicy)
        self.modifyTabSubmitButton.setFont(font5)
        self.modifyTabSubmitButton.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_5.addWidget(self.modifyTabSubmitButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalSpacer_4 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)


        self.verticalLayout_14.addWidget(self.groupBox_5)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.modifyTab, "")
        self.queryTab = QWidget()
        self.queryTab.setObjectName(u"queryTab")
        self.verticalLayout_9 = QVBoxLayout(self.queryTab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_3 = QScrollArea(self.queryTab)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 993, 641))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_8)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.queryTabQueryOne = QRadioButton(self.groupBox_3)
        self.queryRangeButtonGroup = QButtonGroup(MainWindow)
        self.queryRangeButtonGroup.setObjectName(u"queryRangeButtonGroup")
        self.queryRangeButtonGroup.addButton(self.queryTabQueryOne)
        self.queryTabQueryOne.setObjectName(u"queryTabQueryOne")
        self.queryTabQueryOne.setTabletTracking(False)
        self.queryTabQueryOne.setAcceptDrops(False)
        self.queryTabQueryOne.setChecked(True)

        self.horizontalLayout_9.addWidget(self.queryTabQueryOne)

        self.queryTabQueryAll = QRadioButton(self.groupBox_3)
        self.queryRangeButtonGroup.addButton(self.queryTabQueryAll)
        self.queryTabQueryAll.setObjectName(u"queryTabQueryAll")

        self.horizontalLayout_9.addWidget(self.queryTabQueryAll)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.queryTabQueryType = QComboBox(self.groupBox_3)
        self.queryTabQueryType.addItem("")
        self.queryTabQueryType.addItem("")
        self.queryTabQueryType.addItem("")
        self.queryTabQueryType.addItem("")
        self.queryTabQueryType.setObjectName(u"queryTabQueryType")

        self.horizontalLayout_10.addWidget(self.queryTabQueryType)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)


        self.verticalLayout_16.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.queryTabMatchValue = QLineEdit(self.groupBox_3)
        self.queryTabMatchValue.setObjectName(u"queryTabMatchValue")
        self.queryTabMatchValue.setFont(font1)

        self.horizontalLayout_11.addWidget(self.queryTabMatchValue)

        self.queryTabCompleteMatch = QRadioButton(self.groupBox_3)
        self.matchModeButtonGroup = QButtonGroup(MainWindow)
        self.matchModeButtonGroup.setObjectName(u"matchModeButtonGroup")
        self.matchModeButtonGroup.addButton(self.queryTabCompleteMatch)
        self.queryTabCompleteMatch.setObjectName(u"queryTabCompleteMatch")
        self.queryTabCompleteMatch.setChecked(True)

        self.horizontalLayout_11.addWidget(self.queryTabCompleteMatch)

        self.queryTabVagueMatch = QRadioButton(self.groupBox_3)
        self.matchModeButtonGroup.addButton(self.queryTabVagueMatch)
        self.queryTabVagueMatch.setObjectName(u"queryTabVagueMatch")

        self.horizontalLayout_11.addWidget(self.queryTabVagueMatch)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)


        self.verticalLayout_16.addLayout(self.horizontalLayout_11)


        self.verticalLayout_17.addWidget(self.groupBox_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_9)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)


        self.verticalLayout_17.addLayout(self.horizontalLayout_12)

        self.queryTabShowResult = QTextBrowser(self.scrollAreaWidgetContents_3)
        self.queryTabShowResult.setObjectName(u"queryTabShowResult")
        self.queryTabShowResult.setFont(font1)
        self.queryTabShowResult.setLineWrapMode(QTextEdit.NoWrap)
        self.queryTabShowResult.setOverwriteMode(False)
        self.queryTabShowResult.setOpenExternalLinks(False)
        self.queryTabShowResult.setOpenLinks(False)

        self.verticalLayout_17.addWidget(self.queryTabShowResult)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_17.addItem(self.verticalSpacer_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.queryTabSubmitQuery = QPushButton(self.scrollAreaWidgetContents_3)
        self.queryTabSubmitQuery.setObjectName(u"queryTabSubmitQuery")
        sizePolicy.setHeightForWidth(self.queryTabSubmitQuery.sizePolicy().hasHeightForWidth())
        self.queryTabSubmitQuery.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.queryTabSubmitQuery)


        self.verticalLayout_17.addLayout(self.horizontalLayout_13)


        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_9.addWidget(self.scrollArea_3)

        self.tabWidget.addTab(self.queryTab, "")
        self.removeTab = QWidget()
        self.removeTab.setObjectName(u"removeTab")
        self.horizontalLayout_16 = QHBoxLayout(self.removeTab)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.scrollArea_4 = QScrollArea(self.removeTab)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 993, 641))
        self.horizontalLayout_19 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_16 = QSpacerItem(125, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_16)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_2)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 20)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, 200, -1)
        self.label_10 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.horizontalLayout_14.addWidget(self.label_10)

        self.removeTabTargetAccount = QLineEdit(self.scrollAreaWidgetContents_4)
        self.removeTabTargetAccount.setObjectName(u"removeTabTargetAccount")
        self.removeTabTargetAccount.setFont(font1)

        self.horizontalLayout_14.addWidget(self.removeTabTargetAccount)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.removeTabShowAccounts = QPushButton(self.scrollAreaWidgetContents_4)
        self.removeTabShowAccounts.setObjectName(u"removeTabShowAccounts")

        self.horizontalLayout_14.addWidget(self.removeTabShowAccounts)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textBrowser_2 = QTextBrowser(self.groupBox_4)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_10.addWidget(self.textBrowser_2)

        self.removeTabConfirmProtocol = QCheckBox(self.groupBox_4)
        self.removeTabConfirmProtocol.setObjectName(u"removeTabConfirmProtocol")

        self.verticalLayout_10.addWidget(self.removeTabConfirmProtocol)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)


        self.verticalLayout_12.addWidget(self.groupBox_4)

        self.verticalSpacer_6 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.removeTabSubmitButton = QPushButton(self.scrollAreaWidgetContents_4)
        self.removeTabSubmitButton.setObjectName(u"removeTabSubmitButton")
        self.removeTabSubmitButton.setEnabled(False)
        sizePolicy.setHeightForWidth(self.removeTabSubmitButton.sizePolicy().hasHeightForWidth())
        self.removeTabSubmitButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.removeTabSubmitButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_19.addLayout(self.verticalLayout_12)

        self.line_3 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_3)

        self.horizontalSpacer_17 = QSpacerItem(125, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_17)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_16.addWidget(self.scrollArea_4)

        self.tabWidget.addTab(self.removeTab, "")

        self.verticalLayout_13.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1045, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8d26\u6237\u52a0\u5bc6\u5de5\u5177", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u516c\u94a5\u6587\u4ef6\uff1a", None))
        self.cryptoTabBrowseButton.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u533a", None))
        self.cryptoTabAddRow.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.cryptoTabRemoveRow.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.cryptoTabClearRow.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        ___qtablewidgetitem = self.cryptoTabAccountTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u94f6\u884c\u540d\u79f0", None))
        ___qtablewidgetitem1 = self.cryptoTabAccountTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u94f6\u884c\u8d26\u6237", None))
        ___qtablewidgetitem2 = self.cryptoTabAccountTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u6237\u540d\u79f0", None))
        ___qtablewidgetitem3 = self.cryptoTabAccountTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u5bc6\u7801", None))
        ___qtablewidgetitem4 = self.cryptoTabAccountTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"U\u76fe\u5bc6\u7801", None))
        ___qtablewidgetitem5 = self.cryptoTabAccountTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u6237\u53f7(\u53ef\u9009)", None))
        ___qtablewidgetitem6 = self.cryptoTabAccountTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u5458\u53f7(\u53ef\u9009)", None))
        ___qtablewidgetitem7 = self.cryptoTabAccountTable.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1", None))

        __sortingEnabled = self.cryptoTabAccountTable.isSortingEnabled()
        self.cryptoTabAccountTable.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.cryptoTabAccountTable.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u5982\uff1a\u4e2d\u56fd\u94f6\u884c", None))
        ___qtablewidgetitem9 = self.cryptoTabAccountTable.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u5982\uff1a1001", None))
        ___qtablewidgetitem10 = self.cryptoTabAccountTable.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u5982\uff1aXX\u6709\u9650\u516c\u53f8", None))
        self.cryptoTabAccountTable.setSortingEnabled(__sortingEnabled)

        self.cryptoTabEncryptButton.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cryptoTab), QCoreApplication.translate("MainWindow", u"\u8d26\u6237\u52a0\u5bc6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u7c7b\u578b\uff1a", None))
        self.modifyTabTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u5bc6\u7801", None))
        self.modifyTabTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"U\u76fe\u5bc6\u7801", None))
        self.modifyTabTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5ba2\u6237\u53f7", None))
        self.modifyTabTypeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u5458\u53f7", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u8d26\u6237\uff1a", None))
        self.modifyTabQueryAccounts.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u65b0\u503c\uff1a", None))
        self.modifyTabClearNewValue.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8ba4\u8bc1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u8d26\u6237\u767b\u5f55\u5bc6\u7801\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u8d26\u6237U\u76fe\u5bc6\u7801\uff1a ", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u8bf7\u5148\u9605\u8bfb\u5e76\u540c\u610f\u534f\u8bae", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap }\n"
"</style></head><body style=\" font-family:'Sitka Subheading','Sitka Subheading','Sitka Subheading' font-size:12pt font-weight:400 font-style:normal\">\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif' font-size:14pt font-weight:696 color:#333333 background-color:#ffffff\">\u00a0\u5c0a\u656c\u7684\u7528\u6237\uff1a</span></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><span style=\" font-family:'Sitka Subheading'\">\u4e3a\u4e86\u66f4\u597d\u5730\u4e3a\u60a8\u63d0\u4f9b\u670d\u52a1\uff0c\u8bf7\u60a8\u4ed4\u7ec6\u9605\u8bfb\u672c\u300a\u7528\u6237\u670d\u52a1"
                        "\u534f\u8bae\u300b\uff08\u4ee5\u4e0b\u7b80\u79f0\u201c\u672c\u534f\u8bae\u201d\uff09\u3002\u5728\u60a8\u5f00\u59cb\u4f7f\u7528\u672c\u5e94\u7528\u53ca\u76f8\u5173\u670d\u52a1\u4e4b\u524d\uff0c\u8bf7\u60a8\u52a1\u5fc5\u8ba4\u771f\u9605\u8bfb\u5e76\u5145\u5206\u7406\u89e3\u672c\u534f\u8bae\uff0c\u5982\u60a8\u672a\u6ee118\u5468\u5c81\uff0c\u8bf7\u60a8\u5728\u6cd5\u5b9a\u76d1\u62a4\u4eba\u966a\u540c\u4e0b\u4ed4\u7ec6\u9605\u8bfb\u5e76\u5145\u5206\u7406\u89e3\u672c\u534f\u8bae\uff0c\u5e76\u5f81\u5f97\u6cd5\u5b9a\u76d1\u62a4\u4eba\u7684\u540c\u610f\u540e\u4e0b\u8f7d\u672c\u5e94\u7528\u3002\u5f53\u60a8\u5b8c\u5168\u5b8c\u6210\u6ce8\u518c\u7a0b\u5e8f\uff0c\u4fbf\u6210\u4e3a\u672c\u5e94\u7528\u7684\u6ce8\u518c\u7528\u6237\uff0c\u540c\u65f6\u6b64\u534f\u8bae\u5373\u65f6\u751f\u6548\u3002\u60a8\u6709\u4e49\u52a1\u4fdd\u8bc1\u5bc6\u7801\u548c\u5e10\u53f7\u7684\u5b89\u5168\u3002\u60a8\u5bf9\u5229\u7528\u8be5\u5bc6\u7801\u548c\u5e10\u53f7\u6240\u8fdb\u884c\u7684\u4e00\u5207\u6d3b\u52a8\u8d1f\u5168\u90e8\u8d23\u4efb\uff1b\u56e0"
                        "\u6b64\u6240\u884d\u751f\u7684\u4efb\u4f55\u635f\u5931\u6216\u635f\u5bb3\uff0c\u6211\u4eec\u65e0\u6cd5\u4e5f\u4e0d\u627f\u62c5\u4efb\u4f55\u8d23\u4efb\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px font-family:'Sitka Subheading'\"><br /></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><span style=\" font-family:'Sitka Subheading'\">\u4e3a\u4e86\u80fd\u4f7f\u7528\u672c\u670d\u52a1\uff0c\u60a8\u540c\u610f\u4ee5\u4e0b\u4e8b\u9879\uff1a</span></p>\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px font-family:'Sitka Subheading'\"><br /></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><span style=\" font-family:'Sitka Subheading'\">(1) \u7ef4"
                        "\u6301\u66f4\u65b0\u60a8\u4e2a\u4eba\u7528\u6237\u4fe1\u606f\uff0c\u786e\u4fdd\u5176\u771f\u5b9e\u3001\u6b63\u786e\u3001\u6700\u65b0\u53ca\u5b8c\u6574\u3002</span></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><span style=\" font-family:'Sitka Subheading'\">\u82e5\u60a8\u63d0\u4f9b\u4efb\u4f55\u9519\u8bef\u3001\u4e0d\u5b9e\u3001\u8fc7\u65f6\u6216\u4e0d\u5b8c\u6574\u7684\u8d44\u6599\uff0c\u5e76\u4e3a\u5e94\u7528\u6240\u786e\u77e5\uff0c\u6216\u8005\u5e94\u7528\u6709\u5408\u7406\u7684\u7406\u7531\u6000\u7591\u524d\u8ff0\u8d44\u6599\u4e3a\u9519\u8bef\u3001\u4e0d\u5b9e\u3001\u8fc7\u65f6\u6216\u4e0d\u5b8c\u6574\uff0c\u6211\u53f8\u6709\u6743\u6682\u505c\u6216\u7ec8\u6b62\u60a8\u7684\u5e10\u53f7\uff0c\u5e76\u62d2\u7edd\u60a8\u4e8e\u73b0\u5728\u548c\u672a\u6765\u4f7f\u7528\u5e94\u7528\u5168\u90e8\u6216\u90e8\u5206\u7684\u670d\u52a1\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0"
                        "px margin-right:0px -qt-block-indent:0 text-indent:0px font-family:'Sitka Subheading'\"><br /></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><span style=\" font-family:'Sitka Subheading'\">(2) \u5e94\u7528\u4e0d\u5bf9\u7528\u6237\u6240\u53d1\u5e03\u4fe1\u606f\u7684\u5220\u9664\u6216\u50a8\u5b58\u5931\u8d25\u8d1f\u8d23\u3002</span></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><span style=\" font-family:'Sitka Subheading'\">\u5e94\u7528\u5e76\u4e0d\u627f\u8bfa\u5bf9\u7528\u6237\u7684\u5b58\u50a8\u4fe1\u606f\u8fdb\u884c\u65e0\u9650\u671f\u4fdd\u7559\u3002\u9664\u975e\u672c\u534f\u8bae\u4e2d\u53e6\u6709\u89c4\u5b9a\uff0c\u5426\u5219\u5e94\u7528\u4e0d\u4fdd\u8bc1\u670d\u52a1\u4e00\u5b9a\u4f1a\u6ee1\u8db3\u7528\u6237\u7684\u4f7f\u7528\u8981\u6c42\uff0c\u4e5f\u4e0d\u4fdd\u8bc1\u670d\u52a1\u4e0d\u4f1a\u53d7\u4e2d\u65ad\uff0c\u5bf9\u670d\u52a1\u7684"
                        "\u53ca\u65f6\u6027\u3001\u5b89\u5168\u6027\u3001\u51c6\u786e\u6027\u4e5f\u4e0d\u4f5c\u62c5\u4fdd\u3002\u5e94\u7528\u6709\u5224\u5b9a\u7528\u6237\u7684\u884c\u4e3a\u662f\u5426\u7b26\u5408\u5e94\u7528\u670d\u52a1\u6761\u6b3e\u7684\u8981\u6c42\u548c\u7cbe\u795e\u7684\u4fdd\u7559\u6743\u5229\uff0c\u5982\u679c\u7528\u6237\u8fdd\u80cc\u4e86\u670d\u52a1\u6761\u6b3e\u7684\u89c4\u5b9a\uff0c\u5e94\u7528\u6709\u4e2d\u65ad\u5bf9\u5176\u63d0\u4f9b\u7f51\u7edc\u670d\u52a1\u7684\u6743\u5229\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px font-family:'Sitka Subheading'\"><br /></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><span style=\" font-family:'Sitka Subheading'\">(3) \u7528\u6237\u5bf9\u7f51\u7edc\u670d\u52a1\u7684\u4f7f\u7528\u627f\u62c5\u98ce\u9669\u3002\u5e94\u7528\u5bf9\u6b64\u4e0d\u4f5c\u4efb\u4f55\u7c7b\u578b\u7684"
                        "\u62c5\u4fdd\uff0c\u4e0d\u8bba\u662f\u660e\u786e\u7684\u6216\u9690\u542b\u7684\uff0c\u4f46\u662f\u4e0d\u5bf9\u5546\u4e1a\u6027\u7684\u9690\u542b\u62c5\u4fdd\u3001\u7279\u5b9a\u76ee\u7684\u548c\u4e0d\u8fdd\u53cd\u89c4\u5b9a\u7684\u9002\u5f53\u62c5\u4fdd\u4f5c\u9650\u5236</span></p>\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px font-family:'Sitka Subheading'\"><br /></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><span style=\" font-family:'Sitka Subheading'\">(4) \u7528\u6237\u5355\u72ec\u627f\u62c5\u53d1\u5e03\u5185\u5bb9\u7684\u8d23\u4efb\u3002\u7528\u6237\u5bf9\u670d\u52a1\u7684\u4f7f\u7528\u662f\u6839\u636e\u6240\u6709\u9002\u7528\u4e8e\u5e94\u7528\u7684\u56fd\u5bb6\u6cd5\u5f8b\u3001\u5730\u65b9\u6cd5\u5f8b\u548c\u56fd\u9645\u6cd5\u5f8b\u6807\u51c6\u7684\u3002</span></p></body></html>", None))
        self.modifyTabConfirmProtocol.setText(QCoreApplication.translate("MainWindow", u"\u540c\u610f\u670d\u52a1\u534f\u8bae", None))
        self.modifyTabSubmitButton.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modifyTab), QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u8d26\u6237", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u8303\u56f4", None))
        self.queryTabQueryOne.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u5355\u4e2a", None))
        self.queryTabQueryAll.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u5168\u90e8", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u7c7b\u578b\uff1a", None))
        self.queryTabQueryType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u94f6\u884c\u540d\u79f0", None))
        self.queryTabQueryType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u94f6\u884c\u8d26\u6237", None))
        self.queryTabQueryType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u8d26\u6237\u540d\u79f0", None))
        self.queryTabQueryType.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5339\u914d\u5185\u5bb9\uff1a", None))
        self.queryTabCompleteMatch.setText(QCoreApplication.translate("MainWindow", u"\u5b8c\u6574\u5339\u914d", None))
        self.queryTabVagueMatch.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u7cca\u5339\u914d", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5bb9\u5c55\u793a", None))
        self.queryTabShowResult.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap }\n"
"</style></head><body style=\" font-family:'Calibri','Sitka Subheading' font-size:12pt font-weight:400 font-style:normal\">\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><br /></p></body></html>", None))
        self.queryTabSubmitQuery.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.queryTab), QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u8d26\u6237", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u8d26\u6237\uff1a", None))
        self.removeTabShowAccounts.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u6240\u6709\u8d26\u6237", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u8bf7\u5148\u9605\u8bfb\u5e76\u540c\u610f\u534f\u8bae", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap }\n"
"</style></head><body style=\" font-family:'Sitka Subheading' font-size:12pt font-weight:400 font-style:normal\">\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><span style=\" font-family:'Helvetica Neue','Helvetica','Arial','sans-serif' font-size:14pt font-weight:696 color:#333333 background-color:#ffffff\">\u00a0\u5c0a\u656c\u7684\u7528\u6237\uff1a</span></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\">\u4e3a\u4e86\u66f4\u597d\u5730\u4e3a\u60a8\u63d0\u4f9b\u670d\u52a1\uff0c\u8bf7\u60a8\u4ed4\u7ec6\u9605\u8bfb\u672c\u300a\u7528\u6237\u670d\u52a1\u534f\u8bae\u300b\uff08\u4ee5\u4e0b\u7b80\u79f0\u201c\u672c\u534f\u8bae\u201d\uff09"
                        "\u3002\u5728\u60a8\u5f00\u59cb\u4f7f\u7528\u672c\u5e94\u7528\u53ca\u76f8\u5173\u670d\u52a1\u4e4b\u524d\uff0c\u8bf7\u60a8\u52a1\u5fc5\u8ba4\u771f\u9605\u8bfb\u5e76\u5145\u5206\u7406\u89e3\u672c\u534f\u8bae\uff0c\u5982\u60a8\u672a\u6ee118\u5468\u5c81\uff0c\u8bf7\u60a8\u5728\u6cd5\u5b9a\u76d1\u62a4\u4eba\u966a\u540c\u4e0b\u4ed4\u7ec6\u9605\u8bfb\u5e76\u5145\u5206\u7406\u89e3\u672c\u534f\u8bae\uff0c\u5e76\u5f81\u5f97\u6cd5\u5b9a\u76d1\u62a4\u4eba\u7684\u540c\u610f\u540e\u4e0b\u8f7d\u672c\u5e94\u7528\u3002\u5f53\u60a8\u5b8c\u5168\u5b8c\u6210\u6ce8\u518c\u7a0b\u5e8f\uff0c\u4fbf\u6210\u4e3a\u672c\u5e94\u7528\u7684\u6ce8\u518c\u7528\u6237\uff0c\u540c\u65f6\u6b64\u534f\u8bae\u5373\u65f6\u751f\u6548\u3002\u60a8\u6709\u4e49\u52a1\u4fdd\u8bc1\u5bc6\u7801\u548c\u5e10\u53f7\u7684\u5b89\u5168\u3002\u60a8\u5bf9\u5229\u7528\u8be5\u5bc6\u7801\u548c\u5e10\u53f7\u6240\u8fdb\u884c\u7684\u4e00\u5207\u6d3b\u52a8\u8d1f\u5168\u90e8\u8d23\u4efb\uff1b\u56e0\u6b64\u6240\u884d\u751f\u7684\u4efb\u4f55\u635f\u5931\u6216\u635f\u5bb3\uff0c\u6211"
                        "\u4eec\u65e0\u6cd5\u4e5f\u4e0d\u627f\u62c5\u4efb\u4f55\u8d23\u4efb\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><br /></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\">\u4e3a\u4e86\u80fd\u4f7f\u7528\u672c\u670d\u52a1\uff0c\u60a8\u540c\u610f\u4ee5\u4e0b\u4e8b\u9879\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><br /></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\">(1) \u7ef4\u6301\u66f4\u65b0\u60a8\u4e2a\u4eba\u7528\u6237\u4fe1\u606f\uff0c\u786e\u4fdd\u5176\u771f\u5b9e\u3001\u6b63\u786e\u3001\u6700\u65b0\u53ca\u5b8c\u6574\u3002</p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-in"
                        "dent:0 text-indent:0px\">\u82e5\u60a8\u63d0\u4f9b\u4efb\u4f55\u9519\u8bef\u3001\u4e0d\u5b9e\u3001\u8fc7\u65f6\u6216\u4e0d\u5b8c\u6574\u7684\u8d44\u6599\uff0c\u5e76\u4e3a\u5e94\u7528\u6240\u786e\u77e5\uff0c\u6216\u8005\u5e94\u7528\u6709\u5408\u7406\u7684\u7406\u7531\u6000\u7591\u524d\u8ff0\u8d44\u6599\u4e3a\u9519\u8bef\u3001\u4e0d\u5b9e\u3001\u8fc7\u65f6\u6216\u4e0d\u5b8c\u6574\uff0c\u6211\u53f8\u6709\u6743\u6682\u505c\u6216\u7ec8\u6b62\u60a8\u7684\u5e10\u53f7\uff0c\u5e76\u62d2\u7edd\u60a8\u4e8e\u73b0\u5728\u548c\u672a\u6765\u4f7f\u7528\u5e94\u7528\u5168\u90e8\u6216\u90e8\u5206\u7684\u670d\u52a1\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><br /></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\">(2) \u5e94\u7528\u4e0d\u5bf9\u7528\u6237\u6240\u53d1\u5e03\u4fe1\u606f\u7684\u5220\u9664\u6216\u50a8\u5b58\u5931\u8d25\u8d1f\u8d23"
                        "\u3002</p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\">\u5e94\u7528\u5e76\u4e0d\u627f\u8bfa\u5bf9\u7528\u6237\u7684\u5b58\u50a8\u4fe1\u606f\u8fdb\u884c\u65e0\u9650\u671f\u4fdd\u7559\u3002\u9664\u975e\u672c\u534f\u8bae\u4e2d\u53e6\u6709\u89c4\u5b9a\uff0c\u5426\u5219\u5e94\u7528\u4e0d\u4fdd\u8bc1\u670d\u52a1\u4e00\u5b9a\u4f1a\u6ee1\u8db3\u7528\u6237\u7684\u4f7f\u7528\u8981\u6c42\uff0c\u4e5f\u4e0d\u4fdd\u8bc1\u670d\u52a1\u4e0d\u4f1a\u53d7\u4e2d\u65ad\uff0c\u5bf9\u670d\u52a1\u7684\u53ca\u65f6\u6027\u3001\u5b89\u5168\u6027\u3001\u51c6\u786e\u6027\u4e5f\u4e0d\u4f5c\u62c5\u4fdd\u3002\u5e94\u7528\u6709\u5224\u5b9a\u7528\u6237\u7684\u884c\u4e3a\u662f\u5426\u7b26\u5408\u5e94\u7528\u670d\u52a1\u6761\u6b3e\u7684\u8981\u6c42\u548c\u7cbe\u795e\u7684\u4fdd\u7559\u6743\u5229\uff0c\u5982\u679c\u7528\u6237\u8fdd\u80cc\u4e86\u670d\u52a1\u6761\u6b3e\u7684\u89c4\u5b9a\uff0c\u5e94\u7528\u6709\u4e2d\u65ad\u5bf9\u5176\u63d0\u4f9b\u7f51\u7edc\u670d\u52a1\u7684"
                        "\u6743\u5229\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><br /></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\">(3) \u7528\u6237\u5bf9\u7f51\u7edc\u670d\u52a1\u7684\u4f7f\u7528\u627f\u62c5\u98ce\u9669\u3002\u5e94\u7528\u5bf9\u6b64\u4e0d\u4f5c\u4efb\u4f55\u7c7b\u578b\u7684\u62c5\u4fdd\uff0c\u4e0d\u8bba\u662f\u660e\u786e\u7684\u6216\u9690\u542b\u7684\uff0c\u4f46\u662f\u4e0d\u5bf9\u5546\u4e1a\u6027\u7684\u9690\u542b\u62c5\u4fdd\u3001\u7279\u5b9a\u76ee\u7684\u548c\u4e0d\u8fdd\u53cd\u89c4\u5b9a\u7684\u9002\u5f53\u62c5\u4fdd\u4f5c\u9650\u5236</p>\n"
"<p style=\"-qt-paragraph-type:empty margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0px\"><br /></p>\n"
"<p style=\" margin-top:0px margin-bottom:0px margin-left:0px margin-right:0px -qt-block-indent:0 text-indent:0p"
                        "x\">(4) \u7528\u6237\u5355\u72ec\u627f\u62c5\u53d1\u5e03\u5185\u5bb9\u7684\u8d23\u4efb\u3002\u7528\u6237\u5bf9\u670d\u52a1\u7684\u4f7f\u7528\u662f\u6839\u636e\u6240\u6709\u9002\u7528\u4e8e\u5e94\u7528\u7684\u56fd\u5bb6\u6cd5\u5f8b\u3001\u5730\u65b9\u6cd5\u5f8b\u548c\u56fd\u9645\u6cd5\u5f8b\u6807\u51c6\u7684\u3002</p></body></html>", None))
        self.removeTabConfirmProtocol.setText(QCoreApplication.translate("MainWindow", u"\u540c\u610f\u670d\u52a1\u534f\u8bae", None))
        self.removeTabSubmitButton.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.removeTab), QCoreApplication.translate("MainWindow", u"\u5220\u9664\u8d26\u6237", None))
    # retranslateUi


class SubWindow(object):
    def setupUi(self, SubWindow):
        if not SubWindow.objectName():
            SubWindow.setObjectName(u"SubWindow")
        SubWindow.resize(481, 429)
        self.contentBrowser = QTextBrowser(SubWindow)
        self.contentBrowser.setObjectName(u"contentBrowser")
        self.contentBrowser.setGeometry(QRect(10, 10, 461, 331))
        font = QFont()
        font.setPointSize(12)
        self.contentBrowser.setFont(font)
        self.returnButton = QPushButton(SubWindow)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setGeometry(QRect(190, 370, 93, 41))

        self.retranslateUi(SubWindow)

        QMetaObject.connectSlotsByName(SubWindow)

    # setupUi

    def retranslateUi(self, SubWindow):
        SubWindow.setWindowTitle(QCoreApplication.translate("SubWindow", u"\u5c55\u793a", None))
        self.returnButton.setText(QCoreApplication.translate("SubWindow", u"\u8fd4\u56de", None))
    # retranslateUi
