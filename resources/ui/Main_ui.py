# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(716, 661)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"QTabWidget::tab-bar {\n"
"	border: 30px solid rgb(0, 0, 255);\n"
"	color: rgb(189, 189, 189);\n"
"}\n"
"QTabBar > #titleTab{\n"
"	padding:20px;\n"
"}\n"
"\n"
"QTabBar{\n"
"	background-color: rgb(53, 53, 53);\n"
"	\n"
"}\n"
"QTabBar::tab { \n"
"	border-top-left-radius:12;\n"
"	border-top-right-radius:12;\n"
"  	padding: 10px;\n"
"	color :rgb(189, 189, 189);\n"
"	\n"
" }\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(0, 142, 246);\n"
"	text-decoration: none;\n"
" }\n"
"\n"
"QTabWidget::pane{\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"QTabWidget::pane {\n"
" border-top:2px solid rgb(0, 142, 246) ;\n"
"}\n"
"\n"
"#mainTab QPushButton{\n"
"	background-color: rgb(43, 45, 53);\n"
"	color: rgb(189, 189, 189);\n"
"    border: 1px solid rgb(189, 189, 189);\n"
"    border-radius: 12px; \n"
"    padding: 20px; \n"
"}\n"
"\n"
"#mainTab QPushButton::hover{\n"
"	background-color: rgb(0, 142, 246);\n"
"	color: rgb(189, 189, 189);\n"
"    border"
                        ": 1px solid rgb(189, 189, 189);\n"
"    border-radius: 12px; \n"
"    padding: 20px; \n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(30, 30))
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.titleTab = QWidget()
        self.titleTab.setObjectName(u"titleTab")
        self.tabWidget.addTab(self.titleTab, "")
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.gridLayout_2 = QGridLayout(self.mainTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.liveButton = QPushButton(self.mainTab)
        self.liveButton.setObjectName(u"liveButton")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/circle-dot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.liveButton.setIcon(icon)
        self.liveButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.liveButton)

        self.playBackButton = QPushButton(self.mainTab)
        self.playBackButton.setObjectName(u"playBackButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/Play-back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playBackButton.setIcon(icon1)
        self.playBackButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.playBackButton)

        self.dataBaseButton = QPushButton(self.mainTab)
        self.dataBaseButton.setObjectName(u"dataBaseButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/Data-Base.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBaseButton.setIcon(icon2)
        self.dataBaseButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.dataBaseButton)

        self.settingbutton = QPushButton(self.mainTab)
        self.settingbutton.setObjectName(u"settingbutton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingbutton.setIcon(icon3)
        self.settingbutton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.settingbutton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/Home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.mainTab, icon4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.titleTab), QCoreApplication.translate("MainWindow", u"Access Controler", None))
        self.liveButton.setText(QCoreApplication.translate("MainWindow", u"  Live", None))
        self.playBackButton.setText(QCoreApplication.translate("MainWindow", u"  PlayBack", None))
        self.dataBaseButton.setText(QCoreApplication.translate("MainWindow", u"  Data Base", None))
        self.settingbutton.setText(QCoreApplication.translate("MainWindow", u"parametre ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), QCoreApplication.translate("MainWindow", u"Main", None))
    # retranslateUi

