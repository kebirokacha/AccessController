from PySide6.QtCore import QThread, Signal ,Slot ,QTimer
from databasemanager import DataBaseManager
import time
import numpy as np
from deepface import DeepFace
import cv2

class RecognitionWorker(QThread):
	databaseManager = DataBaseManager()
	knownEncodings = databaseManager.getEncodingArray()
	status = True

	def __init__(self ,parent=None):
		QThread.__init__(self , parent)

	@Slot(cv2.Mat)
	def faceRecognition(self ,fram):
		print('faceRecognition function START')
		try:
			# Get embedding representation of the face using DeepFace
			embedding = np.array(DeepFace.represent(fram, model_name='Facenet512', detector_backend='yolov8')[0]["embedding"])
			# Compare the face with known encodings
			# matches = self.compare_faces(self.knownEncodings, embedding)
			# TODO: Handle the matches, e.g., emit a signal or update the UI
		except Exception as e:
			print(f'Face not found: {e}')
		print('faceRecognition function END')
		

	def killWorker(self):
		self.status = False
		self.quit()
		self.wait()
		self = None