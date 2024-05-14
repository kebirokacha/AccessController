from .cameraCardInfo_ui import Ui_CameraCardInfo
from PySide6.QtWidgets import QWidget ,QApplication 
from PySide6.QtCore import QMimeData, Qt
from PySide6.QtGui import QDrag ,QPixmap

class CameraCardInfo(Ui_CameraCardInfo ,QWidget):
	def __init__(self ,name:str ,captureId:int):
		super(Ui_CameraCardInfo ,self).__init__()
		self.setupUi(self)
		self.captureId = captureId
		self.cameraNameLabel.setText(name)
		self.setAcceptDrops(False) # Disable dropping on this widget

	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.drag_start_position = event.pos()

	def mouseMoveEvent(self, event):
		if not (event.buttons() & Qt.LeftButton):
			return
		if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
			return
		
		drag = QDrag(self)
		mimeData = QMimeData()

		mimeData.setData("captureId",f"{self.captureId}".encode())
		mimeData.setData("captureName",f"{self.cameraNameLabel.text()}".encode())

		pixmap = QPixmap(self.size())
		self.render(pixmap)
		drag.setPixmap(pixmap)
		drag.setMimeData(mimeData)
		drag.exec(Qt.MoveAction)
		print('item draged')