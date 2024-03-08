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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.resize(970, 674)
        self.gridLayout = QGridLayout(Camera)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Camera)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"\n"
"background-color: rgb(53, 53, 53);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_4.addWidget(self.label)

        self.FaceRecog = QCheckBox(self.frame)
        self.FaceRecog.setObjectName(u"FaceRecog")

        self.horizontalLayout_4.addWidget(self.FaceRecog)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addWidget(self.frame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cameraLabel_01 = QLabel(Camera)
        self.cameraLabel_01.setObjectName(u"cameraLabel_01")
        self.cameraLabel_01.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.cameraLabel_01.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.cameraLabel_01)

        self.verticalLayout.setStretch(0, 4)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cameraLabel_02 = QLabel(Camera)
        self.cameraLabel_02.setObjectName(u"cameraLabel_02")
        self.cameraLabel_02.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.cameraLabel_02.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.cameraLabel_02)

        self.verticalLayout_2.setStretch(0, 4)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Camera)

        QMetaObject.connectSlotsByName(Camera)
    # setupUi

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(QCoreApplication.translate("Camera", u"Form", None))
        self.label.setText(QCoreApplication.translate("Camera", u"Face recognition ", None))
        self.FaceRecog.setText("")
        self.cameraLabel_01.setText(QCoreApplication.translate("Camera", u"LOAD CAMERA 01", None))
        self.cameraLabel_02.setText(QCoreApplication.translate("Camera", u"LOAD CAMERA 02 ", None))
    # retranslateUi

