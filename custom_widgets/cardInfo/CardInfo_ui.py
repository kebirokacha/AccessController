# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CardInfo.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from resources.qrcs import addPerson_rc

class Ui_CardInfo(object):
    def setupUi(self, CardInfo):
        if not CardInfo.objectName():
            CardInfo.setObjectName(u"CardInfo")
        CardInfo.resize(430, 280)
        CardInfo.setMinimumSize(QSize(430, 280))
        CardInfo.setMaximumSize(QSize(430, 280))
        CardInfo.setStyleSheet(u"#cardInfoFrame{\n"
"	border: 2px solid rgb(189, 189, 189);\n"
"	border-radius:12px;\n"
"\n"
"}\n"
"#editButton, #deleteButton {\n"
"	padding:5px;\n"
"	border:None;\n"
"}")
        self.gridLayout = QGridLayout(CardInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cardInfoFrame = QFrame(CardInfo)
        self.cardInfoFrame.setObjectName(u"cardInfoFrame")
        self.cardInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.cardInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.cardInfoFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imageLabel = QLabel(self.cardInfoFrame)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setMaximumSize(QSize(170, 210))
        self.imageLabel.setPixmap(QPixmap(u":/images/images/Person.jpg"))
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.imageLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nameLabel = QLabel(self.cardInfoFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(10)
        self.nameLabel.setFont(font)

        self.verticalLayout.addWidget(self.nameLabel)

        self.birthdayLabel = QLabel(self.cardInfoFrame)
        self.birthdayLabel.setObjectName(u"birthdayLabel")
        self.birthdayLabel.setFont(font)

        self.verticalLayout.addWidget(self.birthdayLabel)

        self.phoneLabel = QLabel(self.cardInfoFrame)
        self.phoneLabel.setObjectName(u"phoneLabel")
        self.phoneLabel.setFont(font)

        self.verticalLayout.addWidget(self.phoneLabel)

        self.emailLabel = QLabel(self.cardInfoFrame)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setFont(font)

        self.verticalLayout.addWidget(self.emailLabel)

        self.addressLabel = QLabel(self.cardInfoFrame)
        self.addressLabel.setObjectName(u"addressLabel")
        self.addressLabel.setFont(font)

        self.verticalLayout.addWidget(self.addressLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nameInfo = QLabel(self.cardInfoFrame)
        self.nameInfo.setObjectName(u"nameInfo")
        self.nameInfo.setFont(font)

        self.verticalLayout_2.addWidget(self.nameInfo)

        self.birthdayInfo = QLabel(self.cardInfoFrame)
        self.birthdayInfo.setObjectName(u"birthdayInfo")
        self.birthdayInfo.setFont(font)

        self.verticalLayout_2.addWidget(self.birthdayInfo)

        self.phoneInfo = QLabel(self.cardInfoFrame)
        self.phoneInfo.setObjectName(u"phoneInfo")
        self.phoneInfo.setFont(font)

        self.verticalLayout_2.addWidget(self.phoneInfo)

        self.emailInfo = QLabel(self.cardInfoFrame)
        self.emailInfo.setObjectName(u"emailInfo")
        self.emailInfo.setFont(font)

        self.verticalLayout_2.addWidget(self.emailInfo)

        self.addressInfo = QLabel(self.cardInfoFrame)
        self.addressInfo.setObjectName(u"addressInfo")
        self.addressInfo.setFont(font)

        self.verticalLayout_2.addWidget(self.addressInfo)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.status = QLabel(self.cardInfoFrame)
        self.status.setObjectName(u"status")
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setBold(True)
        self.status.setFont(font1)
        self.status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.status)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.editButton = QPushButton(self.cardInfoFrame)
        self.editButton.setObjectName(u"editButton")
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.editButton.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editButton.setIcon(icon)
        self.editButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.cardInfoFrame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.deleteButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.cardInfoFrame, 0, 0, 1, 1)


        self.retranslateUi(CardInfo)

        QMetaObject.connectSlotsByName(CardInfo)
    # setupUi

    def retranslateUi(self, CardInfo):
        CardInfo.setWindowTitle(QCoreApplication.translate("CardInfo", u"Form", None))
        self.imageLabel.setText("")
        self.nameLabel.setText(QCoreApplication.translate("CardInfo", u"Name", None))
        self.birthdayLabel.setText(QCoreApplication.translate("CardInfo", u"Birthday", None))
        self.phoneLabel.setText(QCoreApplication.translate("CardInfo", u"Phone", None))
        self.emailLabel.setText(QCoreApplication.translate("CardInfo", u"Email", None))
        self.addressLabel.setText(QCoreApplication.translate("CardInfo", u"Address", None))
        self.nameInfo.setText(QCoreApplication.translate("CardInfo", u"Unkown", None))
        self.birthdayInfo.setText(QCoreApplication.translate("CardInfo", u"Unkown", None))
        self.phoneInfo.setText(QCoreApplication.translate("CardInfo", u"Unkown", None))
        self.emailInfo.setText(QCoreApplication.translate("CardInfo", u"Unkown", None))
        self.addressInfo.setText(QCoreApplication.translate("CardInfo", u"Unkown", None))
        self.status.setText(QCoreApplication.translate("CardInfo", u"Status", None))
        self.editButton.setText("")
        self.deleteButton.setText("")
    # retranslateUi

