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
		self.fram = None


	def run(self):
		while self.status:
			if self.fram is not None:
				print('faceRecognition function START')
				start = time.time()
				try:
					# Get embedding representation of the face using DeepFace
					embedding = np.array(DeepFace.represent(self.fram, model_name='Facenet512', detector_backend='yolov8')[0]["embedding"])
					# Compare the face with known encodings
					# matches = self.compare_faces(self.knownEncodings, embedding)
					# TODO: Handle the matches, e.g., emit a signal or update the UI
				except Exception as e:
					print(f'Face not found: {e}')
				print(f"The required time for process is :{time.time() - start}")
				print('faceRecognition function END')
				self.fram = None

	@Slot(cv2.Mat)
	def faceRecognition(self ,fram):
		self.fram = fram
		

	def killWorker(self):
		self.status = False
		self.quit()
		self.wait()
		self = None