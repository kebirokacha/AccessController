from PySide6.QtCore import QThread, Signal, QTimer
from PySide6.QtGui import QImage
from databasemanager import DataBaseManager
from .RecognitionWorker import RecognitionWorker
import threading
import time
import numpy as np
import cv2

class CameraWorker(QThread):
    updateFrame = Signal(QImage)
    sendFram = Signal(cv2.Mat)

    def __init__(self, capture: cv2.VideoCapture, parent=None):
        QThread.__init__(self, parent)
        self.status = True
        self.capture = capture
        self.counter = 0
        self.recognitionWorker = RecognitionWorker()
        self.sendFram.connect(self.recognitionWorker.faceRecognition)
        self.timer = QTimer()
        self.timer.timeout.connect(self.processFrame)
        self.timer.start(1500) # Emit the frame every 1 second (1000 milliseconds)

    def processFrame(self):
        ret, frame = self.capture.read()
        if not ret:
            return
        self.sendFram.emit(frame) # Emit the frame to the RecognitionWorker

    def run(self):
        while self.status:
            color_frame = cv2.cvtColor(self.capture.read()[1], cv2.COLOR_BGR2RGB)
            height, width, channel = color_frame.shape
            image = QImage(color_frame.data, width, height, QImage.Format_RGB888)
            self.updateFrame.emit(image)
            # time.sleep(0.01)

    def killWorker(self):
        self.status = False
        self.timer.stop()
        self.recognitionWorker.killWorker()
        self.quit()
        self.wait()
        self = None