from PySide6.QtCore import QThread, Signal ,Slot
from PySide6.QtGui import QImage
from .RecognitionWorker import RecognitionWorker
import cv2

class CameraWorker(QThread):
	updateFrame = Signal(QImage)
	requestCapture = Signal(str)
	refreshCapture = Signal(str)

	def __init__(self, captureId ,parent=None):
		QThread.__init__(self, parent)
		self.captureId = captureId
		self.status = True
		self.cap:cv2.VideoCapture = None

	def run(self):
		self.requestCapture.emit(self.captureId)
		counter = 0
		while self.status:
			if self.cap is not None:
				if counter == 0:
						fps = self.cap.get(cv2.CAP_PROP_FPS)
						print(f"The FPS in the camera with ID {self.captureId} are {fps} ")
						print('Note yout are in the camera worker')
						counter = 1
				ret, frame = self.cap.read()
				if ret:
					frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
					height ,width ,channel = frameRgb.shape
					bytesPerLine = channel * width
					qimage = QImage(frameRgb.data ,width ,height ,bytesPerLine ,QImage.Format.Format_RGB888)
					self.updateFrame.emit(qimage)
		
	def killWorker(self):
		self.status = False
		# TODO:Send a signal to the setting to inform that worker has killed
		if self.cap is not None:
			self.refreshCapture.emit(self.captureId)
		# if self.cap is not None:
		# 	self.cap.release()
		self.exit()
		self.wait()
	
	@Slot(cv2.VideoCapture)
	def reciveCapture(self ,capture):
		self.cap = capture