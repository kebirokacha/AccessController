# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PersonDetails.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QDateTimeEdit,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from . import personDetails_rc

class Ui_PersonDetails(object):
    def setupUi(self, PersonDetails):
        if not PersonDetails.objectName():
            PersonDetails.setObjectName(u"PersonDetails")
        PersonDetails.resize(1000, 590)
        PersonDetails.setMinimumSize(QSize(1000, 590))
        PersonDetails.setMaximumSize(QSize(1000, 590))
        PersonDetails.setStyleSheet(u"#PersonDetails{\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"QPushButton{\n"
"	border:2px solid rgb(189, 189, 189); \n"
"	border-radius:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	height:50px;\n"
"	font-size:20px\n"
"\n"
"}\n"
"#PersonDetails QPushButton:hover{\n"
"	background-color: rgb(28, 113, 216);\n"
"\n"
"}\n"
"QPushButton#cancelButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
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
"	color: rgb(255, 255, 255"
                        "); \n"
"	height: 50px; \n"
"	font-size: 20px; \n"
"}\n"
"\n"
"\n"
"QDateEdit::calendar-popup { \n"
"	border: 2px solid rgb(189, 189, 189); \n"
"	border-radius: 12px; \n"
"}\n"
"")
        self.gridLayout = QGridLayout(PersonDetails)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(PersonDetails)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.gridPictures = QGridLayout()
        self.gridPictures.setObjectName(u"gridPictures")

        self.gridLayout_3.addLayout(self.gridPictures, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.resetButton = QPushButton(PersonDetails)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(60, 0))
        icon = QIcon()
        icon.addFile(u":/icons/resources/Icons/rotate-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resetButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.resetButton)

        self.selectPicturesButton = QPushButton(PersonDetails)
        self.selectPicturesButton.setObjectName(u"selectPicturesButton")
        self.selectPicturesButton.setMinimumSize(QSize(60, 0))
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/Icons/circle-plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.selectPicturesButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.selectPicturesButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.nameLabel = QLabel(PersonDetails)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameInput = QLineEdit(PersonDetails)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setMaxLength(35)
        self.nameInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameInput)

        self.birthdayLabel = QLabel(PersonDetails)
        self.birthdayLabel.setObjectName(u"birthdayLabel")
        self.birthdayLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.birthdayLabel)

        self.birthdayInput = QDateEdit(PersonDetails)
        self.birthdayInput.setObjectName(u"birthdayInput")
        self.birthdayInput.setWrapping(False)
        self.birthdayInput.setFrame(True)
        self.birthdayInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.birthdayInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.birthdayInput.setCurrentSection(QDateTimeEdit.Section.DaySection)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.birthdayInput)

        self.phoneNumberLabel = QLabel(PersonDetails)
        self.phoneNumberLabel.setObjectName(u"phoneNumberLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.phoneNumberLabel)

        self.phoneNumberInput = QLineEdit(PersonDetails)
        self.phoneNumberInput.setObjectName(u"phoneNumberInput")
        self.phoneNumberInput.setMaxLength(13)
        self.phoneNumberInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.phoneNumberInput)

        self.emailLabel = QLabel(PersonDetails)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.emailLabel)

        self.emailInput = QLineEdit(PersonDetails)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setMaxLength(250)
        self.emailInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.emailInput)

        self.adresseLabel = QLabel(PersonDetails)
        self.adresseLabel.setObjectName(u"adresseLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.adresseLabel)

        self.adresseInput = QLineEdit(PersonDetails)
        self.adresseInput.setObjectName(u"adresseInput")
        self.adresseInput.setMaxLength(250)
        self.adresseInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.adresseInput)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelButton = QPushButton(PersonDetails)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.submitButton = QPushButton(PersonDetails)
        self.submitButton.setObjectName(u"submitButton")

        self.horizontalLayout.addWidget(self.submitButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 2)

        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.nameLabel.setBuddy(self.nameInput)
        self.birthdayLabel.setBuddy(self.birthdayInput)
        self.phoneNumberLabel.setBuddy(self.phoneNumberInput)
        self.emailLabel.setBuddy(self.emailInput)
        self.adresseLabel.setBuddy(self.adresseInput)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.birthdayInput, self.phoneNumberInput)
        QWidget.setTabOrder(self.phoneNumberInput, self.emailInput)
        QWidget.setTabOrder(self.emailInput, self.adresseInput)

        self.retranslateUi(PersonDetails)

        QMetaObject.connectSlotsByName(PersonDetails)
    # setupUi

    def retranslateUi(self, PersonDetails):
        PersonDetails.setWindowTitle(QCoreApplication.translate("PersonDetails", u"Form", None))
        self.resetButton.setText("")
        self.selectPicturesButton.setText("")
        self.nameLabel.setText(QCoreApplication.translate("PersonDetails", u"&Name", None))
        self.nameInput.setPlaceholderText(QCoreApplication.translate("PersonDetails", u"Name", None))
        self.birthdayLabel.setText(QCoreApplication.translate("PersonDetails", u"&Birthday", None))
        self.birthdayInput.setDisplayFormat(QCoreApplication.translate("PersonDetails", u"d/M/yyyy", None))
        self.phoneNumberLabel.setText(QCoreApplication.translate("PersonDetails", u"Phone", None))
        self.phoneNumberInput.setInputMask(QCoreApplication.translate("PersonDetails", u"+999999999999", None))
        self.phoneNumberInput.setText(QCoreApplication.translate("PersonDetails", u"+000000000000", None))
        self.phoneNumberInput.setPlaceholderText(QCoreApplication.translate("PersonDetails", u"+000000000000", None))
        self.emailLabel.setText(QCoreApplication.translate("PersonDetails", u"Ema&il", None))
        self.emailInput.setInputMask("")
        self.emailInput.setPlaceholderText(QCoreApplication.translate("PersonDetails", u"Email", None))
        self.adresseLabel.setText(QCoreApplication.translate("PersonDetails", u"&Adresse", None))
        self.adresseInput.setPlaceholderText(QCoreApplication.translate("PersonDetails", u"Adresse", None))
        self.cancelButton.setText(QCoreApplication.translate("PersonDetails", u"Cancel", None))
        self.submitButton.setText(QCoreApplication.translate("PersonDetails", u"Submit", None))
    # retranslateUi

