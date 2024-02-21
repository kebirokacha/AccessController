from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal ,QDate 
import face_recognition
from ..dialog.ErrorDialog import ErrorDialog
from .PersonDetails_ui import Ui_PersonDetails
from ..dataBase.DataBase import DataBaseWidget
from databasemanager import DataBaseManager
import cv2 as cv
import shutil
import os
import re

class PersonDetailsWidget(Ui_PersonDetails, QWidget):
    sendInformation = Signal()
    dataBaseManager = DataBaseManager()
    imagePath ,personInfo ,errorDialog = None ,None ,None
    
    def __init__(self, Widget: DataBaseWidget):
        super(PersonDetailsWidget, self).__init__()
        self.setupUi(self)

        self.addButton.clicked.connect(self.processPersonDetails)
        self.selectImageButton.clicked.connect(self.selectImage)
        self.cancelButton.clicked.connect(self.closePersonDetailsWidget)
        self.sendInformation.connect(Widget.receiveData)
        
    def selectImage(self):
        file_directory = QFileDialog.getOpenFileName(self, 'Select Person Image', filter='Images (*.png *.xpm *.jpg *.jpeg)')
        if file_directory[0] != "":
            self.imagePath = file_directory[0]
            self.personPictureLabel.setPixmap(QPixmap(self.imagePath).scaled(200, 250))

    def loadPersonImage(self, personName):
        personImageFolder = "person_images"
        sourcePath = os.path.join(personImageFolder, f"{personName}.jpg")
        if os.path.exists(sourcePath):
            self.personPictureLabel.setPixmap(QPixmap(sourcePath).scaled(200,  250))

    def copyImageToPersonFolder(self, imagePath, personName):
        personImageFolder = "person_images"
        if not os.path.exists(personImageFolder):
            os.makedirs(personImageFolder)
        destinationPath = os.path.join(personImageFolder, f"{personName}.jpg")
        shutil.copy2(imagePath, destinationPath)

    def validatePhoneNumber(self, phoneNumber):
        # Regex pattern for international phone numbers
        pattern = r'^\+\d{1,3}\d{1,14}$'
        return re.match(pattern, phoneNumber) is not None

    def validateEmail(self, email):
        # Regex pattern for email addresses
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def processPersonDetails(self):
        if self.nameInput.text() == "":
            self.showErrorDialog("Error Validation" ,"Please fill the nameInput.")
            return
        if self.phoneNumberInput.text() == "":
            self.showErrorDialog("Error Validation" ,"Please fill the phoneNumberInput.")
            return
        if self.emailInput.text() == "":
            self.showErrorDialog("Error Validation" ,"Please fill the emailInput.")
            return
        if self.adresseInput.text() == "":
            self.showErrorDialog("Error Validation" ,"Please fill the adresseInput.")
            return
        if self.imagePath is None and self.personInfo is None:
            self.showErrorDialog("Error Validation" ,"Please select an image.")
            return
        
        if not self.validatePhoneNumber(self.phoneNumberInput.text()):
            self.showErrorDialog("Error Validation", "Please enter a valid phone number.")
            return
        
        if not self.validateEmail(self.emailInput.text()):
            self.showErrorDialog("Error Validation", "Please enter a valid email address.")
            return
        #TODO: Add Validation for email and number
        
        if self.personInfo is None:
            existingPerson = self.dataBaseManager.getPersonByName(self.nameInput.text())
            if existingPerson:
                self.showErrorDialog( "Person Already Exists", "A person with this name already exists in the database.")
                return
            existingPhone = self.dataBaseManager.getPersonByPhone(self.phoneNumberInput.text())
            if existingPhone:
                self.showErrorDialog("Phone Number Already Exists", "A person with this phone number already exists in the database.")
                return
            existingEmail = self.dataBaseManager.getPersonByEmail(self.emailInput.text())
            if existingEmail:
                self.showErrorDialog("Email Already Exists", "A person with this email already exists in the database.")
                return
            image = cv.imread(self.imagePath)
            personEncoding = face_recognition.face_encodings(image) 
            self.copyImageToPersonFolder(self.imagePath, self.nameInput.text())
            self.dataBaseManager.addPerson(
                self.nameInput.text(), 
                self.birthdayInput.date().toString('yyyy-MM-dd'), 
                self.phoneNumberInput.text(), 
                self.emailInput.text(), 
                self.adresseInput.text(), 
                personEncoding
            )

        else:
            if self.imagePath is None:
                oldName = self.personInfo['name']
                newName = self.nameInput.text()
                if oldName != newName:
                    existingPerson = self.dataBaseManager.getPersonByName(self.nameInput.text())
                    if existingPerson:
                        self.showErrorDialog( "Person Already Exists", "A person with this name already exists in the database.")
                        return
                    personImageFolder = "person_images"
                    oldSourcePath = os.path.join(personImageFolder, f"{oldName}.jpg")
                    newSourcePath = os.path.join(personImageFolder, f"{newName}.jpg")
                    os.rename(oldSourcePath, newSourcePath)
                self.dataBaseManager.modifyPersonWithoutEncoding(
                    self.personInfo['id'],
                    self.nameInput.text(), 
                    self.birthdayInput.date().toString('yyyy-MM-dd'), 
                    self.phoneNumberInput.text(), 
                    self.emailInput.text(), 
                    self.adresseInput.text()
                )
            else:
                print('replace image + update  all info')
                image = cv.imread(self.imagePath)
                personEncoding = face_recognition.face_encodings(image) 
                print('person encoding are :\n',personEncoding)
                self.copyImageToPersonFolder(self.imagePath, self.nameInput.text())
                self.dataBaseManager.modifyPerson(
                    self.personInfo['id'],
                    self.nameInput.text(), 
                    self.birthdayInput.date().toString('yyyy-MM-dd'), 
                    self.phoneNumberInput.text(), 
                    self.emailInput.text(), 
                    self.adresseInput.text(), 
                    personEncoding
                )
        self.sendInformation.emit()
        self.close()
        
    def showErrorDialog(self ,title ,message):
        dialog = ErrorDialog(title ,message, self)
        dialog.exec()

    def fillPersonInfo(self ,personInfo):
        self.personInfo = personInfo
        self.addButton.setText("Modify")
        self.nameInput.setText(personInfo['name'])
        self.birthdayInput.setDate(QDate.fromString(personInfo['birthday'], 'yyyy-MM-dd'))
        self.phoneNumberInput.setText(str(personInfo['phone']))
        self.emailInput.setText(personInfo['email'])
        self.adresseInput.setText(personInfo['address'])
        self.loadPersonImage(personInfo['name'])
    
    def closePersonDetailsWidget(self):
        self.sendInformation.emit()
        self.close()

    def closeEvent(self, event):
        self.sendInformation.emit()
        event.accept()