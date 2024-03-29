from PySide6.QtCore import QThread ,Slot ,Signal
from databasemanager import DataBaseManager
from deepface import DeepFace
import numpy as np
import cv2

class RecognitionWorker(QThread):
	requestCapture = Signal(str)

	def __init__(self ,captureId ,parent=None):
		QThread.__init__(self , parent)
		self.captureId = captureId
		self.databaseManager = DataBaseManager()
		self.knownEmbeddings = self.databaseManager.getEncodingArray()
		self.status = True
		self.cap:cv2.VideoCapture = None

	def run(self):
		self.requestCapture.emit(self.captureId)
		counter = 0
		while self.status:
			if self.cap is not None:
					if counter == 0:
						fps = self.cap.get(cv2.CAP_PROP_FPS)
						print(f"The FPS in the camera with ID {self.captureId} are {fps}")
						print('Note yout are in the recognition worker')
						counter = 1
					ret ,fram = self.cap.read()
					if ret:
						try:
							results = DeepFace.represent(fram, model_name='Facenet512', detector_backend='yolov8')
							for face in results:
								embedding = np.array(face["embedding"])
								self.checkEmbeddingMatch(self.knownEmbeddings ,embedding)
						except Exception as e:
							print(f'Face not found: {e}')
			
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
		print(f'matches are {matches}')
		# if max(matches.values())< 80:
			#TODO:Implement the logique for saving the fram and sending alert for admin
			# print('who are you identify you self /"""" ')

	def killWorker(self):
		self.status = False
		# TODO:Send a signal to the setting to inform that worker has killed
		# if self.cap is not None:
		# 	self.cap.release()
		self.exit()
		self.wait()
		# self = None
	
	@Slot(cv2.VideoCapture)
	def reciveCapture(self ,capture):
		self.cap = capture