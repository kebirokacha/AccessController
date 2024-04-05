from PySide6.QtWidgets import QWidget ,QListWidgetItem
from PySide6.QtCore import Slot
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer
from .records_ui import  Ui_Records
from ..videoCardInfo.videoCardInfo import VideoCardInfo
import os

class Records(Ui_Records ,QWidget):
	def __init__(self):
		super(Records ,self).__init__()
		self.setupUi(self)
		self.rightSideBar.setMinimumWidth(600)
		self.rightSideBar.hide()
		self.toggleSideBarButton.clicked.connect(self.toggleSideBar)
		self.player = QMediaPlayer()
		self.videoWidget = QVideoWidget()
		self.player.setVideoOutput(self.videoWidget)
		self.videoWidgetFramLayout.addWidget(self.videoWidget)
		self.listWidget.itemClicked.connect(lambda item :self.selectVideo(item))
		self.slider.setRange(0, 0)
		self.slider.sliderMoved.connect(self.set_position)
		# Connect the player's positionChanged signal to update_slider
		self.player.positionChanged.connect(self.update_slider)
		self.player.durationChanged.connect(self.duration_changed)
		self.player.positionChanged.connect(self.update_current_time_label)
		self.fillListWidget()
		

	def set_position(self, position):
		self.player.setPosition(position)

	def update_slider(self, position):
		self.slider.setValue(position)

	def duration_changed(self, duration):
		self.slider.setRange(0, duration)

	def update_current_time_label(self, position):
		self.currentTimeVideo.setText(self.format_time(position))
		self.totalTimeVideo.setText(self.format_time(self.player.duration()))
	
	def duration_changed(self, duration):
		self.slider.setRange(0, duration)
		self.totalTimeVideo.setText(self.format_time(duration))

	@staticmethod
	def format_time(ms):
		seconds = ms // 1000
		minutes = seconds // 60
		hours = minutes // 60
		return f"{hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}"

	@Slot()
	def fillListWidget(self):
		#FIXME: later you will get the path from setting or database
		self.listWidget.clear()
		videoFolderPath = "files_records/videos"
		videoFiles = [f for f in os.listdir(videoFolderPath) if f.endswith(('.mp4', '.avi', '.mkv'))]

		for videoFile in videoFiles:
			videoCardInfo = VideoCardInfo()
			videoCardInfo.refreshVideoList.connect(self.fillListWidget)
			videoCardInfo.setupCard({
					"videoFolderPath":videoFolderPath,
					"videoFile":videoFile,
				})
			listWidgetItem = QListWidgetItem(self.listWidget)
			listWidgetItem.setSizeHint(videoCardInfo.sizeHint())
			self.listWidget.addItem(listWidgetItem)
			self.listWidget.setItemWidget(listWidgetItem, videoCardInfo)

	def toggleSideBar(self):
		toggled = self.rightSideBar.property('toggled')
		if toggled:
			self.rightSideBar.setProperty('toggled' ,not toggled)
			self.rightSideBar.show()
		else:
			self.rightSideBar.setProperty('toggled' ,not toggled)
			self.rightSideBar.hide()
		
	def selectVideo(self ,item:QListWidgetItem):
		videoCardInfo = self.listWidget.itemWidget(item)
		self.player.setSource(videoCardInfo.videoFilePath)
		self.player.play()

