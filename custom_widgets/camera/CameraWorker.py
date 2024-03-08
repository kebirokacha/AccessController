from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
from databasemanager import DataBaseManager
import time
import cv2

class CameraWorker(QThread):
	updateFrame = Signal(cv2.Mat)
	def __init__(self, capture, parent=None):
		QThread.__init__(self, parent)
		self.status = True
		self.capture = capture
		
	def run(self):
		while self.status:
			time.sleep(0.01)
			ret, fram = self.capture.read()
			if not ret:
				continue
			#Detecte Face
			# color_frame = cv2.cvtColor(fram, cv2.COLOR_BGR2RGB)
			# height, width, channel = color_frame.shape
			# image = QImage(color_frame.data, width, height, QImage.Format_RGB888)
			self.updateFrame.emit(fram)

	def killWorker(self):
		self.status = False  # Set the status flag to stop the thread
		self.quit()
		self.wait()  # Wait for the thread to finish
		self = None