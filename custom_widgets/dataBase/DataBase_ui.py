# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataBase.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DataBase(object):
    def setupUi(self, DataBase):
        if not DataBase.objectName():
            DataBase.setObjectName(u"DataBase")
        DataBase.resize(790, 525)
        DataBase.setStyleSheet(u"* {\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"#DataBase QLabel ,QPushButton{\n"
"color: rgb(189, 189, 189);\n"
"}\n"
"\n"
"\n"
"#DataBase QPushButton{\n"
"	border : 1px solid rgb(189, 189, 189);\n"
"	border-radius: 12px;\n"
"	padding: 15px;\n"
"\n"
"}\n"
"#DataBase #registerIdButton{\n"
"	background-color: rgb(0, 142, 246);\n"
"\n"
"}\n"
"#DataBase #batchRegisterButton{\n"
"	border: 1px solid  rgb(0, 142, 246);\n"
"}\n"
"#DataBase #deleteButton{\n"
"	border: 1px solid  red\n"
"\n"
"}\n"
"#DataBase #deleteButton::hover{\n"
"	\n"
"	background-color: rgb(255, 0, 4);\n"
"\n"
"}\n"
"#nameInput{\n"
"	background-color:  rgb(33, 33, 33);\n"
"	border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 12px;\n"
"    color: rgb(204, 204, 204);\n"
"\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(DataBase)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nameLabel = QLabel(DataBase)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setMinimumSize(QSize(0, 0))
        self.nameLabel.setMaximumSize(QSize(45, 16777215))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(10)
        font.setBold(True)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.nameLabel)

        self.nameInput = QLineEdit(DataBase)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setMinimumSize(QSize(0, 35))
        self.nameInput.setMaximumSize(QSize(170, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(10)
        self.nameInput.setFont(font1)

        self.horizontalLayout.addWidget(self.nameInput)

        self.modelingLabel = QLabel(DataBase)
        self.modelingLabel.setObjectName(u"modelingLabel")
        self.modelingLabel.setMaximumSize(QSize(65, 16777215))
        self.modelingLabel.setFont(font)
        self.modelingLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.modelingLabel)

        self.modelingComboBox = QComboBox(DataBase)
        self.modelingComboBox.addItem("")
        self.modelingComboBox.setObjectName(u"modelingComboBox")
        self.modelingComboBox.setFont(font1)

        self.horizontalLayout.addWidget(self.modelingComboBox)

        self.resetButton = QPushButton(DataBase)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setFont(font)

        self.horizontalLayout.addWidget(self.resetButton)

        self.searchButton = QPushButton(DataBase)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setFont(font)

        self.horizontalLayout.addWidget(self.searchButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.deleteButton = QPushButton(DataBase)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.deleteButton)

        self.checkBox = QCheckBox(DataBase)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font1)

        self.horizontalLayout_2.addWidget(self.checkBox)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.batchRegisterButton = QPushButton(DataBase)
        self.batchRegisterButton.setObjectName(u"batchRegisterButton")
        self.batchRegisterButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.batchRegisterButton)

        self.registerIdButton = QPushButton(DataBase)
        self.registerIdButton.setObjectName(u"registerIdButton")
        self.registerIdButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.registerIdButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.frame = QFrame(DataBase)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 750, 371))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cardInfoGrid = QGridLayout()
        self.cardInfoGrid.setSpacing(6)
        self.cardInfoGrid.setObjectName(u"cardInfoGrid")

        self.horizontalLayout_4.addLayout(self.cardInfoGrid)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DataBase)

        QMetaObject.connectSlotsByName(DataBase)
    # setupUi

    def retranslateUi(self, DataBase):
        DataBase.setWindowTitle(QCoreApplication.translate("DataBase", u"Form", None))
        self.nameLabel.setText(QCoreApplication.translate("DataBase", u"Name", None))
        self.modelingLabel.setText(QCoreApplication.translate("DataBase", u"Modeling", None))
        self.modelingComboBox.setItemText(0, QCoreApplication.translate("DataBase", u"ALL", None))

        self.resetButton.setText(QCoreApplication.translate("DataBase", u"Reset", None))
        self.searchButton.setText(QCoreApplication.translate("DataBase", u"Search", None))
        self.deleteButton.setText(QCoreApplication.translate("DataBase", u"Delete", None))
        self.checkBox.setText(QCoreApplication.translate("DataBase", u"ALL", None))
        self.batchRegisterButton.setText(QCoreApplication.translate("DataBase", u"Batch Register", None))
        self.registerIdButton.setText(QCoreApplication.translate("DataBase", u"Register ID", None))
    # retranslateUi

