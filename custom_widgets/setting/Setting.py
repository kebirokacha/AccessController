from PySide6.QtWidgets import  QWidget ,QTableWidgetItem ,QCheckBox ,QFileDialog
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtCore import Slot ,Signal ,QStandardPaths
from .FrameReadingThread import FrameReadingThread
from databasemanager import DataBaseManager
from .Setting_ui import Ui_Setting
from .sendEmailClass import Emailsender


class Setting (Ui_Setting,QWidget):
	connectThread = Signal()
	updateRecordsFolderPath = Signal()

	def __init__(self):
		super(Setting ,self).__init__()
		self.setupUi(self)
		self.MAXRECOGNITIONWORKER = 2
		self.framReaderThreads:dict[str ,FrameReadingThread] = {}
		self.dataBaseManager = DataBaseManager()
		self.path.setText(self.dataBaseManager.getRecordsFolderPath())
		self.selectPathButton.clicked.connect(self.selectFolder)
		self.loadCameras()

	def loadCameras(self):
		self.cameraTableWidget.clear()
		captures = QMediaDevices.videoInputs()
		#FIXME: Testing purpose (Remove Later)
		self.cameraTableWidget.setRowCount(len(captures)+3)
		# self.cameraTableWidget.setRowCount(len(captures))
		self.cameraTableWidget.setColumnCount(3)
		for row ,capture in enumerate(captures):
			captureId  = row
			name = capture.description()
			self.cameraTableWidget.setItem(row ,0 ,QTableWidgetItem(captureId))
			self.cameraTableWidget.setItem(row ,1 ,QTableWidgetItem(name))
			checkbox = QCheckBox()
			checkbox.setDisabled(True)
			checkbox.stateChanged.connect(lambda state: self.toggleRecognition(captureId , state))
			self.cameraTableWidget.setCellWidget(row ,2 ,checkbox)
			# self.cameraTableWidget.hideColumn(0)
			
		#FIXME: Testing purpose (Remove Later)
		# captureIP = 'http://192.168.1.3:8080/video'
		# self.cameraTableWidget.setItem(row+1 ,0 ,QTableWidgetItem('http://192.168.179.10:4747/video'))
		# self.cameraTableWidget.setItem(row+1 ,1 ,QTableWidgetItem('My Phone'))
		# checkbox = QCheckBox()
		# checkbox.setDisabled(True)
		# checkbox.stateChanged.connect(lambda state: self.toggleRecognition('http://192.168.179.10:4747/video' , state))
		# self.cameraTableWidget.setCellWidget(row+1 ,2 ,checkbox)

		# captureIP = 'http://192.168.1.4:4747/video'
		# self.cameraTableWidget.setItem(row+2 ,0 ,QTableWidgetItem('http://192.168.1.4:4747/video'))
		# self.cameraTableWidget.setItem(row+2 ,1 ,QTableWidgetItem('Mother phone'))
		# checkbox = QCheckBox()
		# checkbox.setDisabled(True)
		# checkbox.stateChanged.connect(lambda state: self.toggleRecognition('http://192.168.1.4:4747/video' , state))
		# self.cameraTableWidget.setCellWidget(row+2 ,2 ,checkbox)

		# captureIP = 'http://192.168.1.2:4747/video'
		# self.cameraTableWidget.setItem(row+3 ,0 ,QTableWidgetItem('http://192.168.42.129:4747/video'))
		# self.cameraTableWidget.setItem(row+3 ,1 ,QTableWidgetItem('Saadane phone'))
		# checkbox = QCheckBox()
		# checkbox.setDisabled(True)
		# checkbox.stateChanged.connect(lambda state: self.toggleRecognition('http://192.168.42.129:4747/video' , state))
		# self.cameraTableWidget.setCellWidget(row+3 ,2 ,checkbox)
  
	def selectFolder(self):
		folderPath = QFileDialog.getExistingDirectory(
				self ,
				caption='Select Person Pictures' ,
				dir=QStandardPaths.writableLocation(QStandardPaths.StandardLocation.PicturesLocation),
			)
		if folderPath:
			self.path.setText(folderPath)
			self.dataBaseManager.setRecordsFolderPath(folderPath)
			for framReadingThread in self.framReaderThreads.values():
				framReadingThread.updateFilename()
				framReadingThread.recognitionThread.updateRecordsFolderPath()

	@Slot()
	def updateEmbedding(self):
		for framReadingThread in self.framReaderThreads.values():
			recognitionThread = framReadingThread.recognitionThread
			recognitionThread.initializeKnownEmbeddings()

	def toggleRecognition(self ,captureId ,state):
		if captureId in self.framReaderThreads:
			frameReadingThread = self.framReaderThreads[captureId]
			totalCheckedBox = self.getTotalCheckedBox()
			if not state:
				print('unchecked')
				frameReadingThread.endRecognitionThread()
			elif totalCheckedBox <= self.MAXRECOGNITIONWORKER :
				print('checked')
				frameReadingThread.startRecognitionThread()
		print(f'the framReaderThreads in Setting is {self.framReaderThreads}')

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
	
	@Slot(bool)
	def sendingEmail(self,find:bool):
		if not find:
			print ("the email is working ")
			Emailsender()
			

		
	def killAllThreads(self):
		for framReadingThread in self.framReaderThreads.values():
			framReadingThread.killThread()
	
	@Slot(str ,str)
	def startLive(self ,captureId ,captureName):
		if captureId not in self.framReaderThreads:
			frameReadingThread = FrameReadingThread(captureId ,captureName)
			frameReadingThread.recognitionThread.signalEmail.connect(self.sendingEmail)
			self.framReaderThreads[captureId] = frameReadingThread
			self.connectThread.emit()
			checkbox = self.getCheckboxForCaptureId(captureId)
			checkbox.setEnabled(True)
			checkbox.setChecked(True)
			frameReadingThread.start()
	
	@Slot(str)
	def killThreads(self ,captureId):
		if captureId in self.framReaderThreads:
			self.framReaderThreads[captureId].killThread()
			del self.framReaderThreads[captureId]
			checkbox = self.getCheckboxForCaptureId(captureId)
			checkbox.setChecked(False)
			checkbox.setDisabled(True)
			print('framReaderThread was killed in setting')
		