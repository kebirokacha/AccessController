# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoCardInfo.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from resources.ui import resources_rc

class Ui_VideoCardInfo(object):
    def setupUi(self, VideoCardInfo):
        if not VideoCardInfo.objectName():
            VideoCardInfo.setObjectName(u"VideoCardInfo")
        VideoCardInfo.resize(320, 120)
        VideoCardInfo.setMinimumSize(QSize(320, 120))
        VideoCardInfo.setStyleSheet(u"#videoIcon {\n"
"	background-color: rgb(0, 0, 0);\n"
"	padding: 7px;\n"
"	border: none;\n"
"	border-radius:12px\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(VideoCardInfo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.videoIcon = QPushButton(VideoCardInfo)
        self.videoIcon.setObjectName(u"videoIcon")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/video-green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.videoIcon.setIcon(icon)
        self.videoIcon.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.videoIcon)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sourceLabel = QLabel(VideoCardInfo)
        self.sourceLabel.setObjectName(u"sourceLabel")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(10)
        font.setBold(False)
        self.sourceLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.sourceLabel)

        self.dateLabel = QLabel(VideoCardInfo)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.dateLabel)

        self.timeLabel = QLabel(VideoCardInfo)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.timeLabel)

        self.sizeLabel = QLabel(VideoCardInfo)
        self.sizeLabel.setObjectName(u"sizeLabel")
        self.sizeLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.sizeLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sourceInfo = QLabel(VideoCardInfo)
        self.sourceInfo.setObjectName(u"sourceInfo")
        self.sourceInfo.setFont(font)

        self.verticalLayout_3.addWidget(self.sourceInfo)

        self.dateInfo = QLabel(VideoCardInfo)
        self.dateInfo.setObjectName(u"dateInfo")
        self.dateInfo.setFont(font)

        self.verticalLayout_3.addWidget(self.dateInfo)

        self.timeInfo = QLabel(VideoCardInfo)
        self.timeInfo.setObjectName(u"timeInfo")
        self.timeInfo.setFont(font)

        self.verticalLayout_3.addWidget(self.timeInfo)

        self.sizeInfo = QLabel(VideoCardInfo)
        self.sizeInfo.setObjectName(u"sizeInfo")
        self.sizeInfo.setFont(font)

        self.verticalLayout_3.addWidget(self.sizeInfo)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.line = QFrame(VideoCardInfo)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)


        self.retranslateUi(VideoCardInfo)

        QMetaObject.connectSlotsByName(VideoCardInfo)
    # setupUi

    def retranslateUi(self, VideoCardInfo):
        VideoCardInfo.setWindowTitle(QCoreApplication.translate("VideoCardInfo", u"Form", None))
        self.videoIcon.setText("")
        self.sourceLabel.setText(QCoreApplication.translate("VideoCardInfo", u"Source", None))
        self.dateLabel.setText(QCoreApplication.translate("VideoCardInfo", u"Date", None))
        self.timeLabel.setText(QCoreApplication.translate("VideoCardInfo", u"Time", None))
        self.sizeLabel.setText(QCoreApplication.translate("VideoCardInfo", u"Size", None))
        self.sourceInfo.setText(QCoreApplication.translate("VideoCardInfo", u"Unkown", None))
        self.dateInfo.setText(QCoreApplication.translate("VideoCardInfo", u"Unkown", None))
        self.timeInfo.setText(QCoreApplication.translate("VideoCardInfo", u"Unkown", None))
        self.sizeInfo.setText(QCoreApplication.translate("VideoCardInfo", u"Unkown", None))
    # retranslateUi

