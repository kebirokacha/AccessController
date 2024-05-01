from PySide6.QtWidgets import QWidget ,QMessageBox ,QMenu
from PySide6.QtCore import Signal
from PySide6.QtGui import Qt ,QAction
from .VideoCardInfo_ui import Ui_VideoCardInfo
from PySide6.QtMultimedia import QMediaPlayer
import os
import time

class VideoCardInfo(Ui_VideoCardInfo ,QWidget):
	refreshVideoList = Signal()

	def __init__(self):
		super(VideoCardInfo ,self).__init__()
		self.setupUi(self)
		self.player = QMediaPlayer()
		self.player.durationChanged.connect(lambda duration : self.formatTime(duration))
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.showContextMenu)
		self.videoFilePath = None

	def setupCard(self ,info:dict):
		videoFilePath = os.path.join(info['videoFolderPath'], info['videoFile'])
		videoSizeInBytes = os.path.getsize(videoFilePath)
		videoSizeInMB = videoSizeInBytes / (1024 ** 2)
		videoCreationTime = time.ctime(os.path.getctime(videoFilePath))
		self.player.setSource(videoFilePath)
		videoDuration = self.formatTime(self.player.duration())
		self.sourceInfo.setText( info['videoFile'])
		self.sizeInfo.setText(str(videoSizeInMB))
		self.dateInfo.setText(videoCreationTime)
		self.timeInfo.setText(str(videoDuration))
		self.videoFilePath = videoFilePath
	
	def formatTime(self ,ms):
		seconds = ms // 1000
		minutes = seconds // 60
		hours = minutes // 60
		self.timeInfo.setText(f"{hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}")

	def showContextMenu(self ,position):
		menu = QMenu(self)
		action = QAction('Delete' ,self)
		action.triggered.connect(self.deleteVideo)
		menu.addAction(action)
		menu.exec(self.mapToGlobal(position))
	
	def deleteVideo(self):
		if os.path.exists(self.videoFilePath):
			reply = QMessageBox.question(self, 'Confirm Delete',
										f"Are you sure you want to delete the video at {self.videoFilePath}?", QMessageBox.Yes |
										QMessageBox.No, QMessageBox.No)

			if reply == QMessageBox.Yes:
				try:
					os.remove(self.videoFilePath)
					self.refreshVideoList.emit()
					print(f'Video {self.videoFilePath} deleted successfully.')
				except Exception as e:
					QMessageBox.critical(self, 'Error', f"Failed to delete the video: {e}")
			else:
				print(f'Deletion of video {self.videoFilePath} cancelled.')
		else:
			QMessageBox.warning(self, 'File Not Found', f"The video at {self.videoFilePath} does not exist.")
		