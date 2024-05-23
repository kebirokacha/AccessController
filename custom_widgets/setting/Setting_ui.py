# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setting.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from . import setting_rc

class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(800, 556)
        Setting.setStyleSheet(u"#Setting{\n"
"	background-color: rgb(43, 45, 53);\n"
"	\n"
"}\n"
"#Setting QLabel ,QPushButton{\n"
"	color: rgb(189, 189, 189);\n"
"\n"
"}\n"
"#Setting QPushButton{\n"
"	border : 1px solid rgb(189, 189, 189);\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"\n"
"}\n"
"#Setting  QPushButton:hover{\n"
"	background-color: rgb(0, 142, 246);\n"
"\n"
"}\n"
"\n"
"#Setting QLabel ,QCheckBox{\n"
"	color:rgb(189, 189, 189);\n"
"\n"
"}\n"
"#emailInput{\n"
"	padding-left:5px;\n"
"	background-color:  rgb(33, 33, 33);\n"
"	border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 10px;\n"
"    color: rgb(204, 204, 204);\n"
"\n"
"}\n"
"QTableWidget {\n"
"        background-color: rgb(53, 53, 53);\n"
"        alternate-background-color: rgb(43, 45, 53);\n"
"        color: rgb(189, 189, 189);\n"
"        selection-background-color: rgb(0, 142, 246);\n"
"        selection-color: rgb(255, 255, 255);\n"
"        border: 1px solid  #D4D4D5;\n"
"    }\n"
"    \n"
"    QTableWidget::item {\n"
"        padding: 10px;\n"
"    }\n"
""
                        "    \n"
"    QTableWidget::item:selected {\n"
"        background-color: rgb(0, 142, 246);\n"
"        color: rgb(255, 255, 255);\n"
"    }\n"
"    \n"
"    QHeaderView::section {\n"
"        background-color: rgb(33, 33, 33);\n"
"        color: rgb(189, 189, 189);\n"
"        padding: 5px;\n"
"        \n"
"    }")
        self.horizontalLayout_5 = QHBoxLayout(Setting)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sideBare = QFrame(Setting)
        self.sideBare.setObjectName(u"sideBare")
        self.verticalLayout_2 = QVBoxLayout(self.sideBare)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.recognitionButton = QPushButton(self.sideBare)
        self.recognitionButton.setObjectName(u"recognitionButton")
        icon = QIcon()
        icon.addFile(u":/icons/resources/Icons/record-vinyl-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recognitionButton.setIcon(icon)

        self.verticalLayout_2.addWidget(self.recognitionButton)

        self.recordsButton = QPushButton(self.sideBare)
        self.recordsButton.setObjectName(u"recordsButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/Icons/photo-film-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recordsButton.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.recordsButton)

        self.notificationButton = QPushButton(self.sideBare)
        self.notificationButton.setObjectName(u"notificationButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/Icons/bell-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationButton.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.notificationButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.sideBare)

        self.mainFrame = QFrame(Setting)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.Shape.Box)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget = QStackedWidget(self.mainFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.recognitionStack = QWidget()
        self.recognitionStack.setObjectName(u"recognitionStack")
        self.verticalLayout = QVBoxLayout(self.recognitionStack)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.recognitionStack)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.refreshButton = QPushButton(self.recognitionStack)
        self.refreshButton.setObjectName(u"refreshButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/Icons/rotate-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.refreshButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.cameraTableWidget = QTableWidget(self.recognitionStack)
        if (self.cameraTableWidget.columnCount() < 3):
            self.cameraTableWidget.setColumnCount(3)
        self.cameraTableWidget.setObjectName(u"cameraTableWidget")
        self.cameraTableWidget.setFrameShape(QFrame.Shape.Box)
        self.cameraTableWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.cameraTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.cameraTableWidget.setShowGrid(True)
        self.cameraTableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.cameraTableWidget.setSortingEnabled(False)
        self.cameraTableWidget.setColumnCount(3)
        self.cameraTableWidget.verticalHeader().setVisible(False)
        self.cameraTableWidget.verticalHeader().setHighlightSections(True)

        self.verticalLayout.addWidget(self.cameraTableWidget)

        self.stackedWidget.addWidget(self.recognitionStack)
        self.recordsStrack = QWidget()
        self.recordsStrack.setObjectName(u"recordsStrack")
        self.verticalLayout_3 = QVBoxLayout(self.recordsStrack)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.recordsStrack)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.path = QLabel(self.recordsStrack)
        self.path.setObjectName(u"path")
        font1 = QFont()
        font1.setBold(True)
        self.path.setFont(font1)
        self.path.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.path)

        self.selectPathButton = QPushButton(self.recordsStrack)
        self.selectPathButton.setObjectName(u"selectPathButton")
        icon4 = QIcon()
        icon4.addFile(u":/icons/resources/Icons/folder-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.selectPathButton.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.selectPathButton)

        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.recordsStrack)
        self.notificationStack = QWidget()
        self.notificationStack.setObjectName(u"notificationStack")
        self.verticalLayout_4 = QVBoxLayout(self.notificationStack)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.emailLabel = QLabel(self.notificationStack)
        self.emailLabel.setObjectName(u"emailLabel")

        self.horizontalLayout_3.addWidget(self.emailLabel)

        self.emailInput = QLineEdit(self.notificationStack)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_3.addWidget(self.emailInput)

        self.saveEmailButton = QPushButton(self.notificationStack)
        self.saveEmailButton.setObjectName(u"saveEmailButton")
        icon5 = QIcon()
        icon5.addFile(u":/icons/resources/Icons/floppy-disk-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveEmailButton.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.saveEmailButton)

        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.liveEmailCheckBox = QCheckBox(self.notificationStack)
        self.liveEmailCheckBox.setObjectName(u"liveEmailCheckBox")

        self.verticalLayout_4.addWidget(self.liveEmailCheckBox)

        self.dailyEmailCheckBox = QCheckBox(self.notificationStack)
        self.dailyEmailCheckBox.setObjectName(u"dailyEmailCheckBox")

        self.verticalLayout_4.addWidget(self.dailyEmailCheckBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.notificationStack)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.mainFrame)


        self.retranslateUi(Setting)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"Form", None))
        self.recognitionButton.setText(QCoreApplication.translate("Setting", u"Recognition", None))
        self.recordsButton.setText(QCoreApplication.translate("Setting", u"Records", None))
        self.notificationButton.setText(QCoreApplication.translate("Setting", u"Notification", None))
        self.label_2.setText(QCoreApplication.translate("Setting", u"Available Cameras", None))
        self.refreshButton.setText(QCoreApplication.translate("Setting", u"refresh", None))
        self.label.setText(QCoreApplication.translate("Setting", u"Default Folder :", None))
        self.path.setText(QCoreApplication.translate("Setting", u"Path", None))
        self.selectPathButton.setText(QCoreApplication.translate("Setting", u"select folder", None))
        self.emailLabel.setText(QCoreApplication.translate("Setting", u"Ema&il", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("Setting", u"example@mail.com", None))
        self.saveEmailButton.setText(QCoreApplication.translate("Setting", u"Save", None))
        self.liveEmailCheckBox.setText(QCoreApplication.translate("Setting", u"Live Email", None))
        self.dailyEmailCheckBox.setText(QCoreApplication.translate("Setting", u"Daily Email", None))
    # retranslateUi

