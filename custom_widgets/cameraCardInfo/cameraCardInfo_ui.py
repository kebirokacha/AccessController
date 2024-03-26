# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameraCardInfo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
from resources.ui import resources_rc

class Ui_CameraRow(object):
    def setupUi(self, CameraRow):
        if not CameraRow.objectName():
            CameraRow.setObjectName(u"CameraRow")
        CameraRow.resize(147, 40)
        CameraRow.setMinimumSize(QSize(0, 40))
        CameraRow.setMaximumSize(QSize(16777215, 40))
        CameraRow.setStyleSheet(u"#CameraRow {\n"
"	border:2px solid #EDECEC;\n"
"	border-radius:12px\n"
"}\n"
"\n"
"#cameraIcon {\n"
"	border:None;\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(CameraRow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cameraIcon = QPushButton(CameraRow)
        self.cameraIcon.setObjectName(u"cameraIcon")
        self.cameraIcon.setMaximumSize(QSize(40, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/video.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cameraIcon.setIcon(icon)

        self.horizontalLayout.addWidget(self.cameraIcon)

        self.cameraNameLabel = QLabel(CameraRow)
        self.cameraNameLabel.setObjectName(u"cameraNameLabel")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(10)
        font.setBold(True)
        self.cameraNameLabel.setFont(font)

        self.horizontalLayout.addWidget(self.cameraNameLabel)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(CameraRow)

        QMetaObject.connectSlotsByName(CameraRow)
    # setupUi

    def retranslateUi(self, CameraRow):
        CameraRow.setWindowTitle(QCoreApplication.translate("CameraRow", u"Form", None))
        self.cameraIcon.setText("")
        self.cameraNameLabel.setText(QCoreApplication.translate("CameraRow", u"Camera Name", None))
    # retranslateUi

