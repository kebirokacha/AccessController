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
		self.queue = queue
		self.inermediatValue = True
		
		
	def run(self):
		while self.status:
			ret, fram = self.capture.read()
			if not ret:
				continue
			self.updateFrame.emit(fram)
			self.queue.put(fram)
			time.sleep(0.02)
			

	def killWorker(self):
		self.status = False  # Set the status flag to stop the thread
		self.quit()
		self.wait()  # Wait for the thread to finish
		self = None