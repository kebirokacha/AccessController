from PySide6.QtCore import Slot ,QThread
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import  QWidget
from .CameraWorker import  CameraWorker
from .RecognitionWorker import RecognitionWorker
from .Camera_ui import Ui_Camera
import cv2

class CameraWidget(Ui_Camera ,QWidget):
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FPS ,30)

    def __init__(self):
        super(CameraWidget, self).__init__()
        self.setupUi(self)
        self.cameraWorker = CameraWorker(self.capture)
        self.cameraWorker.update_frame.connect(self.setImage)
        self.recognitionWorker = RecognitionWorker(self.capture)
        # self.cameraWorker.faceDetected.connect(self.recognitionWorker.recognitionProcess)
        # self.recognitionWorker.recognizedFace.connect(self.handleRecognition)
        self.cameraWorker.start()
        self.recognitionWorker.start()
        self.cameraWorker.setPriority(QThread.Priority.HighestPriority)
        self.recognitionWorker.setPriority(QThread.Priority.LowPriority)

    def closeEvent(self, event):
        self.cameraWorker.killWorker()
        self.recognitionWorker.killWorker()
        event.accept()

    @Slot()
    def setImage(self, image):
        self.cameraLabel_01.setPixmap(QPixmap.fromImage(image))

    # @Slot()
    # def killThread(self):
    #     self.cameraWorker.status = False  # Set the status flag to stop the thread
    #     self.cameraWorker.quit()
    #     self.cameraWorker.wait()  # Wait for the thread to finish
    #     self.cameraWorker = None
        
    @Slot()
    def handleRecognition(self ,matches:list):
        print('matches are :\n',matches)


