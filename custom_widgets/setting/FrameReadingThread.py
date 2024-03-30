
from PySide6.QtCore import Signal  ,QThread 
from PySide6.QtGui import QImage
import cv2

class FrameReadingThread(QThread):
	sendFrame = Signal(cv2.Mat)
	updateFrame = Signal(QImage)

	def __init__(self ,captureId ,parent=None):
		QThread.__init__(self ,parent)
		self.capture = cv2.VideoCapture(captureId)
		self.counter = 0
		self.status = True

	def run(self):
		while self.status:
			ret ,frame = self.capture.read()
			if not ret:
				continue
			if self.counter % 30 == 0:
				self.sendFrame.emit(frame)
				self.counter = 0
			frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			height ,width ,channel = frameRgb.shape
			bytesPerLine = channel * width
			qimage = QImage(frameRgb.data ,width ,height ,bytesPerLine ,QImage.Format.Format_RGB888)
			self.updateFrame.emit(qimage)
			self.counter += 1

	def killThread(self):
		self.status = False
		self.capture.release()
		self.quit()
		self.wait()