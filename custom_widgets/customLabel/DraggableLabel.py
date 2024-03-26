from PySide6.QtWidgets import QLabel ,QListWidget
from custom_widgets.camera.CameraWorker import  CameraWorker
from PySide6.QtCore import Signal ,Slot 
from PySide6.QtGui import QPixmap , QImage


class DraggableLabel(QLabel):
	startWorker  = Signal()
	removeItem = Signal(str)
	cameraId = None
	cameraWorker = None

	def __init__(self ,text :QListWidget ,parent=None):
		super(DraggableLabel ,self).__init__(parent)
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
		self.cameraWorker.updateFrame.connect(self.setImageLabel)
		self.cameraWorker.start()
	
	def updateRecognitionWorkerInfo(self):
		if self.cameraWorker is not None:
			self.cameraWorker.recognitionWorker

	def killWorker(self):
		if self.cameraWorker is not None and self.cameraWorker.isRunning():
			self.cameraWorker.killWorker()

	@Slot(QImage)
	def setImageLabel(self, image:QImage):
		self.setPixmap(QPixmap.fromImage(image))