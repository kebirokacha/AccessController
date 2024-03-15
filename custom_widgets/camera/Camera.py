from PySide6.QtCore import Slot ,Qt
from PySide6.QtGui import QPixmap ,QImage ,QAction
from PySide6.QtWidgets import  QWidget ,QLabel ,QMenu
from .CameraWorker import  CameraWorker

from .Camera_ui import Ui_Camera
import cv2

class CameraWidget(Ui_Camera ,QWidget):
	def __init__(self):
		super(CameraWidget, self).__init__()
		self.setupUi(self)
		self.cameraLabels = [self.label_1 ,self.label_2 ,self.label_3 ,self.label_4]
		self.oneCam()
		cap = 'http://192.168.1.3:4747/video'
		self.cameraWorker = CameraWorker(0)
		self.cameraWorker.updateFrame.connect(self.setImageLabel_1)
		# self.cameraWorker2 = CameraWorker('http://192.168.1.3:4747/video')
		# self.cameraWorker2.updateFrame.connect(self.setImageLabel_2)
		self.oneCamButton.clicked.connect(self.oneCam)
		self.twoCamButton.clicked.connect(self.twoCam)
		self.fourCamButton.clicked.connect(self.fourCam)
		self.cameraWorker.start()
	
	def oneCam(self):
		for label in self.cameraLabels[1:]:
			label.hide()
		# if self.cameraWorker2.isRunning():
		# 	self.cameraWorker2.killWorker()
		
	def twoCam(self):
		self.cameraLabels[1].show()
		for label in self.cameraLabels[2:]:
			label.hide()
		# if not self.cameraWorker2.isRunning():
		# 	self.cameraWorker2.start()
	
	def fourCam(self):
		for label in self.cameraLabels[1:]:
			label.show()



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
