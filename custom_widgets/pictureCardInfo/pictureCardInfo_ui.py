# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pictureCardInfo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
from . import pictureCardInfo_rc

class Ui_PictureCardInfo(object):
    def setupUi(self, PictureCardInfo):
        if not PictureCardInfo.objectName():
            PictureCardInfo.setObjectName(u"PictureCardInfo")
        PictureCardInfo.resize(379, 166)
        PictureCardInfo.setMaximumSize(QSize(379, 166))
        self.horizontalLayout_2 = QHBoxLayout(PictureCardInfo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pictureLabel = QLabel(PictureCardInfo)
        self.pictureLabel.setObjectName(u"pictureLabel")
        self.pictureLabel.setMaximumSize(QSize(16777215, 167))
        self.pictureLabel.setPixmap(QPixmap(u":/image/resources/images/Person.jpg"))
        self.pictureLabel.setScaledContents(True)
        self.pictureLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.pictureLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sourceLabel = QLabel(PictureCardInfo)
        self.sourceLabel.setObjectName(u"sourceLabel")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(10)
        font.setBold(False)
        self.sourceLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.sourceLabel)

        self.dateLabel = QLabel(PictureCardInfo)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.dateLabel)

        self.sizeLabel = QLabel(PictureCardInfo)
        self.sizeLabel.setObjectName(u"sizeLabel")
        self.sizeLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.sizeLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sourceInfo = QLabel(PictureCardInfo)
        self.sourceInfo.setObjectName(u"sourceInfo")
        self.sourceInfo.setFont(font)

        self.verticalLayout_3.addWidget(self.sourceInfo)

        self.dateInfo = QLabel(PictureCardInfo)
        self.dateInfo.setObjectName(u"dateInfo")
        self.dateInfo.setFont(font)

        self.verticalLayout_3.addWidget(self.dateInfo)

        self.sizeInfo = QLabel(PictureCardInfo)
        self.sizeInfo.setObjectName(u"sizeInfo")
        self.sizeInfo.setFont(font)

        self.verticalLayout_3.addWidget(self.sizeInfo)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(PictureCardInfo)

        QMetaObject.connectSlotsByName(PictureCardInfo)
    # setupUi

    def retranslateUi(self, PictureCardInfo):
        PictureCardInfo.setWindowTitle(QCoreApplication.translate("PictureCardInfo", u"Form", None))
        self.pictureLabel.setText("")
        self.sourceLabel.setText(QCoreApplication.translate("PictureCardInfo", u"Source", None))
        self.dateLabel.setText(QCoreApplication.translate("PictureCardInfo", u"Date", None))
        self.sizeLabel.setText(QCoreApplication.translate("PictureCardInfo", u"Size", None))
        self.sourceInfo.setText(QCoreApplication.translate("PictureCardInfo", u"Unkown", None))
        self.dateInfo.setText(QCoreApplication.translate("PictureCardInfo", u"Unkown", None))
        self.sizeInfo.setText(QCoreApplication.translate("PictureCardInfo", u"Unkown", None))
    # retranslateUi

