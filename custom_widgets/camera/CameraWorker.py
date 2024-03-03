from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
from databasemanager import DataBaseManager
from queue import Queue
import time
import cv2

class CameraWorker(QThread):
	updateFrame = Signal(cv2.Mat)

	def __init__(self, capture:cv2.VideoCapture , queue:Queue, parent=None):
		QThread.__init__(self, parent)
		self.status = True
		self.capture = capture
		
	def run(self):
		while self.status:
			ret, fram = self.capture.read()
			if not ret:
				continue
			#Detecte Face
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