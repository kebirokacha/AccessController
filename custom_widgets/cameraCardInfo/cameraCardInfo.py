from .cameraCardInfo_ui import Ui_CameraRow
from PySide6.QtWidgets import QWidget ,QApplication 
from PySide6.QtCore import QMimeData, Qt
from PySide6.QtGui import QDrag ,QPixmap

class CameraCardInfo(Ui_CameraRow ,QWidget):
	def __init__(self ,name:str ,cameraId):
		super(Ui_CameraRow ,self).__init__()
		self.setupUi(self)
		self.cameraId = cameraId
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
		mime_data = QMimeData()
		mime_data.setText(f"{self.cameraId},{self.cameraNameLabel.text()}")
		drag.setMimeData(mime_data)
		pixmap = QPixmap(self.size())
		self.render(pixmap)
		drag.setPixmap(pixmap)
		drag.exec(Qt.MoveAction)