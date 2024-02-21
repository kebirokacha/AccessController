from PySide6.QtWidgets import QWidget ,QDialog, QMessageBox
from databasemanager import DataBaseManager
from ..dataBase.DataBase import DataBaseWidget
from .CardInfo_ui import Ui_CardInfo
from PySide6.QtGui import QPixmap
import os

class CardInfo (Ui_CardInfo ,QWidget):
	personInfo = None
	dataBaseWidget = None
	dataBaseManager = DataBaseManager()
	def __init__(self ,dataBaseWidget:DataBaseWidget ,personInfo):
		super(CardInfo ,self).__init__()
		self.setupUi(self)
		self.personInfo = personInfo
		self.dataBaseWidget = dataBaseWidget
		self.setupCardInfo()
		
	
	def setupCardInfo(self):
		self.nameInfo.setText(str(self.personInfo['name']))
		self.birthdayInfo.setText(str(self.personInfo['birthday']))
		self.phoneInfo.setText(str(self.personInfo['phone']))
		self.emailInfo.setText(str(self.personInfo['email']))
		self.addressInfo.setText(str(self.personInfo['address']))
		self.editButton.clicked.connect(self.showPersonDetailsWidget)
		self.deleteButton.clicked.connect(self.confirmDeletePerson)
		self.loadPersonImage(self.personInfo['name'])
	
	def loadPersonImage(self, personName):
		personImageFolder = "person_images"
		sourcePath = os.path.join(personImageFolder, f"{personName}.jpg")
		if os.path.exists(sourcePath):
			self.imageLabel.setPixmap(QPixmap(sourcePath).scaled(170,  210))

	def showPersonDetailsWidget(self):
			if self.dataBaseWidget.PersonDetailsWidgetWindow is None:
				from ..personDetails.PersonDetails import PersonDetailsWidget
				self.dataBaseWidget.PersonDetailsWidgetWindow = PersonDetailsWidget(self.dataBaseWidget)
				self.dataBaseWidget.PersonDetailsWidgetWindow.fillPersonInfo(self.personInfo)
				self.dataBaseWidget.PersonDetailsWidgetWindow.show()

	def deletePersonImage(self, personName):
		# Define the source folder for person images
		personImageFolder = "person_images"
		# Construct the source file path
		sourcePath = os.path.join(personImageFolder, f"{personName}.jpg")
		# Check if the image file exists
		if os.path.exists(sourcePath):
			# Delete the image file
			os.remove(sourcePath)

	def confirmDeletePerson(self):
		dialog = QDialog(self)
		dialog.setWindowTitle("Confirm Deletion")
		# dialog.setWindowModality(WindowModal)

		message = QMessageBox(dialog)
		message.setIcon(QMessageBox.Question)
		message.setText(f"Are you sure you want to delete {self.personInfo['name']}?")
		message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		message.setDefaultButton(QMessageBox.No)

		result = message.exec_()
		if result == QMessageBox.Yes:
			self.deletePersonImage(self.personInfo['name'])
			self.dataBaseManager.deletePerson(self.personInfo['id'])
			self.dataBaseWidget.populateTableWithPersonsInfo()