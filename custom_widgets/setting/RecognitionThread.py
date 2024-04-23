from PySide6.QtCore import Slot ,QThread ,QDateTime
from databasemanager import DataBaseManager
import numpy as np
import cv2 
from deepface.DeepFace import represent
import os

class RecognitionThread(QThread):

	def __init__(self ,captureName:str ,parent=None):
		QThread.__init__(self ,parent)
		self.captureName = captureName
		self.pictureFolderPath = None
		self.initializeKnownEmbeddings()
		self.initializeRecordsFolderPath()
		self.status = True
		self.frame = None

	def run(self):
		while self.status:
			if self.frame is None:
				continue
			try:
				results = represent(self.frame, model_name='Facenet512' , detector_backend='yolov8')
				for face in results:
					embedding = np.array(face["embedding"])
					maxMatch = self.checkEmbeddingMatch(self.knownEmbeddings ,embedding)
					if maxMatch < 55 and self.pictureFolderPath is not None and self.frame is not None:
						currentTime = QDateTime.currentDateTime().toString("dd_MM_yyyy_HH_mm_ss")
						filename = f"{self.captureName}_{currentTime}.jpg"
						filename = filename.replace(":", "_")
						filename = os.path.join(self.pictureFolderPath ,filename)
						# save only when we find new face 
						dataBaseManager = DataBaseManager()
						isSaved = dataBaseManager.saveUnknownEmbedding(embedding)
						if isSaved:
							facial_area = face["facial_area"]
							x, y, w, h = facial_area["x"]-20 ,facial_area["y"]-20 ,facial_area["w"]+20 ,facial_area["h"]+20
							faceImage = self.frame[y:y+h, x:x+w]
							cv2.imwrite(filename ,faceImage)
			except Exception as e:
				print(f'Face not found: {e}')
			finally:
				self.frame = None

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
		maxMatche = max(matches.values())
		return maxMatche
	
	def initializeRecordsFolderPath(self):
		if self.pictureFolderPath is None:
			dataBaseManager = DataBaseManager()
			recordsFolderPath = dataBaseManager.getRecordsFolderPath()
			self.pictureFolderPath = os.path.join(recordsFolderPath ,'pictures')
			if not os.path.isdir(self.pictureFolderPath):
				os.mkdir(self.pictureFolderPath)


	def updateRecordsFolderPath(self):
		if self.pictureFolderPath is not None:
			dataBaseManager = DataBaseManager()
			recordsFolderPath = dataBaseManager.getRecordsFolderPath()
			self.pictureFolderPath = os.path.join(recordsFolderPath ,'pictures')
			if not os.path.isdir(self.pictureFolderPath):
				os.mkdir(self.pictureFolderPath)

	def initializeKnownEmbeddings(self):
		self.dataBaseManager = DataBaseManager()
		self.knownEmbeddings = self.dataBaseManager.getEncodingArray()

	@Slot(cv2.Mat)
	def setFrame(self ,frame:cv2.Mat):
		self.frame = frame

	def killThread(self):
		self.status = False
		self.quit()
		self.wait()