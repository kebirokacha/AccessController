from PySide6.QtCore import Slot ,QThread 
from databasemanager import DataBaseManager
from deepface import DeepFace
import numpy as np
import cv2 

class RecognitionThread(QThread):

	def __init__(self ,parent=None):
		QThread.__init__(self ,parent)
		self.databaseManager = DataBaseManager()
		self.knownEmbeddings = self.databaseManager.getEncodingArray()
		self.status = True
		self.frame = None

	def run(self):
		while self.status:
			if self.frame is None:
				continue
			try:
				results = DeepFace.represent(self.frame, model_name='Facenet512', detector_backend='yolov8')
				for face in results:
					embedding = np.array(face["embedding"])
					self.checkEmbeddingMatch(self.knownEmbeddings ,embedding)
			except Exception as e:
				print(f'Face not found: {e}')
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
		print(f'matches are {matches}')

	@Slot(cv2.Mat)
	def setFrame(self ,frame:cv2.Mat):
		self.frame = frame

	def killThread(self):
		self.status = False

		self.quit()
		self.wait()