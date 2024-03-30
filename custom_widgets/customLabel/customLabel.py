from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal ,Slot 
from PySide6.QtGui import QPixmap , QImage
from ..setting.Setting import Setting


class CustomLabel(QLabel):
	startLiveSignal  = Signal(str)
	endLiveSignal  = Signal(str)
	removeItem = Signal(str)
	captureId = None
	cameraWorker = None

	def __init__(self ,text:str ,setting:Setting ,parent=None):
		super(CustomLabel ,self).__init__(parent)
		self.setting = setting
		self.setting.checkThreads.connect(self.connectThread)
		self.startLiveSignal.connect(self.setting.startLive)
		self.endLiveSignal.connect(self.setting.killThreads)
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
			captureId , cameraName = info[0] ,info[1]
			self.startLive(captureId)
			event.acceptProposedAction()
			self.removeItem.emit(cameraName)
			self.setAcceptDrops(False)

	def startLive(self, captureId):
		print(f'starting camera with id:{captureId}')
		self.captureId = captureId
		self.startLiveSignal.emit(self.captureId)
		
	def close(self):
		if self.captureId is not None:
			self.endLiveSignal.emit(self.captureId)
		
	@Slot()
	def connectThread(self):
		captures = self.setting.framReaderThreads
		if self.captureId is not None and self.captureId in captures:
			print(f' capture id in the custom label{self.captureId}')
			captures[self.captureId].updateFrame.connect(self.setImageLabel)

	@Slot(QImage)
	def setImageLabel(self, image:QImage):
		self.setPixmap(QPixmap.fromImage(image))