import cv2 as cv
from ultralytics import YOLO
import cvzone
import face_recognition
from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import  QWidget
from .Camera_ui import Ui_Camera
from databasemanager import DataBaseManager
import numpy as np

class CameraWidget(Ui_Camera ,QWidget):

    def __init__(self):
        super(CameraWidget, self).__init__()
        self.setupUi(self)
        self.database_manager = DataBaseManager()
        self.known_embeddings = DataBaseManager().getEncodingArray()
        self.names = DataBaseManager().getPersonNames()
        self.model = YOLO('yolov8n-face.pt')
        self.th = Thread(self)
        self.showLive1.stateChanged.connect(self.showlive)
        self.FaceYolo.stateChanged.connect(self.showFaceDetect)
        self.th.update_frame.connect(self.setImage)
        

    def showlive(self,state):
        if state == 2:
            self.th.start()
        
    def showFaceDetect(self,state):
        if state == 2 :
           self.th.frames.connect(self.faceDetect)
        
   
    @Slot()
    def setImage(self, image):
        self.cameraLabel_01.setPixmap(QPixmap.fromImage(image))
    @Slot(QImage)
    def faceDetect(self,image):
            buffer = memoryview(image.bits()).cast("B")
            frame = np.array(buffer).reshape((image.height(), image.width(), 3))
            results = self.model.predict(frame)
                
            for info in results:
                parameters = info.boxes
                for box in parameters:
                    #(left ,top, right, bottom)
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    h, w = y2 - y1, x2 - x1
                    cvzone.cornerRect(frame, [x1, y1, w, h], l=30,rt=0,t=1,colorC=(255,255,255))




    
class Thread(QThread):
    update_frame= Signal(QImage)
    frames =Signal(QImage)
    def __init__(self, parent=None):
        QThread.__init__(self, parent) 
    def run(self):
        self.capture = cv.VideoCapture(0)
        while True:
            ret, frame = self.capture.read()
           
            if not ret:
                continue
            height, width,channel = frame.shape
            image = QImage(frame.data, width, height, QImage.Format_RGB888)
            self.update_frame.emit(image)
            self.frames.emit(image)
                # results = self.model.predict(frame)
                
                # for info in results:
                #     parameters = info.boxes
                #     for box in parameters:
                #         #(left ,top, right, bottom)
                #         x1, y1, x2, y2 = box.xyxy[0]
                #         x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                #         h, w = y2 - y1, x2 - x1
                #         cvzone.cornerRect(frame, [x1, y1, w, h], l=30,rt=0,t=1,colorC=(255,255,255))

                        
                        # Extract the face from the frame
                        # face = frame[y1:y2, x1:x2]

                        # Create an encoding for the extracted face
                        #(top, right, bottom, left)
                        # face_encoding = face_recognition.face_encodings(frame ,[(y1, x2, y2 ,x1)])[0]

                        # # Compare the face encoding with the known encodings
                        # matches = face_recognition.compare_faces(self.known_embeddings, face_encoding)

                        # name = "Unknown"

                        # if True in matches:
                        #     # print ('kebir okacha abdel illah ')
                        #     first_match_index = matches.index(True)
                        #     name = self.names[first_match_index]
                        #     print('trueeeeeeeeeeeeee')
                            
                # height, width,channel = frame.shape
                # image = QImage(frame.data, width, height, QImage.Format_RGB888)
                # self.update_frame.emit(image)
            
                # self.frame2.emit(frame)
      
        


