# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'records.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QDateTimeEdit,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
from . import records_rc

class Ui_Records(object):
    def setupUi(self, Records):
        if not Records.objectName():
            Records.setObjectName(u"Records")
        Records.resize(1123, 446)
        Records.setMinimumSize(QSize(0, 0))
        Records.setStyleSheet(u"#Records{\n"
"	background-color: rgb(33, 33, 33);\n"
"\n"
"}\n"
"#Records QLabel{\n"
"	color: rgb(189, 189, 189);\n"
"\n"
"}\n"
"#Records >QFrame {\n"
"	border: 1px solid rgb(189, 189, 189);\n"
"}\n"
" #searchButton {\n"
"	background-color: rgb(0, 176, 251);\n"
"	border : None;\n"
"	border-radius:10px;\n"
"	padding:10px;\n"
"}\n"
"#frame QPushButton {\n"
"	background-color: rgb(43, 45, 53);\n"
"	color: rgb(189, 189, 189);\n"
"    border: 1px solid rgb(189, 189, 189);\n"
"    border-radius: 12px; \n"
"    padding: 10px; \n"
"\n"
"}\n"
"#frame QPushButton::hover {\n"
"	background-color: rgb(0, 142, 246);\n"
"\n"
"}\n"
"\n"
"QRadioButton{\n"
"	color: rgb(189, 189, 189);\n"
"\n"
"}\n"
"\n"
"#toggleSideBarButton{\n"
"	background-color: rgb(43, 45, 53);\n"
"	color: rgb(189, 189, 189);\n"
"    border: 1px solid rgb(189, 189, 189);\n"
"    border-radius: 12px; \n"
"\n"
"}\n"
"\n"
"#listWidget{\n"
"	background-color:  rgb(33, 33, 33);\n"
"	color: rgb(189, 189, 189);\n"
"	border: 1px solid rgb(189, 189, 189);\n"
"}\n"
""
                        "#listWidget::item:selected{\n"
"	background-color: rgb(78, 114, 171);\n"
"\n"
"}\n"
"#listWidget::item:hover{\n"
"	background-color: rgb(86, 125, 188);\n"
"\n"
"}\n"
"\n"
"/* Generated automatical with phind (don't care to understand what's it do becaus it look cool)*/\n"
"\n"
"QDateTimeEdit {\n"
"        background-color: rgb(43, 45, 53);\n"
"        color: rgb(189, 189, 189);\n"
"        border: 1px solid rgb(189, 189, 189);\n"
"        border-radius: 12px;\n"
"        padding: 10px;\n"
"        font-size: 14px;\n"
"    }\n"
"\n"
"    QDateTimeEdit::drop-down {\n"
"		 image: url(:/resources/resources/Icons/angle-down-solid.svg);\n"
"       	subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        width: 25px;\n"
"        border-left-width: 1px;\n"
"        border-left-color: rgb(189, 189, 189);\n"
"        border-left-style: solid;\n"
"        border-top-right-radius: 12px;\n"
"        border-bottom-right-radius: 12px;\n"
"        icon-size: 16px, 16px;\n"
"        padding: 5px;\n"
""
                        "    }\n"
"\n"
" QDateTimeEdit::hover {\n"
"        border: 1px solid rgb(0, 142, 246);\n"
"    }\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(Records)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.leftSideBare = QFrame(Records)
        self.leftSideBare.setObjectName(u"leftSideBare")
        self.leftSideBare.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftSideBare)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
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

        self.startDateLabel = QLabel(self.leftSideBare)
        self.startDateLabel.setObjectName(u"startDateLabel")

        self.verticalLayout_3.addWidget(self.startDateLabel)

        self.startDateInput = QDateTimeEdit(self.leftSideBare)
        self.startDateInput.setObjectName(u"startDateInput")
        self.startDateInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.startDateInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.startDateInput.setAccelerated(True)
        self.startDateInput.setProperty("showGroupSeparator", True)
        self.startDateInput.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.startDateInput)

        self.endDateLabel = QLabel(self.leftSideBare)
        self.endDateLabel.setObjectName(u"endDateLabel")

        self.verticalLayout_3.addWidget(self.endDateLabel)

        self.endDateInput = QDateTimeEdit(self.leftSideBare)
        self.endDateInput.setObjectName(u"endDateInput")
        self.endDateInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.endDateInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.endDateInput.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.endDateInput)

        self.verticalSpacer_2 = QSpacerItem(20, 348, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.searchButton = QPushButton(self.leftSideBare)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(0, 40))
        icon = QIcon()
        icon.addFile(u":/resources/resources/Icons/magnifying-glass-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon)

        self.verticalLayout_3.addWidget(self.searchButton)


        self.horizontalLayout_2.addWidget(self.leftSideBare)

        self.frame = QFrame(Records)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.videoPlayerPage = QWidget()
        self.videoPlayerPage.setObjectName(u"videoPlayerPage")
        self.verticalLayout_4 = QVBoxLayout(self.videoPlayerPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.videoWidgetFram = QFrame(self.videoPlayerPage)
        self.videoWidgetFram.setObjectName(u"videoWidgetFram")
        self.videoWidgetFram.setFrameShape(QFrame.Shape.StyledPanel)
        self.videoWidgetFram.setFrameShadow(QFrame.Shadow.Raised)
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
        self.slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_5.addWidget(self.slider)

        self.totalTimeVideo = QLabel(self.videoPlayerPage)
        self.totalTimeVideo.setObjectName(u"totalTimeVideo")

        self.horizontalLayout_5.addWidget(self.totalTimeVideo)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.playButton = QPushButton(self.videoPlayerPage)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMinimumSize(QSize(70, 40))
        self.playButton.setMaximumSize(QSize(120, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/resources/resources/Icons/play-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.playButton)

        self.stopButton = QPushButton(self.videoPlayerPage)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(70, 40))
        self.stopButton.setMaximumSize(QSize(120, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/resources/resources/Icons/stop-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon2)

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
        self.pictureViewer.setScaledContents(True)
        self.pictureViewer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.pictureViewer)

        self.stackedWidget.addWidget(self.picutreViewerPage)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame)

        self.toggleSideBarButton = QPushButton(Records)
        self.toggleSideBarButton.setObjectName(u"toggleSideBarButton")
        self.toggleSideBarButton.setMinimumSize(QSize(30, 65))
        self.toggleSideBarButton.setMaximumSize(QSize(30, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/resources/resources/Icons/angle-left-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleSideBarButton.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.toggleSideBarButton)

        self.rightSideBar = QFrame(Records)
        self.rightSideBar.setObjectName(u"rightSideBar")
        self.rightSideBar.setEnabled(True)
        self.rightSideBar.setMinimumSize(QSize(0, 0))
        self.rightSideBar.setMaximumSize(QSize(16777215, 16777215))
        self.rightSideBar.setFrameShadow(QFrame.Shadow.Raised)
        self.rightSideBar.setProperty("toggled", True)
        self.verticalLayout = QVBoxLayout(self.rightSideBar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.rightSideBar)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.listWidget = QListWidget(self.rightSideBar)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(True)
        self.listWidget.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)

        self.verticalLayout.addWidget(self.listWidget)


        self.horizontalLayout_2.addWidget(self.rightSideBar)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(3, 7)
        QWidget.setTabOrder(self.videoRadioButton, self.pictureRadioButton)
        QWidget.setTabOrder(self.pictureRadioButton, self.startDateInput)
        QWidget.setTabOrder(self.startDateInput, self.endDateInput)
        QWidget.setTabOrder(self.endDateInput, self.searchButton)

        self.retranslateUi(Records)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Records)
    # setupUi

    def retranslateUi(self, Records):
        Records.setWindowTitle(QCoreApplication.translate("Records", u"Form", None))
        self.videoRadioButton.setText(QCoreApplication.translate("Records", u"V&ideos", None))
        self.pictureRadioButton.setText(QCoreApplication.translate("Records", u"Pic&tures", None))
        self.startDateLabel.setText(QCoreApplication.translate("Records", u"Start Date", None))
        self.startDateInput.setDisplayFormat(QCoreApplication.translate("Records", u"M/d/yyyy   h:mm AP", None))
        self.endDateLabel.setText(QCoreApplication.translate("Records", u"End Date", None))
        self.endDateInput.setDisplayFormat(QCoreApplication.translate("Records", u"M/d/yyyy   h:mm AP", None))
        self.searchButton.setText(QCoreApplication.translate("Records", u"Search", None))
        self.currentTimeVideo.setText(QCoreApplication.translate("Records", u"00:00:00", None))
        self.totalTimeVideo.setText(QCoreApplication.translate("Records", u"00:00:00", None))
        self.playButton.setText(QCoreApplication.translate("Records", u"Play/Pause", None))
        self.stopButton.setText(QCoreApplication.translate("Records", u"Stop", None))
        self.pictureViewer.setText(QCoreApplication.translate("Records", u"TextLabel", None))
        self.toggleSideBarButton.setText("")
        self.titleLabel.setText(QCoreApplication.translate("Records", u"Title", None))
    # retranslateUi

