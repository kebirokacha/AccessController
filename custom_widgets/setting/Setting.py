from PySide6.QtWidgets import  QWidget ,QTableWidgetItem ,QCheckBox
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtCore import Slot ,Signal 
from .FrameReadingThread import FrameReadingThread
from .RecognitionThread import RecognitionThread
from .Setting_ui import Ui_Setting

class Setting (Ui_Setting,QWidget):
	checkThreads = Signal()

	def __init__(self):
		super(Setting,self).__init__()
		self.setupUi(self)
		self.MAXRECOGNITIONWORKER = 5
		self.framReaderThreads:dict[str ,FrameReadingThread] = {}
		self.recognitionThreads:dict[str ,RecognitionThread] = {}
		self.loadCameras()

	def loadCameras(self):
		self.cameraTableWidget.clear()
		captures = QMediaDevices.videoInputs()
		#FIXME: Testing purpose (Remove Later)
		self.cameraTableWidget.setRowCount(len(captures)+3)
		# self.cameraTableWidget.setRowCount(len(captures))
		self.cameraTableWidget.setColumnCount(3)
		for row ,capture in enumerate(captures):
			captureId  = capture.id().data().decode()
			name = capture.description()
			self.cameraTableWidget.setItem(row ,0 ,QTableWidgetItem(captureId))
			self.cameraTableWidget.setItem(row ,1 ,QTableWidgetItem(name))
			checkbox = QCheckBox()
			checkbox.setDisabled(True)
			checkbox.stateChanged.connect(lambda state: self.startRecognition(captureId , state))
			self.cameraTableWidget.setCellWidget(row ,2 ,checkbox)
			# self.cameraTableWidget.hideColumn(0)
			
		#FIXME: Testing purpose (Remove Later)
		captureIP = 'http://192.168.1.3:8080/video'
		self.cameraTableWidget.setItem(row+1 ,0 ,QTableWidgetItem('http://192.168.1.3:8080/video'))
		self.cameraTableWidget.setItem(row+1 ,1 ,QTableWidgetItem('My Phone'))
		checkbox = QCheckBox()
		checkbox.setDisabled(True)
		checkbox.stateChanged.connect(lambda state: self.startRecognition('http://192.168.1.3:8080/video' , state))
		self.cameraTableWidget.setCellWidget(row+1 ,2 ,checkbox)
		# self.cameraTableWidget.hideColumn(0)

		captureIP = 'http://192.168.1.4:4747/video'
		self.cameraTableWidget.setItem(row+2 ,0 ,QTableWidgetItem('http://192.168.1.4:4747/video'))
		self.cameraTableWidget.setItem(row+2 ,1 ,QTableWidgetItem('Mother phone'))
		checkbox = QCheckBox()
		checkbox.setDisabled(True)
		checkbox.stateChanged.connect(lambda state: self.startRecognition('http://192.168.1.4:4747/video' , state))
		self.cameraTableWidget.setCellWidget(row+2 ,2 ,checkbox)
		# self.cameraTableWidget.hideColumn(0)

		captureIP = 'http://192.168.1.2:4747/video'
		self.cameraTableWidget.setItem(row+3 ,0 ,QTableWidgetItem('http://192.168.1.2:4747/video'))
		self.cameraTableWidget.setItem(row+3 ,1 ,QTableWidgetItem('Saadane phone'))
		checkbox = QCheckBox()
		checkbox.setDisabled(True)
		checkbox.stateChanged.connect(lambda state: self.startRecognition('http://192.168.1.2:4747/video' , state))
		self.cameraTableWidget.setCellWidget(row+3 ,2 ,checkbox)
		# self.cameraTableWidget.hideColumn(0)
  
	def loadPath(self):
		# Check the database for path if existe
		pass

	def startRecognition(self ,captureId ,state):
		totalCheckedBox = self.getTotalCheckedBox()
		if not state:
			print('unchecked')
			if captureId in self.recognitionThreads:
				self.recognitionThreads[captureId].killThread()
				del self.recognitionThreads[captureId] 
		elif totalCheckedBox < self.MAXRECOGNITIONWORKER :
			print('checked')
			if captureId not in self.recognitionThreads: 
				recognitonThread = RecognitionThread()
				if captureId in self.framReaderThreads:
					framReaderThread = self.framReaderThreads[captureId]
					framReaderThread.sendFrame.connect(recognitonThread.setFrame)
					framReaderThread.start()
					print(f'framReaderThread {framReaderThread} is started ')
				self.recognitionThreads[captureId] = recognitonThread
				recognitonThread.start()
				print(f'recognitonThread {recognitonThread} is started ')

		print(f'the framReaderThreads in Setting is {self.framReaderThreads}')
		print(f'the recognitionThreads in Setting is {self.recognitionThreads}')

	def getTotalCheckedBox(self) -> int:
		totalChecked = 0
		for row in range(self.cameraTableWidget.rowCount()):
			checkbox:QCheckBox = self.cameraTableWidget.cellWidget(row, 2)
			if checkbox.isChecked():
				totalChecked += 1
		return totalChecked
	
	def getCheckboxForCaptureId(self, captureId) ->QCheckBox:
		for row in range(self.cameraTableWidget.rowCount()):
			item = self.cameraTableWidget.item(row, 0)
			if item and item.text() == captureId:
				checkbox = self.cameraTableWidget.cellWidget(row, 2)
				return checkbox
		return None

	def killAllThreads(self):
		for framReadingThread in self.framReaderThreads.values():
			framReadingThread.killThread()
		for recognitionThread in self.recognitionThreads.values():
			recognitionThread.killThread()
	
	@Slot(str ,str)
	def startLive(self ,captureId ,captureName):
		if captureId not in self.framReaderThreads:
			frameReadingThread = FrameReadingThread(captureId ,captureName)
			self.framReaderThreads[captureId] = frameReadingThread
			self.checkThreads.emit()
			checkbox = self.getCheckboxForCaptureId(captureId)
			checkbox.setEnabled(True)
			checkbox.setChecked(True)
	
	@Slot(str)
	def killThreads(self ,captureId):
		#FIXME: reset the checkbox to default
		if captureId in self.framReaderThreads:
			checkbox = self.getCheckboxForCaptureId(captureId)
			checkbox.setChecked(False)
			checkbox.setDisabled(True)
			self.framReaderThreads[captureId].killThread()
			del self.framReaderThreads[captureId]
			print('framReaderThread was killed ')
		if captureId in self.recognitionThreads:
			self.recognitionThreads[captureId].killThread()
			del self.recognitionThreads[captureId]
			print('recognitionThread was killed ')
		print('KillThreads completed')
		