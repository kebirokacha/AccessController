from PySide6.QtCore import Signal, QThread, QDateTime, QTime ,Slot
from PySide6.QtGui import QImage
import cv2

class FrameReadingThread(QThread):
	sendFrame = Signal(cv2.Mat)
	updateFrame = Signal(QImage)
	resetCustomLabel = Signal()

	def __init__(self, captureId, captureName, parent=None):
		QThread.__init__(self, parent)
		self.capture = cv2.VideoCapture(captureId)
		self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1024)
		self.captureName = captureName
		self.videoWriter = None
		self.counter = 0
		self.status = True
		self.start_time = QTime.currentTime() # Initialize QTime to track elapsed time
		self.updateFilename() # Initialize the video writer with the first filename

	def run(self):
		while self.status:
			ret, frame = self.capture.read()
			if not ret:
				continue
			if self.counter % 30 == 0:
				self.sendFrame.emit(frame)
				self.counter = 0
			self.counter += 1
			# Check if an hour has passed and update the filename if necessary
			if self.start_time.secsTo(QTime.currentTime()) >= 3600000: # 3600000 milliseconds = 1 hour
				self.updateFilename()
			self.videoWriter.write(frame)
			cv2.putText(frame, self.captureName, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
			frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			height, width, channel = frameRgb.shape
			bytesPerLine = channel * width
			qimage = QImage(frameRgb.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
			self.updateFrame.emit(qimage)

	def updateFilename(self):
		# Update the filename with the current time
		current_time = QDateTime.currentDateTime().toString("HHmmss")
		filename = f"{self.captureName}_{current_time}.mp4"
		filename = filename.replace(":", "_")
		print(f'fileName is {filename}')
		# Release the old video writer and create a new one with the updated filename
		size = (int(self.capture.get(3)), int(self.capture.get(4)))
		fps = int(self.capture.get(cv2.CAP_PROP_FPS))
		if self.videoWriter is not None:
			self.videoWriter.release()
		self.videoWriter = cv2.VideoWriter(f'files_records/videos/{filename}', cv2.VideoWriter.fourcc(*'mp4v') ,fps ,size, isColor=True)
		# Reset the start time
		self.start_time = QTime.currentTime()

	@Slot()
	def setIsRecognize(self):
		self.isRecognize = not self.isRecognize

	def killThread(self):
		self.status = False
		self.capture.release()
		if self.videoWriter is not None:
			self.videoWriter.release()
		self.quit()
		self.wait()
		print('frame reading complet')
