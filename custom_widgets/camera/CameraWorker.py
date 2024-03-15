from PySide6.QtCore import QThread, Signal ,QThreadPool 
from PySide6.QtGui import QImage
from .RecognitionWorker import RecognitionWorker

import cv2

class CameraWorker(QThread):
    updateFrame = Signal(QImage)
    sendFram = Signal(cv2.Mat)

    def __init__(self, cameraId, parent=None):
        QThread.__init__(self, parent)
        self.status = True
        self.cap = None
        self.cameraId = cameraId
        self.recognitionWorker = RecognitionWorker()
        self.sendFram.connect(self.recognitionWorker.faceRecognition)
        self.counter: int = 1

    def run(self):
        self.recognitionWorker.start()
        self.cap = cv2.VideoCapture(self.cameraId)
        fps = self.cap.get(cv2.CAP_PROP_FPS)

        print(f"The FPS in the camera with ID {self.cameraId} are {fps}")
        while self.status:
            ret, frame = self.cap.read()
            if ret:
                frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height ,width ,channel = frameRgb.shape
                bytesPerLine = channel * width
                qimage = QImage(frameRgb.data ,width ,height ,bytesPerLine ,QImage.Format.Format_RGB888)
                self.updateFrame.emit(qimage)
                if self.counter % 30 == 0:
                    self.sendFram.emit(frame)
                    self.counter = 0
                self.counter += 1
            
            

    def killWorker(self):
        self.status = False
        if self.cap is not None:
            self.cap.release()
        self.quit()
        self.wait()
        self.recognitionWorker.killWorker()
        self = None