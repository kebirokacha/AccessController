from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
from databasemanager import DataBaseManager
import cvzone
import time
import cv2

class CameraWorker(QThread):
	update_frame = Signal(cv2.Mat)
	faceDetected = Signal(cv2.Mat)
	status = True
	

	def __init__(self, capture, parent=None):
		QThread.__init__(self, parent)
		self.capture = capture
		
	def run(self):
		while self.status:
			time.sleep(0.01)
			ret, fram = self.capture.read()
			if not ret:
				continue
			#Detecte Face
			# Update the frame with no rectangle
			
			self.update_frame.emit(fram)

	def killWorker(self):
		self.status = False  # Set the status flag to stop the thread
		self.quit()
		self.wait()  # Wait for the thread to finish
		self = None