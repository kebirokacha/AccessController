from PySide6.QtWidgets import QLabel ,QMenu
from PySide6.QtCore import Signal ,Slot ,Qt 
from PySide6.QtGui import QPixmap , QImage ,QAction
from ..setting.Setting import Setting

class CustomLabel(QLabel):
	startLiveSignal  = Signal(str ,str)
	endLiveSignal  = Signal(str)
	addItem = Signal(str ,str)
	removeItem = Signal(str)

	def __init__(self ,setting:Setting ,parent=None):
		super(CustomLabel ,self).__init__(parent)
		self.setting = setting
		self.setting.connectThread.connect(self.connectThread)
		self.startLiveSignal.connect(self.setting.startLive)
		self.endLiveSignal.connect(self.setting.killThreads)
		self.setText('Loading')
		self.setScaledContents(True)
		self.setAcceptDrops(True)
		self.captureId = None
		self.captureName =None
		self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.customContextMenuRequested.connect(self.showContextMenu)

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
			self.captureId , self.captureName = info[0] ,info[1]
			self.startLiveSignal.emit(self.captureId ,self.captureName)
			event.acceptProposedAction()
			self.removeItem.emit(self.captureName)
			self.setAcceptDrops(False)

	def close(self):
		if self.captureId is not None:
			self.endLiveSignal.emit(self.captureId)
			self.setAcceptDrops(True)
			self.addItem.emit(self.captureName ,self.captureId)
			self.captureId = None
			self.captureName =None
		

	def showContextMenu(self ,position):
		menu = QMenu(self)
		action = QAction('End Live' ,self)
		action.triggered.connect(self.close)
		menu.addAction(action)
		menu.exec(self.mapToGlobal(position))

	@Slot()
	def resetCustomLabel(self):
		self.setText('Loading')
		self.repaint()
		
	@Slot()
	def connectThread(self):
		captures = self.setting.framReaderThreads
		if self.captureId is not None and self.captureId in captures:
			print(f'capture id in the custom label ha been connected  {self.captureId}')
			captures[self.captureId].updateFrame.connect(self.setImageLabel)
			captures[self.captureId].resetCustomLabel.connect(self.resetCustomLabel)

	@Slot(QImage)
	def setImageLabel(self, image:QImage):
		self.setPixmap(QPixmap.fromImage(image))