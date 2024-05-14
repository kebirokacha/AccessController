from PySide6.QtWidgets import QWidget ,QListWidgetItem
from PySide6.QtCore import Slot ,QUrl 
from PySide6.QtGui import QPixmap ,Qt
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer
from .records_ui import  Ui_Records
from ..videoCardInfo.videoCardInfo import VideoCardInfo
from ..pictureCardInfo.pictureCardInfo import PictureCardInfo
from databasemanager import DataBaseManager
import os

class Records(Ui_Records ,QWidget):
	def __init__(self):
		super(Records ,self).__init__()
		self.setupUi(self)
		self.rightSideBar.hide()
		self.initializeVideoPlayer()
		self.fillListWidgetWithVideos()
		self.toggleSideBarButton.clicked.connect(self.toggleSideBar)
		self.videoRadioButton.toggled.connect(self.setVideoPlayer)
		self.pictureRadioButton.toggled.connect(self.setPictureViewer)
		
	def setPosition(self, position):
		self.player.setPosition(position)

	def updateSlider(self, position):
		self.slider.setValue(position)

	def updateCurrentTimeLabel(self, position):
		self.currentTimeVideo.setText(self.getFormatTime(position))
		self.totalTimeVideo.setText(self.getFormatTime(self.player.duration()))
	
	def durationChanged(self, duration):
		self.slider.setRange(0, duration)
		self.totalTimeVideo.setText(self.getFormatTime(duration))

	def getFormatTime(self ,ms):
		seconds = ms // 1000
		minutes = seconds // 60
		hours = minutes // 60
		return f"{hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}"

	def initializeVideoPlayer(self):
		self.titleLabel.setText('Videos')
		self.player = QMediaPlayer()
		self.videoWidget = QVideoWidget()
		self.player.setVideoOutput(self.videoWidget)
		self.videoWidgetFramLayout.addWidget(self.videoWidget)
		self.listWidget.itemClicked.connect(lambda item :self.itemSelected(item))
		self.slider.setRange(0, 0)
		self.slider.sliderMoved.connect(self.setPosition)
		# Connect the player's positionChanged signal to update_slider
		self.player.positionChanged.connect(self.updateSlider)
		self.player.durationChanged.connect(self.durationChanged)
		self.player.positionChanged.connect(self.updateCurrentTimeLabel)

	def setVideoPlayer(self):
		self.titleLabel.setText('Videos')
		self.player.setSource(QUrl())
		self.player.play()
		self.stackedWidget.setCurrentIndex(0)
		self.fillListWidgetWithVideos()

	def setPictureViewer(self):
		self.titleLabel.setText('Pictures')
		self.currentTimeVideo.setText("00:00:00")
		self.totalTimeVideo.setText("00:00:00")
		size = self.pictureViewer.size()
		self.pictureViewer.setPixmap(
				QPixmap('resources/images/blackImage.jpg').scaled(size ,Qt.AspectRatioMode.KeepAspectRatio)
			)
		self.stackedWidget.setCurrentIndex(1)
		self.fillListWidgetWithPictures()


	@Slot()
	def fillListWidgetWithVideos(self):
		self.listWidget.clear()
		dataBaseManager = DataBaseManager()
		recordsFolderPath = dataBaseManager.getRecordsFolderPath()
		videoFolderPath = os.path.join(recordsFolderPath ,'videos')
		if not os.path.isdir(videoFolderPath):
			os.mkdir(videoFolderPath)
		videoFiles = [f for f in os.listdir(videoFolderPath) if f.endswith(('.mp4', '.avi', '.mkv'))]
		for videoFile in videoFiles:
			videoCardInfo = VideoCardInfo()
			videoCardInfo.refreshVideoList.connect(self.fillListWidgetWithVideos)
			videoCardInfo.setupCard({
					"videoFolderPath":videoFolderPath,
					"videoFile":videoFile,
				})
			listWidgetItem = QListWidgetItem(self.listWidget)
			listWidgetItem.setSizeHint(videoCardInfo.sizeHint())
			self.listWidget.addItem(listWidgetItem)
			self.listWidget.setItemWidget(listWidgetItem, videoCardInfo)

	@Slot()
	def fillListWidgetWithPictures(self):
		self.listWidget.clear()
		dataBaseManager = DataBaseManager()
		recordsFolderPath = dataBaseManager.getRecordsFolderPath()
		picturesFolderPath = os.path.join(recordsFolderPath ,'pictures')
		if not os.path.isdir(picturesFolderPath):
			os.mkdir(picturesFolderPath)
		pictureFiles = [f for f in os.listdir(picturesFolderPath) if f.endswith(('.jpg', '.jpeg'))]
		for pictureFile in pictureFiles:
			pictureCardInfo = PictureCardInfo()
			pictureCardInfo.refreshPicturesList.connect(self.fillListWidgetWithPictures)
			pictureCardInfo.setupCard({
					"pictureFolderPath":picturesFolderPath,
					"pictureFile":pictureFile,
				})
			listWidgetItem = QListWidgetItem(self.listWidget)
			listWidgetItem.setSizeHint(pictureCardInfo.sizeHint())
			self.listWidget.addItem(listWidgetItem)
			self.listWidget.setItemWidget(listWidgetItem, pictureCardInfo)


	def toggleSideBar(self):
		toggled = self.rightSideBar.property('toggled')
		if self.videoRadioButton.isChecked():
			self.fillListWidgetWithVideos()
		elif self.pictureRadioButton.isChecked():
			self.fillListWidgetWithPictures()
		if not toggled:
			self.showSideBar()
		else:
			self.hideSideBar()

	def hideSideBar(self):
		self.rightSideBar.setProperty('toggled' ,False)
		self.rightSideBar.hide()

	def showSideBar(self):
		self.rightSideBar.setProperty('toggled' ,True)
		self.rightSideBar.show()
		
		
	def itemSelected(self ,item:QListWidgetItem):
		itemWidget = self.listWidget.itemWidget(item)
		if isinstance(itemWidget ,VideoCardInfo):
			videoCardInfo:VideoCardInfo = self.listWidget.itemWidget(item)
			self.player.setSource(QUrl(videoCardInfo.videoFilePath))
			self.player.play()
		elif isinstance(itemWidget ,PictureCardInfo):
			pictureCardInfo:PictureCardInfo = self.listWidget.itemWidget(item)
			self.pictureViewer.setPixmap(QPixmap(pictureCardInfo.pictureFilePath))

