
from PySide6.QtWidgets import  QWidget
from .Setting_ui import Ui_Setting
from databasemanager import DataBaseManager


class Setting (Ui_Setting,QWidget):
    def __init__(self):
        super(Setting,self).__init__()
        self.setupUi(self)
        self.checkBox.stateChanged.connect(self.faceDetection)
        self.checkBox_2.stateChanged.connect(self.faceRecognition)
        self.checkBox_3.stateChanged.connect(self.tracking)
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