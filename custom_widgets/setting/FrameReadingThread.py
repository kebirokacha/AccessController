from PySide6.QtCore import Signal, QThread, QDateTime, QTime ,Slot
from PySide6.QtGui import QImage
from databasemanager import DataBaseManager
from .RecognitionThread import RecognitionThread
import os
import cv2

class FrameReadingThread(QThread):
	sendFrame = Signal(cv2.Mat)
	updateFrame = Signal(QImage)
	resetCustomLabel = Signal()

	def __init__(self, captureId, captureName, parent=None):
		QThread.__init__(self, parent)
		self.capture = cv2.VideoCapture(captureId)
		#FIXME  check it later to see what it does 
		# self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1024)
		self.captureName = captureName
		self.videoWriter = None
		self.status = True
		self.recognitionThread = RecognitionThread(captureName)
		self.sendFrame.connect(self.recognitionThread.setFrame)
		self.lastRecognition = QTime.currentTime()
		self.startTime = QTime.currentTime()
		self.updateFilename()
		self.recognitionThread.start()

	def run(self):
		while self.status:
			ret, frame = self.capture.read()
			if not ret:
				continue
			if self.lastRecognition.secsTo(QTime.currentTime()) >=1:
				self.sendFrame.emit(frame)
				self.lastRecognition = QTime.currentTime()
			if self.startTime.secsTo(QTime.currentTime()) >= 3600000: # 3600000 milliseconds = 1 hour
				self.updateFilename()
			self.videoWriter.write(frame)
			cv2.putText(frame, self.captureName, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
			#TODO Add some sort of icon to know when  recognition is active 
			frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			height, width, channel = frameRgb.shape
			bytesPerLine = channel * width
			qimage = QImage(frameRgb.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
			self.updateFrame.emit(qimage)

	def updateFilename(self):
		dataBaseManager = DataBaseManager()
		recordsFolderPath = dataBaseManager.getRecordsFolderPath()
		videoFolderPath = os.path.join(recordsFolderPath ,'videos')
		if not os.path.isdir(videoFolderPath):
			os.mkdir(videoFolderPath)
		currentTime = QDateTime.currentDateTime().toString("dd_MM_yyyy_HH_mm_ss")
		filename = f"{self.captureName}_{currentTime}.mp4"
		filename = filename.replace(":", "_")
		filename = os.path.join(videoFolderPath ,filename)
		size = (int(self.capture.get(3)), int(self.capture.get(4)))
		fps = int(self.capture.get(cv2.CAP_PROP_FPS))
		if self.videoWriter is not None:
			self.videoWriter.release()
		self.videoWriter = cv2.VideoWriter(filename, cv2.VideoWriter.fourcc(*'mp4v') ,24 ,size, isColor=True)
		self.startTime = QTime.currentTime()

	@Slot()
	def endRecognitionThread(self):
		if self.recognitionThread is not None and self.recognitionThread.isRunning():
			self.recognitionThread.killThread()
		print('recognition ended')

	@Slot()
	def startRecognitionThread(self):
		if self.recognitionThread is not None and not self.recognitionThread.isRunning():
			self.recognitionThread.start()
		print('recognition started')


	def killThread(self):
		self.status = False
		if self.recognitionThread is not None and self.recognitionThread.isRunning():
			self.recognitionThread.killThread()
			print('recognition Thread complet')

		self.capture.release()
		if self.videoWriter is not None:
			self.videoWriter.release()
		self.quit()
		self.wait()
		print('frame reading thread complet')
		self.resetCustomLabel.emit()
		print('custome Label resete complete')
