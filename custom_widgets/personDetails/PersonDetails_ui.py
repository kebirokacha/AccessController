# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PersonDetails.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from resources.qrcs import addPerson_rc

class Ui_PersonDetails(object):
    def setupUi(self, PersonDetails):
        if not PersonDetails.objectName():
            PersonDetails.setObjectName(u"PersonDetails")
        PersonDetails.resize(600, 500)
        PersonDetails.setMinimumSize(QSize(600, 500))
        PersonDetails.setMaximumSize(QSize(600, 500))
        PersonDetails.setStyleSheet(u"QWidget#PersonDetails{\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton{\n"
"	border:2px solid rgb(189, 189, 189); \n"
"	border-radius:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	height:50px;\n"
"	font-size:20px\n"
"}\n"
"QPushButton#addButton{\n"
"	background-color: rgb(28, 113, 216);\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(33, 33, 33);\n"
"	border:2px solid rgb(189, 189, 189); \n"
"	border-radius:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	height:50px;\n"
"	font-size:20px\n"
"}\n"
"QLabel#person_picture{\n"
"	border:2px solid rgb(189, 189, 189); \n"
"	border-radius:12px;\n"
"	padding:5px\n"
"}\n"
"\n"
"QLabel { \n"
"	background-color: rgb(33, 33, 33);\n"
"	color: rgb(255, 255, 255); \n"
"	height: 50px; \n"
"	font-size: 20px; \n"
"}\n"
"\n"
"QDateEdit { \n"
"	background-color: rgb(33, 33, 33);\n"
"	border: 2px solid rgb(189, 189, 189); \n"
"	border-radius: 12px; \n"
"	color: rgb(255, 255, 255); \n"
"	height: 50px; \n"
"	font-size: 20px; \n"
"}\n"
"\n"
"QDateEdit::up-button, QDateEdit::down-"
                        "button { \n"
"	subcontrol-origin: border; \n"
"	subcontrol-position: right center; \n"
"	width: 20px; \n"
"	border: none; \n"
"	background: transparent; \n"
"}\n"
"\n"
"QDateEdit::up-arrow, QDateEdit::down-arrow { \n"
"	width: 10px; \n"
"	height: 10px; \n"
"	image: url(arrow.png); \n"
"}\n"
"\n"
"QDateEdit::up-arrow { \n"
"	top: -5px; \n"
"	transform: rotate(90deg); \n"
"}\n"
"\n"
"QDateEdit::down-arrow { \n"
"	bottom: -5px; \n"
"	transform: rotate(-90deg); \n"
"}\n"
"\n"
"QDateEdit::calendar-popup { \n"
"	border: 2px solid rgb(189, 189, 189); \n"
"	border-radius: 12px; \n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(PersonDetails)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.personPictureLabel = QLabel(PersonDetails)
        self.personPictureLabel.setObjectName(u"personPictureLabel")
        self.personPictureLabel.setPixmap(QPixmap(u":/images/images/Person.jpg"))
        self.personPictureLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.personPictureLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.nameLabel = QLabel(PersonDetails)
        self.nameLabel.setObjectName(u"nameLabel")

        self.horizontalLayout_5.addWidget(self.nameLabel)

        self.nameInput = QLineEdit(PersonDetails)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.nameInput)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.birthdayLabel = QLabel(PersonDetails)
        self.birthdayLabel.setObjectName(u"birthdayLabel")
        self.birthdayLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.birthdayLabel)

        self.birthdayInput = QDateEdit(PersonDetails)
        self.birthdayInput.setObjectName(u"birthdayInput")
        self.birthdayInput.setAlignment(Qt.AlignCenter)
        self.birthdayInput.setCurrentSection(QDateTimeEdit.DaySection)

        self.horizontalLayout_2.addWidget(self.birthdayInput)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.phoneNumberLabel = QLabel(PersonDetails)
        self.phoneNumberLabel.setObjectName(u"phoneNumberLabel")

        self.horizontalLayout_6.addWidget(self.phoneNumberLabel)

        self.phoneNumberInput = QLineEdit(PersonDetails)
        self.phoneNumberInput.setObjectName(u"phoneNumberInput")
        self.phoneNumberInput.setMaxLength(32767)
        self.phoneNumberInput.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.phoneNumberInput)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.emailLabel = QLabel(PersonDetails)
        self.emailLabel.setObjectName(u"emailLabel")

        self.horizontalLayout_7.addWidget(self.emailLabel)

        self.emailInput = QLineEdit(PersonDetails)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.emailInput)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.adresseLabel = QLabel(PersonDetails)
        self.adresseLabel.setObjectName(u"adresseLabel")

        self.horizontalLayout_8.addWidget(self.adresseLabel)

        self.adresseInput = QLineEdit(PersonDetails)
        self.adresseInput.setObjectName(u"adresseInput")
        self.adresseInput.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.adresseInput)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.selectImageButton = QPushButton(PersonDetails)
        self.selectImageButton.setObjectName(u"selectImageButton")

        self.verticalLayout.addWidget(self.selectImageButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(PersonDetails)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)

        self.cancelButton = QPushButton(PersonDetails)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

#if QT_CONFIG(shortcut)
        self.nameLabel.setBuddy(self.nameInput)
        self.birthdayLabel.setBuddy(self.birthdayInput)
        self.phoneNumberLabel.setBuddy(self.phoneNumberInput)
        self.emailLabel.setBuddy(self.emailInput)
        self.adresseLabel.setBuddy(self.adresseInput)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.nameInput, self.birthdayInput)
        QWidget.setTabOrder(self.birthdayInput, self.phoneNumberInput)
        QWidget.setTabOrder(self.phoneNumberInput, self.emailInput)
        QWidget.setTabOrder(self.emailInput, self.adresseInput)
        QWidget.setTabOrder(self.adresseInput, self.selectImageButton)
        QWidget.setTabOrder(self.selectImageButton, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)

        self.retranslateUi(PersonDetails)

        QMetaObject.connectSlotsByName(PersonDetails)
    # setupUi

    def retranslateUi(self, PersonDetails):
        PersonDetails.setWindowTitle(QCoreApplication.translate("PersonDetails", u"Form", None))
        self.personPictureLabel.setText("")
        self.nameLabel.setText(QCoreApplication.translate("PersonDetails", u"Name", None))
        self.nameInput.setPlaceholderText(QCoreApplication.translate("PersonDetails", u"Name", None))
        self.birthdayLabel.setText(QCoreApplication.translate("PersonDetails", u"Birthday", None))
        self.birthdayInput.setDisplayFormat(QCoreApplication.translate("PersonDetails", u"d/M/yyyy", None))
        self.phoneNumberLabel.setText(QCoreApplication.translate("PersonDetails", u"Phone", None))
        self.phoneNumberInput.setInputMask("")
        self.phoneNumberInput.setPlaceholderText(QCoreApplication.translate("PersonDetails", u"+000000000000", None))
        self.emailLabel.setText(QCoreApplication.translate("PersonDetails", u"Email", None))
        self.emailInput.setInputMask("")
        self.emailInput.setPlaceholderText(QCoreApplication.translate("PersonDetails", u"Email", None))
        self.adresseLabel.setText(QCoreApplication.translate("PersonDetails", u"Adresse", None))
        self.adresseInput.setPlaceholderText(QCoreApplication.translate("PersonDetails", u"Adresse", None))
        self.selectImageButton.setText(QCoreApplication.translate("PersonDetails", u"Select Image", None))
        self.addButton.setText(QCoreApplication.translate("PersonDetails", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("PersonDetails", u"Cancel", None))
    # retranslateUi

