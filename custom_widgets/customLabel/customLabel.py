from PySide6.QtWidgets import QLabel ,QListWidget
from PySide6.QtCore import Signal ,Slot 
from PySide6.QtGui import QPixmap , QImage
from ..camera.CameraWorker import  CameraWorker
from ..setting.Setting import Setting


class CustomLabel(QLabel):
	startWorker  = Signal()
	removeItem = Signal(str)
	cameraId = None
	cameraWorker = None

	def __init__(self ,text:str ,setting:Setting ,parent=None):
		super(CustomLabel ,self).__init__(parent)
		self.setting = setting
		self.cameraText = text
		self.setText(self.cameraText)
		self.setAcceptDrops(True)

	def dragEnterEvent(self, event):
		if event.mimeData().hasText():
			event.acceptProposedAction()

	def dragMoveEvent(self, event):
		if event.mimeData().hasText():
			event.acceptProposedAction()

	def dropEvent(self, event):
		if event.mimeData().hasText():
			info = event.mimeData().text()
			info = info.split(',')
			cameraId , cameraName = info[0] ,info[1]
			self.startCameraWorker(cameraId)
			event.acceptProposedAction()
			self.removeItem.emit(cameraName)
			

	def startCameraWorker(self, cameraId):
		print(f'starting camera with id:{cameraId}')
		self.cameraId = cameraId
		self.cameraWorker = CameraWorker(cameraId)
		self.cameraWorker.requestCapture.connect(self.setting.requestCapture)
		self.cameraWorker.updateFrame.connect(self.setImageLabel)
		self.cameraWorker.refreshCapture.connect(self.setting.refreshCapture)
		self.setting.sendCapture.connect(self.cameraWorker.reciveCapture)
		self.cameraWorker.start()

	def killWorker(self):
		if self.cameraWorker is not None and self.cameraWorker.isRunning():
			self.cameraWorker.killWorker()

	@Slot(QImage)
	def setImageLabel(self, image:QImage):
		self.setPixmap(QPixmap.fromImage(image))