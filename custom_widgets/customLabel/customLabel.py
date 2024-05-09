from PySide6.QtWidgets import QLabel ,QMenu
from PySide6.QtCore import Signal ,Slot ,Qt 
from PySide6.QtGui import QPixmap , QImage ,QAction
from ..setting.Setting import Setting

class CustomLabel(QLabel):
	addItem = Signal(str ,str)
	removeItem = Signal(str)

	def __init__(self ,setting:Setting ,parent=None):
		super(CustomLabel ,self).__init__(parent)
		self.setting:Setting = setting
		self.setting.connectThread.connect(self.connectThread)
		self.setPixmap(QPixmap('resources/images/blackImage.jpg'))
		# self.setText('Loading')
		self.setScaledContents(True)
		self.setAcceptDrops(True)
		self.captureId:int = None
		self.captureName:str =None
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.showContextMenu)

	def dragEnterEvent(self, event):
		if event.mimeData().hasFormat("captureId") and event.mimeData().hasFormat("captureName"):
			event.acceptProposedAction()

	def dragMoveEvent(self, event):
		if event.mimeData().hasFormat("captureId") and event.mimeData().hasFormat("captureName"):
			event.acceptProposedAction()

	def dropEvent(self, event):
		print('item droped!!!')
		if event.mimeData().hasFormat("captureId") and event.mimeData().hasFormat("captureName"):
			captureId = event.mimeData().data("captureId").data().decode()
			self.captureId = int(captureId)
			self.captureName = event.mimeData().data("captureName").data().decode()
			self.setting.startLive(self.captureId ,self.captureName)
			self.removeItem.emit(self.captureName)
			self.setAcceptDrops(False)
			event.acceptProposedAction()

	def close(self):
		if self.captureId is not None:
			if self.captureId in self.setting.framReaderThreads:
				self.setting.framReaderThreads[self.captureId].updateFrame.disconnect(self.setImageLabel)
			self.setting.deleteFrameReadingThread(self.captureId)
			self.addItem.emit(self.captureName ,self.captureId)
			self.captureId = None
			self.captureName =None
			self.setAcceptDrops(True)
			self.setPixmap(QPixmap('resources/images/blackImage.jpg'))


		

	def showContextMenu(self ,position):
		menu = QMenu(self)
		action = QAction('End Live' ,self)
		action.triggered.connect(self.close)
		menu.addAction(action)
		menu.exec(self.mapToGlobal(position))
		
	@Slot()
	def connectThread(self):
		captures = self.setting.framReaderThreads
		if self.captureId is not None and self.captureId in captures:
			print(f'capture id in the custom label ha been connected  {self.captureId}')
			captures[self.captureId].updateFrame.connect(self.setImageLabel)

	@Slot(QImage)
	def setImageLabel(self, image:QImage):
		self.setPixmap(QPixmap.fromImage(image))