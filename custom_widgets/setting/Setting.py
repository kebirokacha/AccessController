from PySide6.QtWidgets import  QWidget ,QTableWidgetItem ,QCheckBox
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtCore import QThread ,Slot 
from databasemanager import DataBaseManager
from .Setting_ui import Ui_Setting
from deepface import DeepFace
import numpy as np
import cv2 

class Setting (Ui_Setting,QWidget):
	def __init__(self):
		super(Setting,self).__init__()
		self.setupUi(self)
		self.recognitionWorkerDict:dict = {}
		self.MAXRECOGNITIONWORKER = 4
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

	def startRecognition(self ,cameraId ,state):
		totalCheckedBox = self.getTotalCheckedBox()
		if not state:
			print('unchecked')
			if cameraId in self.recognitionWorkerDict:
				self.recognitionWorkerDict[cameraId].killWorker() 
				del self.recognitionWorkerDict[cameraId] 
		elif totalCheckedBox < self.MAXRECOGNITIONWORKER :
			print('checked')
			if cameraId not in self.recognitionWorkerDict: 
				worker = RecognitionWorker(cameraId)
				self.recognitionWorkerDict[cameraId] = worker 
				worker.start()
			
	def getTotalCheckedBox(self) -> int:
		totalChecked = 0
		for row in range(self.cameraTableWidget.rowCount()):
			checkbox:QCheckBox = self.cameraTableWidget.cellWidget(row, 2)
			if checkbox.isChecked():
				totalChecked += 1
		return totalChecked


class RecognitionWorker(QThread):

	def __init__(self ,cameraId ,parent=None):
		QThread.__init__(self , parent)
		self.databaseManager = DataBaseManager()
		self.knownEmbeddings = self.databaseManager.getEncodingArray()
		self.cameraId = cameraId
		self.counter = 0
		self.status = True
		self.cap = None

	def run(self):
		self.cap = cv2.VideoCapture(self.cameraId)
		fps = self.cap.get(cv2.CAP_PROP_FPS)
		print(f"The FPS in the camera with ID {self.cameraId} are {fps}")
		while self.status:
			# if self.counter % 30 != 0:
			# 	self.counter += 1
			# 	continue
			ret, fram = self.cap.read()
			if ret:
				try:
					results = DeepFace.represent(fram, model_name='Facenet512', detector_backend='yolov8')
					for index ,face in enumerate(results):
						print(index)
						embedding = np.array(face["embedding"])
						self.checkEmbeddingMatch(self.knownEmbeddings ,embedding)
				except Exception as e:
					print(f'Face not found: {e}')
			# self.counter = 0

	def checkEmbeddingMatch(self ,knownEmbeddings:dict ,unknownEmbedding:np.ndarray ,threshold:int=20):
		matches = {}
		for personId , embeddings in knownEmbeddings.items():
			matchCounter = 0
			for embedding in embeddings:
				knownEmbedding = np.array(embedding)
				distance_vector = np.square(unknownEmbedding - knownEmbedding)
				distance = np.sqrt(distance_vector.sum())
				if distance < threshold:
					matchCounter += 1
			matches[personId] = (matchCounter/len(embeddings)) * 100
		if max(matches.values())< 80:
			#TODO:Implement the logique for saving the fram and sending alert for admin
			print('who are you identify you self /"""" ')

	@Slot(cv2.Mat)
	def setFram(self ,fram):
		self.fram = fram

	def killWorker(self):
		self.status = False
		if self.cap is not None:
			self.cap.release()
		self.quit()
		self.wait()
		self = None