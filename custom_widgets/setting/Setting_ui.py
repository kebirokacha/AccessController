# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setting.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(800, 556)
        Setting.setStyleSheet(u"#Setting{\n"
"	background-color: rgb(43, 45, 53);\n"
"	\n"
"}\n"
"#Setting #frame{\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"#Setting QLabel {\n"
"	color:rgb(189, 189, 189);\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Setting)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Setting)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.faceRecognitionTab = QWidget()
        self.faceRecognitionTab.setObjectName(u"faceRecognitionTab")
        self.verticalLayout = QVBoxLayout(self.faceRecognitionTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.refreshButton = QPushButton(self.faceRecognitionTab)
        self.refreshButton.setObjectName(u"refreshButton")

        self.horizontalLayout.addWidget(self.refreshButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.cameraTableWidget = QTableWidget(self.faceRecognitionTab)
        if (self.cameraTableWidget.columnCount() < 2):
            self.cameraTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.cameraTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cameraTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.cameraTableWidget.setObjectName(u"cameraTableWidget")
        self.cameraTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.cameraTableWidget.horizontalHeader().setHighlightSections(True)
        self.cameraTableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.cameraTableWidget.horizontalHeader().setStretchLastSection(False)
        self.cameraTableWidget.verticalHeader().setVisible(True)
        self.cameraTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.cameraTableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.cameraTableWidget)

        self.tabWidget.addTab(self.faceRecognitionTab, "")
        self.recordsTab = QWidget()
        self.recordsTab.setObjectName(u"recordsTab")
        self.verticalLayout_3 = QVBoxLayout(self.recordsTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.recordsTab)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.path = QLabel(self.recordsTab)
        self.path.setObjectName(u"path")
        font = QFont()
        font.setBold(True)
        self.path.setFont(font)
        self.path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.path)

        self.selectPathButton = QPushButton(self.recordsTab)
        self.selectPathButton.setObjectName(u"selectPathButton")

        self.horizontalLayout_2.addWidget(self.selectPathButton)

        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.recordsTab, "")
        self.notificationTab = QWidget()
        self.notificationTab.setObjectName(u"notificationTab")
        self.verticalLayout_4 = QVBoxLayout(self.notificationTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.emailLabel = QLabel(self.notificationTab)
        self.emailLabel.setObjectName(u"emailLabel")

        self.horizontalLayout_3.addWidget(self.emailLabel)

        self.emailInput = QLineEdit(self.notificationTab)
        self.emailInput.setObjectName(u"emailInput")

        self.horizontalLayout_3.addWidget(self.emailInput)

        self.saveEmailButton = QPushButton(self.notificationTab)
        self.saveEmailButton.setObjectName(u"saveEmailButton")

        self.horizontalLayout_3.addWidget(self.saveEmailButton)

        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.dailyEmailCheckBox = QCheckBox(self.notificationTab)
        self.dailyEmailCheckBox.setObjectName(u"dailyEmailCheckBox")

        self.verticalLayout_4.addWidget(self.dailyEmailCheckBox)

        self.liveEmailCheckBox = QCheckBox(self.notificationTab)
        self.liveEmailCheckBox.setObjectName(u"liveEmailCheckBox")

        self.verticalLayout_4.addWidget(self.liveEmailCheckBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.notificationTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

#if QT_CONFIG(shortcut)
        self.emailLabel.setBuddy(self.emailInput)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Setting)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"Form", None))
        self.refreshButton.setText(QCoreApplication.translate("Setting", u"refresh", None))
        ___qtablewidgetitem = self.cameraTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Setting", u"Camera Name", None));
        ___qtablewidgetitem1 = self.cameraTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Setting", u"Selected", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.faceRecognitionTab), QCoreApplication.translate("Setting", u"Face Recognition", None))
        self.label.setText(QCoreApplication.translate("Setting", u"Default Folder :", None))
        self.path.setText(QCoreApplication.translate("Setting", u"Path", None))
        self.selectPathButton.setText(QCoreApplication.translate("Setting", u"select folder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recordsTab), QCoreApplication.translate("Setting", u"Records", None))
        self.emailLabel.setText(QCoreApplication.translate("Setting", u"Email", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("Setting", u"example@mail.com", None))
        self.saveEmailButton.setText(QCoreApplication.translate("Setting", u"Save", None))
        self.dailyEmailCheckBox.setText(QCoreApplication.translate("Setting", u"Daily Email", None))
        self.liveEmailCheckBox.setText(QCoreApplication.translate("Setting", u"Live Email", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notificationTab), QCoreApplication.translate("Setting", u"Notification", None))
    # retranslateUi

