from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
from databasemanager import DataBaseManager
from ultralytics import YOLO
import cvzone
import cv2 as cv

class CameraWorker(QThread):
	update_frame = Signal(QImage)
	faceDetected = Signal(cv.Mat ,tuple)
	status = True
	capture = cv.VideoCapture('http:/192.168.1.3:4747/video')
	capture.set(cv.CAP_PROP_FPS ,60)
	model = YOLO('yolov8n-face.pt')
	def __init__(self, parent=None):
		QThread.__init__(self, parent)
	
		
	def run(self):
		while self.status:
			ret, fram = self.capture.read()
			if not ret:
				continue
			#Detecte Face
			results = self.model.predict(fram)
			for info in results:
				parameters = info.boxes
				for box in parameters:
					#(left ,top, right, bottom)
					x1, y1, x2, y2 = box.xyxy[0]
					x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
					h, w = y2 - y1, x2 - x1
					#Send the fram and face location to the recognition worker
					self.faceDetected.emit(fram ,(y1, x2, y2 ,x1))
					if True:
						cvzone.cornerRect(fram, [x1, y1, w, h], l=9, rt=1)
					

			# Update the frame with no rectangle
			color_frame = cv.cvtColor(fram, cv.COLOR_BGR2RGB)
			height, width, channel = color_frame.shape
			image = QImage(color_frame.data, width, height, QImage.Format_RGB888)
			self.update_frame.emit(image)

	def killWorker(self):
		self.status = False  # Set the status flag to stop the thread
		self.quit()
		self.wait()  # Wait for the thread to finish
		self = None