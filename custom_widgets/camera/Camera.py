from PySide6.QtCore import Slot ,Qt
from PySide6.QtGui import QPixmap ,QImage ,QAction
from PySide6.QtWidgets import  QWidget ,QLabel ,QMenu
from .CameraWorker import  CameraWorker
from .RecognitionWorker import RecognitionWorker
from .Camera_ui import Ui_Camera
import cv2

class CameraWidget(Ui_Camera ,QWidget):
	def __init__(self):
		super(CameraWidget, self).__init__()
		self.setupUi(self)
		self.label_1 = QLabel('LoadCamera')
		self.label_2 = QLabel('LoadCamera')
		
		self.label_2.hide()
		self.cameraGrid.addWidget(self.label_1 ,0 ,0)
		self.cameraGrid.addWidget(self.label_2 ,0 ,1)

		self.cameraWorker = CameraWorker(0)
		self.cameraWorker.updateFrame.connect(self.setImageLabel_1)
		# self.cameraWorker2 = CameraWorker('http://192.168.1.3:4747/video')
		# self.cameraWorker2.updateFrame.connect(self.setImageLabel_2)
		self.oneCamButton.clicked.connect(self.oneCam)
		self.twoCamButton.clicked.connect(self.twoCam)
		self.cameraWorker.start()
	
	def oneCam(self):
		if self.label_2 is not None:
			self.label_2.hide()
		# if self.cameraWorker2.isRunning():
		# 	self.cameraWorker2.killWorker()
		
	def twoCam(self):
		if self.label_2 is not None:
			self.label_2.show()
		# if not self.cameraWorker2.isRunning():
		# 	self.cameraWorker2.start()


	def closeEvent(self, event):
		self.cameraWorker.killWorker()
		# self.recognitionWorker.killWorker()
		event.accept()


	@Slot(QImage)
	def setImageLabel_1(self, image:QImage):
		self.label_1.setPixmap(QPixmap.fromImage(image))
	
	@Slot(QImage)
	def setImageLabel_2(self, image:QImage):
		self.label_2.setPixmap(QPixmap.fromImage(image))
