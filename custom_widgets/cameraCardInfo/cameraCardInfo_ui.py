# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameraCardInfo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
from . import cameraCardInfo_rc

class Ui_CameraCardInfo(object):
    def setupUi(self, CameraCardInfo):
        if not CameraCardInfo.objectName():
            CameraCardInfo.setObjectName(u"CameraCardInfo")
        CameraCardInfo.resize(130, 40)
        CameraCardInfo.setMinimumSize(QSize(130, 40))
        CameraCardInfo.setMaximumSize(QSize(16777215, 40))
        CameraCardInfo.setStyleSheet(u"#CameraCardInfo {\n"
"	border:2px solid #EDECEC;\n"
"	border-radius:12px;\n"
"}\n"
"\n"
"#CameraCardInfo:hover {\n"
"	background-color: rgb(86, 125, 188);\n"
"\n"
"}\n"
"#cameraNameLabel{\n"
"	background-color: None;\n"
"}\n"
"#cameraIcon {\n"
"	border:None;\n"
"	background-color: None;\n"
"\n"
"}\n"
"#cameraIcon::hover {\n"
"	background-color: rgb(86, 125, 188);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(CameraCardInfo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cameraIcon = QPushButton(CameraCardInfo)
        self.cameraIcon.setObjectName(u"cameraIcon")
        self.cameraIcon.setMaximumSize(QSize(40, 16777215))
        icon = QIcon()
        icon.addFile(u":/resources/resources/Icons/video-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cameraIcon.setIcon(icon)

        self.horizontalLayout.addWidget(self.cameraIcon)

        self.cameraNameLabel = QLabel(CameraCardInfo)
        self.cameraNameLabel.setObjectName(u"cameraNameLabel")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(10)
        font.setBold(True)
        self.cameraNameLabel.setFont(font)

        self.horizontalLayout.addWidget(self.cameraNameLabel)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(CameraCardInfo)

        QMetaObject.connectSlotsByName(CameraCardInfo)
    # setupUi

    def retranslateUi(self, CameraCardInfo):
        CameraCardInfo.setWindowTitle(QCoreApplication.translate("CameraCardInfo", u"Form", None))
        self.cameraIcon.setText("")
        self.cameraNameLabel.setText(QCoreApplication.translate("CameraCardInfo", u"Camera Name", None))
    # retranslateUi

