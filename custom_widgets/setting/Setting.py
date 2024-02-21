import cv2 as cv 
import cvzone
from ultralytics import YOLO
import face_recognition
from .Setting_ui import Ui_Form
from PySide6.QtCore import QThread, Qt, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import  QWidget
from databasemanager import DataBaseManager


class Setting (Ui_Form,QWidget):
    def __init__(self):
        super(Setting,self).__init__()
        self.setupUi(self)
        self.checkBox.stateChanged.connect(self.faceDetection)
        self.checkBox_2.stateChanged.connect(self.faceRecognition)
        self.checkBox_3.stateChanged.connect(self.tracking)
        database_manager = DataBaseManager()
        self.known_embeddings = database_manager.getEncodingArray()
        self.names = database_manager.getPersonNames()
    def faceDetection(self,state):
        
        # Slot function to handle checkbox state changes
        if state == 2:  # 2 corresponds to checked state
            print("Checkbox is checked")
        else:
            print("Checkbox is unchecked")
    def faceRecognition(self):
        print("reco is clicked ")
    def tracking (self):
        print ("tracking is clicked ")