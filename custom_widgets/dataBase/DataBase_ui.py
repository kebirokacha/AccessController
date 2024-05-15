# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataBase.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QGridLayout, QHBoxLayout, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from . import dataBase_rc

class Ui_DataBase(object):
    def setupUi(self, DataBase):
        if not DataBase.objectName():
            DataBase.setObjectName(u"DataBase")
        DataBase.resize(790, 529)
        DataBase.setStyleSheet(u"#DataBase ,#scrollAreaWidgetContents {\n"
"	background-color: rgb(33, 33, 33);\n"
"\n"
"}\n"
"#DataBase QLabel ,QPushButton{\n"
"	color: rgb(189, 189, 189);\n"
"\n"
"}\n"
"#DataBase QPushButton{\n"
"	border : 1px solid rgb(189, 189, 189);\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"\n"
"}\n"
"#DataBase  QPushButton:hover{\n"
"	background-color: rgb(0, 142, 246);\n"
"\n"
"}\n"
"#DataBase  #batchRegisterButton, #DataBase  #registerIdButton{\n"
"	border: 1px solid  rgb(0, 142, 246);\n"
"\n"
"}\n"
"#DataBase #deleteButton{\n"
"	border: 1px solid  red\n"
"\n"
"}\n"
"#DataBase #deleteButton::hover{\n"
"	background-color: rgb(255, 0, 4);\n"
"\n"
"}\n"
"#fieldInput{\n"
"	padding-left:5px;\n"
"	background-color:  rgb(33, 33, 33);\n"
"	border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 10px;\n"
"    color: rgb(204, 204, 204);\n"
"\n"
"}\n"
"\n"
"/* the style of the combobox is mostly generated with chatgpt (tried the gpt-40 and till now look good )*/\n"
"QComboBox {\n"
"    background-color: rgb(33, 33, "
                        "33);\n"
"    color: rgb(204, 204, 204);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(33, 33, 33);\n"
"    color: rgb(204, 204, 204);\n"
"    selection-background-color: rgb(0, 142, 246);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid rgb(204, 204, 204);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/resources/Icons/angle-down-solid.svg);\n"
"    width: 14px;\n"
"    height: 14px;\n"
"\n"
"}\n"
"/*the style of the  is generated mostly by chatgpt (3.5 version) */\n"
"QScrollBar:vertical {\n"
"	background: #333333;\n"
"	width: 15px;\n"
"	margin: 15px 0 15px 0;\n"
"\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"  	background: #666666;\n"
"	min-height: 30px;\n"
"\n"
"}\n"
"QScrollBar::sub-line:vertical:hover,QSc"
                        "rollBar::sub-line:vertical {\n"
"	background: #444444;\n"
"	height: 15px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-image: url(:/icons/resources/Icons/angle-up-solid.svg);\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"\n"
"}\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical {	background: #444444;\n"
"	height: 15px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	background: #444444;\n"
"	height: 15px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-image: url(:/icons/resources/Icons/angle-down-solid.svg);\n"
" 	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(DataBase)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filterSelecter = QComboBox(DataBase)
        self.filterSelecter.addItem("")
        self.filterSelecter.addItem("")
        self.filterSelecter.addItem("")
        self.filterSelecter.addItem("")
        self.filterSelecter.setObjectName(u"filterSelecter")
        self.filterSelecter.setFrame(True)

        self.horizontalLayout.addWidget(self.filterSelecter)

        self.fieldInput = QLineEdit(DataBase)
        self.fieldInput.setObjectName(u"fieldInput")
        self.fieldInput.setMinimumSize(QSize(0, 35))
        self.fieldInput.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(12)
        font.setKerning(False)
        self.fieldInput.setFont(font)
        self.fieldInput.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.fieldInput)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.resetButton = QPushButton(DataBase)
        self.resetButton.setObjectName(u"resetButton")
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.resetButton.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/resources/Icons/rotate-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resetButton.setIcon(icon)
        self.resetButton.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.resetButton)

        self.searchButton = QPushButton(DataBase)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/Icons/magnifying-glass-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.searchButton)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.deleteButton = QPushButton(DataBase)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/Icons/trash-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteButton.setIcon(icon2)
        self.deleteButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.deleteButton)

        self.selectAllCheckBox = QCheckBox(DataBase)
        self.selectAllCheckBox.setObjectName(u"selectAllCheckBox")
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(10)
        self.selectAllCheckBox.setFont(font2)

        self.horizontalLayout_2.addWidget(self.selectAllCheckBox)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.batchRegisterButton = QPushButton(DataBase)
        self.batchRegisterButton.setObjectName(u"batchRegisterButton")
        self.batchRegisterButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/Icons/users-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.batchRegisterButton.setIcon(icon3)
        self.batchRegisterButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.batchRegisterButton)

        self.registerIdButton = QPushButton(DataBase)
        self.registerIdButton.setObjectName(u"registerIdButton")
        self.registerIdButton.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/resources/Icons/user-plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.registerIdButton.setIcon(icon4)
        self.registerIdButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.registerIdButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.frame = QFrame(DataBase)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 766, 387))
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
        self.filterSelecter.setItemText(0, QCoreApplication.translate("DataBase", u"Name", None))
        self.filterSelecter.setItemText(1, QCoreApplication.translate("DataBase", u"Email", None))
        self.filterSelecter.setItemText(2, QCoreApplication.translate("DataBase", u"Phone", None))
        self.filterSelecter.setItemText(3, QCoreApplication.translate("DataBase", u"Address", None))

        self.filterSelecter.setPlaceholderText(QCoreApplication.translate("DataBase", u"Select Filter", None))
        self.resetButton.setText(QCoreApplication.translate("DataBase", u"Reset", None))
        self.searchButton.setText(QCoreApplication.translate("DataBase", u"Search", None))
        self.deleteButton.setText(QCoreApplication.translate("DataBase", u"Delete", None))
        self.selectAllCheckBox.setText(QCoreApplication.translate("DataBase", u"ALL", None))
        self.batchRegisterButton.setText(QCoreApplication.translate("DataBase", u"Batch Register", None))
        self.registerIdButton.setText(QCoreApplication.translate("DataBase", u"Register ID", None))
    # retranslateUi

