from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
from databasemanager import DataBaseManager
import cvzone
import cv2 as cv

class CameraWorker(QThread):
	update_frame = Signal(QImage)
	faceDetected = Signal(cv.Mat)
	status = True
	

	def __init__(self, capture, parent=None):
		QThread.__init__(self, parent)
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