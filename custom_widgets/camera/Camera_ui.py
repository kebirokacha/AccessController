# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Camera.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.resize(975, 560)
        Camera.setMinimumSize(QSize(975, 560))
        Camera.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(Camera)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.sideBar = QFrame(Camera)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setFrameShape(QFrame.StyledPanel)
        self.sideBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sideBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 6, 0, 6)
        self.label = QLabel(self.sideBar)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.cameraListWidget = QListWidget(self.sideBar)
        self.cameraListWidget.setObjectName(u"cameraListWidget")
        self.cameraListWidget.setMinimumSize(QSize(260, 0))
        self.cameraListWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cameraListWidget.setResizeMode(QListView.Adjust)
        self.cameraListWidget.setItemAlignment(Qt.AlignCenter|Qt.AlignHCenter|Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.cameraListWidget)


        self.horizontalLayout_2.addWidget(self.sideBar)

        self.frame = QFrame(Camera)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cameraGrid = QGridLayout()
        self.cameraGrid.setSpacing(10)
        self.cameraGrid.setObjectName(u"cameraGrid")

        self.verticalLayout_2.addLayout(self.cameraGrid)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.frame)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.retranslateUi(Camera)

        QMetaObject.connectSlotsByName(Camera)
    # setupUi

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(QCoreApplication.translate("Camera", u"Form", None))
        self.label.setText(QCoreApplication.translate("Camera", u"Camera availables", None))
        self.oneCamButton.setText(QCoreApplication.translate("Camera", u"1 Camera", None))
        self.twoCamButton.setText(QCoreApplication.translate("Camera", u"2 Camera", None))
        self.fourCamButton.setText(QCoreApplication.translate("Camera", u"4 Camera", None))
    # retranslateUi

