from PySide6.QtWidgets import QWidget, QTableWidgetItem, QCheckBox, QFileDialog ,QHeaderView
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtCore import Slot, Signal, QStandardPaths
from .FrameReadingThread import FrameReadingThread
from databasemanager import DataBaseManager
from ..dialog.ErrorDialog import ErrorDialog
from .Setting_ui import Ui_Setting
from .sendEmailClass import Emailsender
from os.path import isfile



def validateEmail(email: str) -> bool:
	from re import match
	pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
	return match(pattern, email) is not None


class Setting(Ui_Setting, QWidget):
	connectThread = Signal()
	updateRecordsFolderPath = Signal()

	def __init__(self):
		super(Setting, self).__init__()
		self.setupUi(self)
		self.MAXRECOGNITIONWORKER = 2
		self.savedEmailTxt = 'savedEmail.txt'
		self.savedEmail = ''
		self.framReaderThreads: dict[int, FrameReadingThread] = {}
		self.cameraTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
		self.cameraTableWidget.hideColumn(0)
		self.initializeRecordsFolder()
		self.loadCameras()
		self.loadSavedEmail()
		self.saveEmailButton.clicked.connect(self.saveEmail)
		self.refreshButton.clicked.connect(self.loadCameras)
		self.recognitionButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
		self.recordsButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
		self.notificationButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(2))
		self.stackedWidget.currentChanged.connect(self.updateButtonStyles)
		self.updateButtonStyles()

	def loadCameras(self):
		self.cameraTableWidget.clear()
		self.cameraTableWidget.setHorizontalHeaderLabels(["Camera ID","Camera Name","Recognition status"])
		captures = QMediaDevices.videoInputs()
		self.cameraTableWidget.setRowCount(len(captures))
		for row, capture in enumerate(captures):
			name = capture.description()
			self.cameraTableWidget.setItem(row, 0, QTableWidgetItem(str(row)))
			self.cameraTableWidget.setItem(row, 1, QTableWidgetItem(name))
			checkbox = QCheckBox()
			checkbox.setDisabled(True)
			checkbox.stateChanged.connect(lambda state: self.toggleRecognition(row, state))
			self.cameraTableWidget.setCellWidget(row, 2, checkbox)
		else:
			#TODO: when there are co capture detected
			pass
	
	def updateButtonStyles(self):
		currentIndex = self.stackedWidget.currentIndex()
		selected_style = "QPushButton { background-color: #008EF6;}"

		# Apply the base style to all buttons
		self.recognitionButton.setStyleSheet("")
		self.recordsButton.setStyleSheet("")
		self.notificationButton.setStyleSheet("")
		match currentIndex:
			case 0:
				self.recognitionButton.setStyleSheet(selected_style)
			case 1:
				self.recordsButton.setStyleSheet(selected_style)
			case 2:
				self.notificationButton.setStyleSheet(selected_style)

	def saveEmail(self):
		if self.emailInput.text() == "":
			self.showErrorDialog("Error Validation", "Please fill the Email.")
			return

		if not validateEmail(self.emailInput.text()):
			self.showErrorDialog("Error Validation", "Please enter a valid email address.")
			return
		with open(self.savedEmailTxt, 'w') as file:
			file.write(self.emailInput.text())
			self.savedEmail = self.emailInput.text()
		self.showErrorDialog("Email saved", "The email has been saved successfully.")

	def checkSavedEmail(self) -> bool:
		if isfile(self.savedEmailTxt):
			return True
		return False

	def loadSavedEmail(self) -> str:
		if self.checkSavedEmail():
			with open(self.savedEmailTxt ,'r') as file:
				self.savedEmail = str(file.read().strip())
				self.emailInput.setText(self.savedEmail)
			return self.savedEmail
		else:
			return ''

	def showErrorDialog(self, title: str, message: str):
		dialog = ErrorDialog(title, message, self)
		dialog.exec()

	def initializeRecordsFolder(self):
		dataBaseManager = DataBaseManager()
		self.path.setText(dataBaseManager.getRecordsFolderPath())
		self.selectPathButton.clicked.connect(self.selectFolder)

	def selectFolder(self):
		folderPath = QFileDialog.getExistingDirectory(
			self,
			caption='Select Person Pictures',
			dir=QStandardPaths.writableLocation(QStandardPaths.StandardLocation.PicturesLocation),
		)
		if folderPath:
			dataBaseManager = DataBaseManager()
			self.path.setText(folderPath)
			dataBaseManager.setRecordsFolderPath(folderPath)
			for framReadingThread in self.framReaderThreads.values():
				framReadingThread.updateFilename()
				framReadingThread.recognitionThread.updateRecordsFolderPath()

	@Slot()
	def updateEmbedding(self):
		for framReadingThread in self.framReaderThreads.values():
			recognitionThread = framReadingThread.recognitionThread
			recognitionThread.initializeKnownEmbeddings()

	def toggleRecognition(self, captureId, state):
		if captureId in self.framReaderThreads:
			frameReadingThread = self.framReaderThreads[captureId]
			totalCheckedBox = self.getTotalCheckedBox()
			if not state:
				print('unchecked')
				frameReadingThread.endRecognitionThread()
			elif totalCheckedBox <= self.MAXRECOGNITIONWORKER:
				print('checked')
				frameReadingThread.startRecognitionThread()
			print(f'the framReaderThreads in Setting is {self.framReaderThreads}')

	def getTotalCheckedBox(self) -> int:
		totalChecked = 0
		for row in range(self.cameraTableWidget.rowCount()):
			checkbox: QCheckBox = self.cameraTableWidget.cellWidget(row, 2)
			if checkbox.isChecked():
				totalChecked += 1
		return totalChecked

	def getCheckboxForCaptureId(self, captureId:int) -> QCheckBox|None:
		for row in range(self.cameraTableWidget.rowCount()):
			item = self.cameraTableWidget.item(row, 0)
			if item and item.text() == str(captureId):
				checkbox = self.cameraTableWidget.cellWidget(row, 2)
				return checkbox
		return None

	def killAllThreads(self):
		for framReadingThread in self.framReaderThreads.values():
			framReadingThread.killThread()

	@Slot()
	def sendingEmail(self):
		email = self.loadSavedEmail()
		dailyEmail = self.dailyEmailCheckBox.isChecked()
		liveEmail = self.liveEmailCheckBox.isChecked()
		print(f"email {email} \n dailyEmail {dailyEmail}\n liveEmail {liveEmail}")
		if (dailyEmail or liveEmail) and email != '':
			emailSended = Emailsender(receiver = email).sendEmail()
			if emailSended:
				print("email sended")
			else:
				print("we face a problem in sending email!!")

	def startLive(self, captureId:int, captureName:str):
		captureId = int(captureId)
		if captureId not in self.framReaderThreads:
			frameReadingThread = FrameReadingThread(int(captureId), captureName)
			frameReadingThread.recognitionThread.signalEmail.connect(self.sendingEmail)
			self.framReaderThreads[captureId] = frameReadingThread
			self.connectThread.emit()
			checkbox = self.getCheckboxForCaptureId(captureId)
			if checkbox is not None:
				checkbox.setEnabled(True)
				checkbox.setChecked(True)
				frameReadingThread.start()

	def deleteFrameReadingThread(self, captureId:int):
		captureId = int(captureId)
		if captureId in self.framReaderThreads:
			checkbox = self.getCheckboxForCaptureId(captureId)
			if checkbox is not None:
				checkbox.setChecked(False)
				checkbox.setDisabled(True)
			self.framReaderThreads[captureId].killThread()
			del self.framReaderThreads[captureId]
			print(f'framReaderThread with id {captureId} was killed in setting')
