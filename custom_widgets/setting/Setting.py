from PySide6.QtWidgets import  QWidget ,QTableWidgetItem ,QCheckBox
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtCore import Slot ,Signal
from ..camera.RecognitionWorker import RecognitionWorker
from .Setting_ui import Ui_Setting
import cv2 

class Setting (Ui_Setting,QWidget):
	sendCapture = Signal(cv2.VideoCapture)
	sendFrame = Signal(cv2.Mat)

	def __init__(self):
		super(Setting,self).__init__()
		self.setupUi(self)
		self.MAXRECOGNITIONWORKER = 4
		self.capturesDict:dict[str ,cv2.VideoCapture] = {}
		self.recognitionWorkerDict:dict[str ,RecognitionWorker] = {}
		self.loadCapture()
		self.loadCameras()

	def loadCameras(self):
		self.cameraTableWidget.clear()
		cameras = QMediaDevices.videoInputs()
		self.cameraTableWidget.setRowCount(len(cameras))
		self.cameraTableWidget.setColumnCount(3)
		for row ,camera in enumerate(cameras):
			cameraId  = camera.id().data().decode()
			name = camera.description()
			self.cameraTableWidget.setItem(row ,0 ,QTableWidgetItem(cameraId))
			self.cameraTableWidget.setItem(row ,1 ,QTableWidgetItem(name))
			checkbox = QCheckBox()
			checkbox.stateChanged.connect(lambda state: self.startRecognition(cameraId , state))
			self.cameraTableWidget.setCellWidget(row ,2 ,checkbox)
			self.cameraTableWidget.hideColumn(0)
		#TODO: load from database if the camera is used for recognition or not

	def loadCapture(self):
		cameras = QMediaDevices.videoInputs()
		for camera in cameras:
			cameraId = camera.id().data().decode()
			if cameraId not in self.capturesDict:
				self.capturesDict[cameraId] = cv2.VideoCapture(cameraId)

	def startRecognition(self ,cameraId ,state):
		totalCheckedBox = self.getTotalCheckedBox()
		if not state:
			print('unchecked')
			if cameraId in self.recognitionWorkerDict:
				self.recognitionWorkerDict[cameraId].killWorker()
				self.refreshCapture(cameraId)
				del self.recognitionWorkerDict[cameraId] 
		elif totalCheckedBox < self.MAXRECOGNITIONWORKER :
			print('checked')
			if cameraId not in self.recognitionWorkerDict: 
				worker = RecognitionWorker(cameraId)
				self.sendCapture.connect(worker.reciveCapture)
				worker.requestCapture.connect(self.requestCapture)
				self.recognitionWorkerDict[cameraId] = worker 
				worker.start()
		print(f'the Captures in Setting is {self.capturesDict}')
		
			
	def getTotalCheckedBox(self) -> int:
		totalChecked = 0
		for row in range(self.cameraTableWidget.rowCount()):
			checkbox:QCheckBox = self.cameraTableWidget.cellWidget(row, 2)
			if checkbox.isChecked():
				totalChecked += 1
		return totalChecked

	@Slot()
	def requestCapture(self ,captureId ):
		print(f'the Captures in Setting is {self.capturesDict}')
		if captureId in self.capturesDict:
			capture = self.capturesDict[captureId]
			print(f'{capture} requested')
			self.sendCapture.emit(capture)
			print(f'{capture} emited')

	@Slot()
	def refreshCapture(self ,captureId ):
		print(f'the Captures in Setting is {self.capturesDict}')
		if captureId in self.capturesDict and self.capturesDict[captureId].isOpened():
			self.capturesDict[captureId].release()
			self.capturesDict[captureId] = cv2.VideoCapture(captureId)
			self.sendCapture.emit(self.capturesDict[captureId])
