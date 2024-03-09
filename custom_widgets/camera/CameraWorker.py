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
        self.cameraId = cameraId
        self.recognitionWorker = RecognitionWorker()
        self.sendFram.connect(self.recognitionWorker.faceRecognition)
        self.recognitionWorker.start()

        self.counter = 1
        self.fps = 0

    def run(self):
        cap = cv2.VideoCapture(self.cameraId)
        self.fps = cap.get(cv2.CAP_PROP_FPS)

        print(f"The FPS in the camera with ID {self.cameraId} are {self.fps}")
        while self.status:
            ret, frame = cap.read()
            if ret:
                frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height ,width ,channel = frameRgb.shape
                bytesPerLine = channel * width
                qimage = QImage(frameRgb.data ,width ,height ,bytesPerLine ,QImage.Format.Format_RGB888)
                self.updateFrame.emit(qimage)
                if self.counter % 30 == 0:
                    self.sendFram.emit(frame)
                self.counter += 1

    def killWorker(self):
        self.recognitionWorker.killWorker()
        self.status = False
        self.quit()
        self.wait()
        self = None