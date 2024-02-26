import cv2 as cv 
import cvzone
from ultralytics import YOLO
import face_recognition
from .Setting_ui import Ui_Form
from PySide6.QtCore import QThread
from PySide6.QtWidgets import  QWidget
from databasemanager import DataBaseManager
from custom_widgets.camera.CameraWidget import CameraWidget,Thread
class Setting (Ui_Form,QWidget):
    def __init__(self):
        super(Setting,self).__init__()
        self.setupUi(self)
        self.checkBox.stateChanged.connect(self.faceDetection)
        self.checkBox_2.stateChanged.connect(self.faceRecognition)
        self.checkBox_3.stateChanged.connect(self.tracking)
    
    def faceDetection(self,state):
        if state == 2: 
            print("Checkbox is checked")
        else:
            print("Checkbox is unchecked")
            # self.th.quit()

    def faceRecognition(self,state):
        if state == 2 :
            print ("okacha kfkjfosk is tchekdk ")

    def tracking (self):
        print ("tracking is clicked ")