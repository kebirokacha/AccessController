from PySide6.QtWidgets import QWidget ,QMenu ,QMessageBox
from PySide6.QtGui import QAction ,QPixmap
from PySide6.QtCore import Qt  ,Signal
from .pictureCardInfo_ui import Ui_PictureCardInfo
import time
import os

class PictureCardInfo(Ui_PictureCardInfo ,QWidget):
	refreshPicturesList = Signal()

	def __init__(self):
		super(PictureCardInfo ,self).__init__()
		self.setupUi(self)
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.showContextMenu)
		self.pictureFilePath = None

	def setupCard(self ,info:dict):
		pictureFilePath = os.path.join(info['pictureFolderPath'], info['pictureFile'])
		pictureSizeInBytes = os.path.getsize(pictureFilePath)
		pictureSizeInMB = pictureSizeInBytes / (1024 ** 2)
		pictureCreationTime = time.ctime(os.path.getctime(pictureFilePath))
		self.sourceInfo.setText( info['pictureFile'])
		self.sizeInfo.setText(str(pictureSizeInMB))
		self.dateInfo.setText(pictureCreationTime)
		self.pictureFilePath = pictureFilePath
		self.pictureLabel.setPixmap(QPixmap(self.pictureFilePath))
	
	def showContextMenu(self ,position):
		menu = QMenu(self)
		action = QAction('Delete' ,self)
		action.triggered.connect(self.deleteVideo)
		menu.addAction(action)
		menu.exec(self.mapToGlobal(position))
	
	def deleteVideo(self):
		if os.path.exists(self.pictureFilePath):
			reply = QMessageBox.question(self, 'Confirm Delete',
										f"Are you sure you want to delete the video at {self.pictureFilePath}?", QMessageBox.Yes |
										QMessageBox.No, QMessageBox.No)

			if reply == QMessageBox.Yes:
				try:
					os.remove(self.pictureFilePath)
					self.refreshPicturesList.emit()
					print(f'Video {self.pictureFilePath} deleted successfully.')
				except Exception as e:
					QMessageBox.critical(self, 'Error', f"Failed to delete the video: {e}")
			else:
				print(f'Deletion of video {self.pictureFilePath} cancelled.')
		else:
			QMessageBox.warning(self, 'File Not Found', f"The video at {self.pictureFilePath} does not exist.")