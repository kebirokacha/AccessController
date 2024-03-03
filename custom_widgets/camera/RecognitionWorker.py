from PySide6.QtCore import QThread, Signal ,Slot ,QTimer
from databasemanager import DataBaseManager
from ultralytics import YOLO
import face_recognition
import time
import numpy as np
from queue import Queue
import cv2
import cvzone

class RecognitionWorker(QThread):
	databaseManager = DataBaseManager()
	knownEncodings = databaseManager.getEncodingArray()
	model = YOLO('resources/yolov8n-face.pt')
	status = True

	def __init__(self ,queue:Queue ,parent=None):
		QThread.__init__(self , parent)
		self.queue = queue
		images = [
			cv2.imread('person_images/Okacha.jpg'), 
			cv2.imread('person_images/Okacha.jpg'),
			cv2.imread('person_images/Okacha.jpg'),
			cv2.imread('person_images/Okacha.jpg'),
			cv2.imread('person_images/Okacha.jpg'),
			cv2.imread('person_images/Okacha.jpg'),
		]
		self.encoding = []
		for image in images:
			results = self.model.predict(image ,verbose=False)
			for info in results:
				for box in info.boxes:
					x1, y1, x2, y2 = box.xyxy[0]
					x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
					self.encoding.append(face_recognition.face_encodings(image ,[(y1, x2, y2 ,x1)])[0])
		
	def run(self):
		while self.status:
			fram = self.queue.get()
			if fram is not None:
				timerStart = time.time()
				results = self.model.predict(fram, verbose=False)
				for index ,info in enumerate(results):
					for box in info.boxes:
						#(left ,top, right, bottom)
						x1, y1, x2, y2 = box.xyxy[0]
						x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
						h, w = y2 - y1, x2 - x1
						#cvzone.cornerRect(fram, [x1, y1, w, h], l=30,rt=0,t=1,colorC=(255,255,255))
						faceEncoding = face_recognition.face_encodings(fram ,[(y1, x2, y2 ,x1)])[0]
						matches = face_recognition.compare_faces(self.encoding , faceEncoding)

						print(f'The matches of face {index} are !:{matches}')
				timerEnd= time.time()
			print(f'time of execution is !: {timerEnd -timerStart}')
			time.sleep(2)

	def killWorker(self):
		self.status = False
		self.quit()
		self.wait()
		self = None