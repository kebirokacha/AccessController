from PySide6.QtCore import Slot 
from PySide6.QtGui import QPixmap ,QImage
from PySide6.QtWidgets import  QWidget
from .CameraWorker import  CameraWorker
from .RecognitionWorker import RecognitionWorker
from .Camera_ui import Ui_Camera
import cv2

class CameraWidget(Ui_Camera ,QWidget):
	satus = True
	counter = 0
	def __init__(self):
		super(CameraWidget, self).__init__()
		self.setupUi(self)
		self.capture = cv2.VideoCapture(0)
		self.capture.set(cv2.CAP_PROP_FPS ,30)
		self.cameraWorker = CameraWorker(self.capture)
		self.cameraWorker.updateFrame.connect(self.setImage)
		self.cameraWorker.start()



	def closeEvent(self, event):
		self.cameraWorker.killWorker()
		event.accept()


	@Slot(QImage)
	def setImage(self, image):
		self.cameraLabel_01.setPixmap(QPixmap.fromImage(image))
