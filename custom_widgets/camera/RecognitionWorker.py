from PySide6.QtCore import QThread, Signal ,Slot ,QTimer
from databasemanager import DataBaseManager
from ultralytics import YOLO
import face_recognition
import cv2 as cv

class RecognitionWorker(QThread):
    recognizedFace = Signal(list) 
    databaseManager = DataBaseManager()
    knownEncodings = databaseManager.getEncodingArray()
    model = YOLO('resources/yolov8n-face.pt')
    status = True

    def __init__(self ,capture ,parent=None):
        QThread.__init__(self, parent)
        self.timer = QTimer()
        self.capture = capture
        # self.timer.timeout.connect(self.processFrames)
        # self.timer.start(1000)

    def run(self):
        while self.status:
            ret, fram = self.capture.read()
            if not ret:
                continue
            results = self.model.predict(fram, verbose=False)
            for info in results:
                for box in info.boxes:
                    #(left ,top, right, bottom)
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                face_encoding = face_recognition.face_encodings(fram ,[(y1, x2, y2 ,x1)])[0]
                matches = face_recognition.compare_faces(self.knownEncodings, face_encoding)
            print(matches)
        # self.recognizedFace.emit(matches)
            


    def killWorker(self):
        self.status = False
        self.quit()
        self.wait()
        self = None