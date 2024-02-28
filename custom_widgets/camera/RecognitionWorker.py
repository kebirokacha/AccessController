from PySide6.QtCore import QThread, Signal ,Slot ,QTimer
from databasemanager import DataBaseManager
from ultralytics import YOLO
import face_recognition
import time
import numpy as np
import cv2

class RecognitionWorker(QThread):
	recognizedFace = Signal(list) 
	databaseManager = DataBaseManager()
	knownEncodings = databaseManager.getEncodingArray()
	model = YOLO('resources/yolov8n-face.pt')
	status = True

	def __init__(self ,capture ,parent=None):
		QThread.__init__(self, parent)
		self.capture = capture
		images = [
		cv2.imread('person_images/elmhadji.jpg') , 
		cv2.imread('person_images/elmhadji1.jpg') ,
		cv2.imread('person_images/elmhadji2.jpg') ,
		cv2.imread('person_images/elmhadji3.jpg'),
		cv2.imread('person_images/elmhadji4.jpg'),
		cv2.imread('person_images/elmhadji5.jpg'),

		]
		self.encoding = []
		for image in images:
			results = self.model.predict(image ,verbose=False)
			for info in results:
				for box in info.boxes:
					x1, y1, x2, y2 = box.xyxy[0]
					x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
					self.encoding.append(face_recognition.face_encodings(image ,[(y1, x2, y2 ,x1)])[0])
		print(self.knownEncodings)
		print(self.encoding)

	def run(self):
		while self.status:
			time.sleep(1)
			ret, fram = self.capture.read()
			if not ret:
				continue
			results = self.model.predict(fram, verbose=False)
			for info in results:
				for box in info.boxes:
					#(left ,top, right, bottom)
					x1, y1, x2, y2 = box.xyxy[0]
					x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
				faceEncoding = face_recognition.face_encodings(fram ,[(y1, x2, y2 ,x1)])[0]
				matches = face_recognition.compare_faces(self.encoding , faceEncoding)
				
				
					
		

	def killWorker(self):
		self.status = False
		self.quit()
		self.wait()
		self = None