# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Live.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from . import live_rc

class Ui_Live(object):
    def setupUi(self, Live):
        if not Live.objectName():
            Live.setObjectName(u"Live")
        Live.resize(975, 560)
        Live.setMinimumSize(QSize(975, 560))
        Live.setStyleSheet(u"#Live{\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"#Live QLabel{\n"
"	\n"
"	color: rgb(189, 189, 189);\n"
"}\n"
"#Live > QFrame{\n"
"	/*background-color:  rgb(43, 45, 53);*/\n"
"	border: 1px solid rgb(189, 189, 189);\n"
"}\n"
"\n"
"#cameraListWidget{\n"
"	background-color:  rgb(33, 33, 33);\n"
"	color: rgb(189, 189, 189);\n"
"	border: 1px solid rgb(189, 189, 189);\n"
"}\n"
"#cameraListWidget::item:selected{\n"
"	background-color: rgb(78, 114, 171);\n"
"\n"
"}\n"
"#cameraListWidget::item:hover{\n"
"	background-color: rgb(86, 125, 188);\n"
"\n"
"}\n"
"#Live  QPushButton{\n"
"	background-color: rgb(43, 45, 53);\n"
"	color: rgb(189, 189, 189);\n"
"    border: 1px solid rgb(189, 189, 189);\n"
"    border-radius: 12px; \n"
"    padding: 10px; \n"
"}\n"
"\n"
"#Live QPushButton::hover{\n"
"	background-color: rgb(0, 142, 246);\n"
"   \n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(Live)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.sideBar = QFrame(Live)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setFrameShadow(QFrame.Shadow.Raised)
        self.sideBar.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.sideBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 6, 5, 6)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.sideBar)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.refreshCapturesButton = QPushButton(self.sideBar)
        self.refreshCapturesButton.setObjectName(u"refreshCapturesButton")
        icon = QIcon()
        icon.addFile(u":/live_resources/resources/Icons/rotate-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshCapturesButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.refreshCapturesButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.cameraListWidget = QListWidget(self.sideBar)
        self.cameraListWidget.setObjectName(u"cameraListWidget")
        self.cameraListWidget.setMinimumSize(QSize(260, 0))
        self.cameraListWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.cameraListWidget.setResizeMode(QListView.ResizeMode.Adjust)
        self.cameraListWidget.setItemAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.cameraListWidget)


        self.horizontalLayout_2.addWidget(self.sideBar)

        self.frame = QFrame(Live)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.cameraGrid = QGridLayout()
        self.cameraGrid.setSpacing(5)
        self.cameraGrid.setObjectName(u"cameraGrid")

        self.verticalLayout_2.addLayout(self.cameraGrid)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.oneCamButton = QPushButton(self.frame)
        self.oneCamButton.setObjectName(u"oneCamButton")

        self.horizontalLayout.addWidget(self.oneCamButton)

        self.twoCamButton = QPushButton(self.frame)
        self.twoCamButton.setObjectName(u"twoCamButton")

        self.horizontalLayout.addWidget(self.twoCamButton)

        self.fourCamButton = QPushButton(self.frame)
        self.fourCamButton.setObjectName(u"fourCamButton")

        self.horizontalLayout.addWidget(self.fourCamButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 4)

        self.horizontalLayout_2.addWidget(self.frame)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.retranslateUi(Live)

        QMetaObject.connectSlotsByName(Live)
    # setupUi

    def retranslateUi(self, Live):
        Live.setWindowTitle(QCoreApplication.translate("Live", u"Form", None))
        self.label.setText(QCoreApplication.translate("Live", u"Camera availables", None))
        self.refreshCapturesButton.setText(QCoreApplication.translate("Live", u"refresh", None))
        self.oneCamButton.setText(QCoreApplication.translate("Live", u"1 Camera", None))
        self.twoCamButton.setText(QCoreApplication.translate("Live", u"2 Camera", None))
        self.fourCamButton.setText(QCoreApplication.translate("Live", u"4 Camera", None))
    # retranslateUi

