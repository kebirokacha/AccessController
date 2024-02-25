from PySide6.QtCore import QThread, Signal
from databasemanager import DataBaseManager
from .CameraWorker import CameraWorker
import face_recognition
import cv2 as cv

class RecognitionWorker(QThread):
    recognizedFace = Signal(list) 
    databaseManager = DataBaseManager()
    knownEncodings = databaseManager.getEncodingArray()
    status = True

    def __init__(self ,cameraWorker:CameraWorker , parent=None):
        QThread.__init__(self, parent)
        self.cameraWorker = cameraWorker

    def run(self):
        while self.status:
            fram ,faceLocation = self.cameraWorker.faceDetected
            if fram is not None:
                # Perform face recognition here
                # For demonstration, let's assume we have a function `recognize_face`
                # Create an encoding for the extracted face
					#(top, right, bottom, left)
                face_encoding = face_recognition.face_encodings(fram ,[faceLocation])[0]
                matches = face_recognition.compare_faces(self.knownEncodings, face_encoding)
                self.recognizedFace.emit(matches)

    def killWorker(self):
        self.status = False
        self.quit()
        self.wait()
        self = None