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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.resize(970, 674)
        self.gridLayout = QGridLayout(Camera)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(Camera)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.oneCamButton = QPushButton(self.frame_2)
        self.oneCamButton.setObjectName(u"oneCamButton")

        self.verticalLayout.addWidget(self.oneCamButton)

        self.twoCamButton = QPushButton(self.frame_2)
        self.twoCamButton.setObjectName(u"twoCamButton")

        self.verticalLayout.addWidget(self.twoCamButton)

        self.fourCamButton = QPushButton(self.frame_2)
        self.fourCamButton.setObjectName(u"fourCamButton")

        self.verticalLayout.addWidget(self.fourCamButton)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Camera)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cameraGrid = QGridLayout()
        self.cameraGrid.setObjectName(u"cameraGrid")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.cameraGrid.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_1 = QLabel(self.frame)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setTextFormat(Qt.AutoText)
        self.label_1.setScaledContents(False)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.cameraGrid.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.cameraGrid.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.cameraGrid.addWidget(self.label_4, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.cameraGrid, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Camera)

        QMetaObject.connectSlotsByName(Camera)
    # setupUi

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(QCoreApplication.translate("Camera", u"Form", None))
        self.oneCamButton.setText(QCoreApplication.translate("Camera", u"1 Camera", None))
        self.twoCamButton.setText(QCoreApplication.translate("Camera", u"2 Camera", None))
        self.fourCamButton.setText(QCoreApplication.translate("Camera", u"4 Camera", None))
        self.label_2.setText(QCoreApplication.translate("Camera", u"Loading Camrera", None))
        self.label_1.setText(QCoreApplication.translate("Camera", u"Loading Camrera", None))
        self.label_3.setText(QCoreApplication.translate("Camera", u"Loading Camrera", None))
        self.label_4.setText(QCoreApplication.translate("Camera", u"Loading Camrera", None))
    # retranslateUi

