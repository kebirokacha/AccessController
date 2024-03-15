from PySide6.QtCore import QThread, Signal ,Slot ,QTimer
from databasemanager import DataBaseManager
import time
import numpy as np
from deepface import DeepFace
import cv2

class RecognitionWorker(QThread):

	def __init__(self ,parent=None):
		QThread.__init__(self , parent)
		self.databaseManager = DataBaseManager()
		self.knownEmbeddings = self.databaseManager.getEncodingArray()
		self.status = True
		self.fram = None


	def run(self):
		while self.status:
			if self.fram is not None:
				print('faceRecognition function START')
				start = time.time()
				try:
					results = DeepFace.represent(self.fram, model_name='Facenet512', detector_backend='yolov8')
					for face in results:
						# print(face)
						embedding = np.array(face["embedding"])
						self.checkEmbeddingMatch(self.knownEmbeddings ,embedding)
				except Exception as e:
					print(f'Face not found: {e}')
				print(f"The required time for process is :{time.time() - start}")
				print('faceRecognition function END')
				self.fram = None
				time.sleep(1)
		

	def checkEmbeddingMatch(self ,knownEmbeddings:dict ,unknownEmbedding:np.ndarray ,threshold:int=20):
		matches = {}
		for personId , embeddings in knownEmbeddings.items():
			matchCounter = 0
			for embedding in embeddings:
				knownEmbedding = np.array(embedding)
				distance_vector = np.square(unknownEmbedding - knownEmbedding)
				distance = np.sqrt(distance_vector.sum())
				if distance < 21:
					matchCounter += 1
			matches[personId] = (matchCounter/len(embeddings)) * 100
		# print(f'matches : {matches}')
		# print(f'max match is :{max(matches.values())}')
		if max(matches.values())< 80:
			print('who are you identify you self /"""" ')

	@Slot(cv2.Mat)
	def faceRecognition(self ,fram):
		self.fram = fram
		

	def killWorker(self):
		self.status = False
		self.quit()
		self.wait()
		self = None