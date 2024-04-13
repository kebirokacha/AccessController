# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'records.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QDateTimeEdit,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
from resources.ui import resources_rc

class Ui_Records(object):
    def setupUi(self, Records):
        if not Records.objectName():
            Records.setObjectName(u"Records")
        Records.resize(1123, 385)
        Records.setMinimumSize(QSize(0, 0))
        Records.setStyleSheet(u" #searchButton {\n"
"	background-color: rgb(0, 176, 251);\n"
"	border : None;\n"
"	border-radius:12px\n"
"}\n"
"QPushButton {\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius:12px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(Records)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftSideBare = QFrame(Records)
        self.leftSideBare.setObjectName(u"leftSideBare")
        self.leftSideBare.setFrameShape(QFrame.StyledPanel)
        self.leftSideBare.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftSideBare)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.videoRadioButton = QRadioButton(self.leftSideBare)
        self.videoRadioButton.setObjectName(u"videoRadioButton")
        self.videoRadioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.videoRadioButton)

        self.pictureRadioButton = QRadioButton(self.leftSideBare)
        self.pictureRadioButton.setObjectName(u"pictureRadioButton")

        self.horizontalLayout_3.addWidget(self.pictureRadioButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.leftSideBare)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.dateTimeEdit = QDateTimeEdit(self.leftSideBare)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setAccelerated(True)
        self.dateTimeEdit.setProperty("showGroupSeparator", True)
        self.dateTimeEdit.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.dateTimeEdit)

        self.label_2 = QLabel(self.leftSideBare)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.dateTimeEdit_2 = QDateTimeEdit(self.leftSideBare)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEdit_2.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.dateTimeEdit_2)

        self.verticalSpacer_2 = QSpacerItem(20, 348, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.searchButton = QPushButton(self.leftSideBare)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.searchButton)


        self.horizontalLayout_2.addWidget(self.leftSideBare)

        self.frame = QFrame(Records)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.videoPlayerPage = QWidget()
        self.videoPlayerPage.setObjectName(u"videoPlayerPage")
        self.verticalLayout_4 = QVBoxLayout(self.videoPlayerPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.videoWidgetFram = QFrame(self.videoPlayerPage)
        self.videoWidgetFram.setObjectName(u"videoWidgetFram")
        self.videoWidgetFram.setFrameShape(QFrame.StyledPanel)
        self.videoWidgetFram.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.videoWidgetFram)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.videoWidgetFramLayout = QGridLayout()
        self.videoWidgetFramLayout.setSpacing(0)
        self.videoWidgetFramLayout.setObjectName(u"videoWidgetFramLayout")

        self.gridLayout.addLayout(self.videoWidgetFramLayout, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.videoWidgetFram)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.currentTimeVideo = QLabel(self.videoPlayerPage)
        self.currentTimeVideo.setObjectName(u"currentTimeVideo")

        self.horizontalLayout_5.addWidget(self.currentTimeVideo)

        self.slider = QSlider(self.videoPlayerPage)
        self.slider.setObjectName(u"slider")
        self.slider.setSingleStep(1)
        self.slider.setPageStep(20)
        self.slider.setTracking(True)
        self.slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.slider)

        self.totalTimeVideo = QLabel(self.videoPlayerPage)
        self.totalTimeVideo.setObjectName(u"totalTimeVideo")

        self.horizontalLayout_5.addWidget(self.totalTimeVideo)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.playButton = QPushButton(self.videoPlayerPage)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMinimumSize(QSize(70, 40))
        self.playButton.setMaximumSize(QSize(120, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.playButton)

        self.stopButton = QPushButton(self.videoPlayerPage)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(70, 40))
        self.stopButton.setMaximumSize(QSize(120, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.stopButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_4.setStretch(0, 1)
        self.stackedWidget.addWidget(self.videoPlayerPage)
        self.picutreViewerPage = QWidget()
        self.picutreViewerPage.setObjectName(u"picutreViewerPage")
        self.verticalLayout_5 = QVBoxLayout(self.picutreViewerPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pictureViewer = QLabel(self.picutreViewerPage)
        self.pictureViewer.setObjectName(u"pictureViewer")
        self.pictureViewer.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.pictureViewer)

        self.stackedWidget.addWidget(self.picutreViewerPage)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame)

        self.toggleSideBarButton = QPushButton(Records)
        self.toggleSideBarButton.setObjectName(u"toggleSideBarButton")
        self.toggleSideBarButton.setMinimumSize(QSize(30, 65))
        self.toggleSideBarButton.setMaximumSize(QSize(30, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/angle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleSideBarButton.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.toggleSideBarButton)

        self.rightSideBar = QFrame(Records)
        self.rightSideBar.setObjectName(u"rightSideBar")
        self.rightSideBar.setEnabled(True)
        self.rightSideBar.setMinimumSize(QSize(0, 0))
        self.rightSideBar.setMaximumSize(QSize(16777215, 16777215))
        self.rightSideBar.setFrameShape(QFrame.StyledPanel)
        self.rightSideBar.setFrameShadow(QFrame.Raised)
        self.rightSideBar.setProperty("toggled", True)
        self.verticalLayout = QVBoxLayout(self.rightSideBar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.rightSideBar)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.listWidget = QListWidget(self.rightSideBar)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(True)
        self.listWidget.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.verticalLayout.addWidget(self.listWidget)


        self.horizontalLayout_2.addWidget(self.rightSideBar)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        QWidget.setTabOrder(self.videoRadioButton, self.pictureRadioButton)
        QWidget.setTabOrder(self.pictureRadioButton, self.dateTimeEdit)
        QWidget.setTabOrder(self.dateTimeEdit, self.dateTimeEdit_2)
        QWidget.setTabOrder(self.dateTimeEdit_2, self.searchButton)

        self.retranslateUi(Records)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Records)
    # setupUi

    def retranslateUi(self, Records):
        Records.setWindowTitle(QCoreApplication.translate("Records", u"Form", None))
        self.videoRadioButton.setText(QCoreApplication.translate("Records", u"Videos", None))
        self.pictureRadioButton.setText(QCoreApplication.translate("Records", u"Pictures", None))
        self.label.setText(QCoreApplication.translate("Records", u"Start Date", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("Records", u"M/d/yyyy   h:mm AP", None))
        self.label_2.setText(QCoreApplication.translate("Records", u"End Date", None))
        self.dateTimeEdit_2.setDisplayFormat(QCoreApplication.translate("Records", u"M/d/yyyy   h:mm AP", None))
        self.searchButton.setText(QCoreApplication.translate("Records", u"Search", None))
        self.currentTimeVideo.setText(QCoreApplication.translate("Records", u"00:00:00", None))
        self.totalTimeVideo.setText(QCoreApplication.translate("Records", u"00:00:00", None))
        self.playButton.setText(QCoreApplication.translate("Records", u"Play/Pause", None))
        self.stopButton.setText(QCoreApplication.translate("Records", u"PushButton", None))
        self.pictureViewer.setText(QCoreApplication.translate("Records", u"TextLabel", None))
        self.toggleSideBarButton.setText("")
        self.title.setText(QCoreApplication.translate("Records", u"Title", None))
    # retranslateUi

