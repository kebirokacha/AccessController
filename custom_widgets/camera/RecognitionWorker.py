from PySide6.QtCore import QThread, Signal ,Slot ,QTimer
from databasemanager import DataBaseManager
from ultralytics import YOLO
import face_recognition
import cv2
import cvzone
import time

class RecognitionWorker(QThread):
	

    def __init__(self , capture ,parent=None):
        QThread.__init__(self, parent)
        self.timer = QTimer()
        self.capture = capture
        self.databaseManager = DataBaseManager()
        self.knownEncodings = self.databaseManager.getEncodingArray()
        self.model = YOLO('resources/yolov8n-face.pt')
        self.status = True
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
                    h, w = y2 - y1, x2 - x1
                    # cvzone.cornerRect(fram, [x1, y1, w, h], l=30,rt=5,t=1,colorC=(255,255,255))
                    face_encoding = face_recognition.face_encodings(fram ,[(y1, x2, y2 ,x1)])[0]
                    time.sleep(1)
                    matches = face_recognition.compare_faces(self.knownEncodings, face_encoding)
                    time.sleep (0.01)
                    print(matches)
            


    def killWorker(self):
        self.status = False
        self.quit()
        self.wait()
        self = None