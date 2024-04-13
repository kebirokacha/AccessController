from PySide6.QtWidgets import QWidget ,QFileDialog ,QLabel
from PySide6.QtCore import Signal ,QDate ,Qt ,QStandardPaths
from ..dialog.ErrorDialog import ErrorDialog
from .PersonDetails_ui import Ui_PersonDetails
from databasemanager import DataBaseManager
from PySide6.QtGui import QPixmap
from deepface.DeepFace import represent
import shutil
import  numpy as np
import os
import re


class PersonDetailsWidget(Ui_PersonDetails, QWidget):
	sendInformation = Signal()
	dataBaseManager = DataBaseManager()
	picturesPaths =[]
	personInfo  = None  
	MAXPICTURES = 6

	def __init__(self):
		super(PersonDetailsWidget, self).__init__()
		self.setupUi(self)

		self.submitButton.clicked.connect(self.processPersonDetails)
		self.selectPicturesButton.clicked.connect(self.selectPictures)
		self.resetButton.clicked.connect(self.resetPictures)
		self.cancelButton.clicked.connect(self.closePersonDetailsWidget)

		
	def selectPictures(self):
		filePaths = QFileDialog.getOpenFileNames(
												self ,
												caption='Select Person Pictures' ,
												dir=QStandardPaths.writableLocation(QStandardPaths.StandardLocation.PicturesLocation) ,
												filter='Images (*.png *.xpm *.jpg *.jpeg)'
										   )
		if filePaths:
			filePaths = filePaths[0]
			print(f"the file directory is : {filePaths}")
			print(f"the file directory is : {self.picturesPaths}")

			# Check if the total number of selected pictures exceeds MAXPICTURES
			if len(self.picturesPaths) >= self.MAXPICTURES or len(filePaths)  > self.MAXPICTURES:
				self.showErrorDialog("Too much pictures", f"You can select up to {self.MAXPICTURES} Pictures")
				return
			else:
				# If there are already pictures, add the new ones only if it doesn't exceed MAXPICTURES
				if self.picturesPaths:
					new_pictures = filePaths[:self.MAXPICTURES - len(self.picturesPaths)] if len(self.picturesPaths) + len(filePaths) > self.MAXPICTURES else filePaths
					self.picturesPaths.extend(new_pictures)
				else:
					self.picturesPaths = filePaths
				self.displayPicturesInGrid(self.picturesPaths)
			# self.personPictureLabel.setPixmap(QPixmap(self.imagePath).scaled(200, 250))

	def resetPictures(self):
		self.clearPictureInGrid()
		self.picturesPaths = []

	def displayPicturesInGrid(self ,picturesPaths:list[str]):
		# Clear the gridPictures layout before adding new images
		self.clearPictureInGrid()
		# Add the images to the gridPictures layout
		for i, path in enumerate(picturesPaths):
			print(f"path is {path}")
			label = QLabel()
			pixmap = QPixmap(path)
			label.setPixmap(pixmap.scaled(200, 250, Qt.AspectRatioMode.KeepAspectRatio))
			self.gridPictures.addWidget(label, i // 3, i % 3) # Adjust the grid layout as needed
			
	def clearPictureInGrid(self):
		while self.gridPictures.count():
			item = self.gridPictures.takeAt(0)
			widget = item.widget()
			if widget:
				widget.deleteLater()

	def copyImageToPersonFolder(self, imagePath:str, personName:str):
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
			self.showErrorDialog("Error Validation" ,"Please fill the Name.")
			return
		if self.phoneNumberInput.text() == "":
			self.showErrorDialog("Error Validation" ,"Please fill the phone Number.")
			return
		if self.emailInput.text() == "":
			self.showErrorDialog("Error Validation" ,"Please fill the Email.")
			return
		if self.adresseInput.text() == "":
			self.showErrorDialog("Error Validation" ,"Please fill the adresse .")
			return
		if not self.picturesPaths  and self.personInfo is None:
			self.showErrorDialog("Error Validation" ,"Please select Pictures.")
			return
		
		if not self.validatePhoneNumber(self.phoneNumberInput.text()):
			self.showErrorDialog("Error Validation", "Please enter a valid phone number.")
			return
		
		if not self.validateEmail(self.emailInput.text()):
			self.showErrorDialog("Error Validation", "Please enter a valid email address.")
			return
		existingPerson = self.dataBaseManager.getPersonByName(self.nameInput.text())
		if existingPerson:
			self.showErrorDialog( "Person Already Exists", "A person with this name already exists in the database.")
			return
		
		if self.personInfo is None:
			existingPhone = self.dataBaseManager.getPersonByPhone(self.phoneNumberInput.text())
			if existingPhone:
				self.showErrorDialog("Phone Number Already Exists", "A person with this phone number already exists in the database.")
				return
			existingEmail = self.dataBaseManager.getPersonByEmail(self.emailInput.text())
			if existingEmail:
				self.showErrorDialog("Email Already Exists", "A person with this email already exists in the database.")
				return
			embeddingsList = self.createEmbeddings(self.picturesPaths)
			self.dataBaseManager.addPerson(
				self.nameInput.text(), 
				self.birthdayInput.date().toString('yyyy-MM-dd'), 
				self.phoneNumberInput.text(), 
				self.emailInput.text(), 
				self.adresseInput.text(), 
				embeddingsList,
				self.picturesPaths
			)
		else:
			if not self.picturesPaths:				
				self.dataBaseManager.modifyPersonWithoutEmbedding(
					self.personInfo['id'],
					self.nameInput.text(),
					self.personInfo['name'],
					self.birthdayInput.date().toString('yyyy-MM-dd'), 
					self.phoneNumberInput.text(), 
					self.emailInput.text(), 
					self.adresseInput.text()
				)
			else:
				embeddingsList = self.createEmbeddings(self.picturesPaths)
				self.dataBaseManager.modifyPerson(
					self.personInfo['id'],
					self.nameInput.text(),
					self.personInfo['name'],
					self.birthdayInput.date().toString('yyyy-MM-dd'), 
					self.phoneNumberInput.text(), 
					self.emailInput.text(), 
					self.adresseInput.text(), 
					embeddingsList,
					self.picturesPaths
				)
		self.sendInformation.emit()
		self.close()

	def createEmbeddings(self ,picturesPaths:list) -> list[list]:
		embeddingsList = []
		for picturePath in picturesPaths:
			try:
				embedding = represent(picturePath ,model_name='Facenet512' ,detector_backend='yolov8')[0]["embedding"]
				embeddingsList.append(embedding)
			except:
				print('face not detected !!!!!')
		return embeddingsList
		
	def showErrorDialog(self ,title:str ,message:str):
		dialog = ErrorDialog(title ,message, self)
		dialog.exec()

	def fillPersonInfo(self ,personInfo:dict):
		self.personInfo = personInfo
		self.submitButton.setText("Modify")
		self.nameInput.setText(personInfo['name'])
		self.birthdayInput.setDate(QDate.fromString(personInfo['birthday'], 'yyyy-MM-dd'))
		self.phoneNumberInput.setText(str(personInfo['phone']))
		self.emailInput.setText(personInfo['email'])
		self.adresseInput.setText(personInfo['address'])
		self.loadPersonPictures(personInfo['name'])
	
	def loadPersonPictures(self, personName:str):
		personImageFolder = os.path.join("person_pictures", personName)
		if not os.path.exists(personImageFolder):
			print(f"No images found for person: {personName}")
			return

		# Clear the gridPictures layout before adding new images
		self.clearPictureInGrid()

		# List all image files in the person's image folder
		imageFiles = [f for f in os.listdir(personImageFolder) if f.endswith(('.png' ,'.jpg' ,'.jpeg' ,'.xpm'))]

		# Add the images to the gridPictures layout
		for i, imageFile in enumerate(imageFiles):
			imagePath = os.path.join(personImageFolder, imageFile)
			label = QLabel()
			pixmap = QPixmap(imagePath)
			label.setPixmap(pixmap.scaled(200, 250, Qt.AspectRatioMode.KeepAspectRatio))
			self.gridPictures.addWidget(label, i // 3, i % 3) # Adjust the grid layout as needed

	def closePersonDetailsWidget(self):
		self.sendInformation.emit()
		self.close()

	def closeEvent(self, event):
		self.sendInformation.emit()
		event.accept()