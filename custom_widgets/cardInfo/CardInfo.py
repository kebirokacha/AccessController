from PySide6.QtWidgets import QWidget ,QDialog, QMessageBox
from databasemanager import DataBaseManager
from ..dataBase.DataBase import DataBaseWidget
from .CardInfo_ui import Ui_CardInfo
from PySide6.QtGui import QPixmap ,Qt 
from PySide6.QtCore import Signal
import os

class CardInfo (Ui_CardInfo ,QWidget):
	personDetailsSignal = Signal(dict)
	updateCardInfoGrid = Signal()
	dataBaseManager = DataBaseManager()
	def __init__(self ,personInfo:dict):
		super(CardInfo ,self).__init__()
		self.setupUi(self)
		self.personInfo = personInfo
		self.setupCardInfo()
		
	
	def setupCardInfo(self):
		if self.personInfo is not None:
			self.nameInfo.setText(str(self.personInfo['name']))
			self.birthdayInfo.setText(str(self.personInfo['birthday']))
			self.phoneInfo.setText(str(self.personInfo['phone']))
			self.emailInfo.setText(str(self.personInfo['email']))
			self.addressInfo.setText(str(self.personInfo['address']))
			self.editButton.clicked.connect(self.showPersonDetailsWidget)
			self.deleteButton.clicked.connect(self.confirmDeletePerson)
			self.loadPersonImage(self.personInfo['name'])
	
	def loadPersonImage(self, personName:str):
		personImageFolder = "person_pictures"
		sourcePath = os.path.join(personImageFolder ,personName, f"0.jpg")
		if os.path.exists(sourcePath):
			self.imageLabel.setPixmap(QPixmap(sourcePath).scaled(170,  210 ,Qt.AspectRatioMode.KeepAspectRatio))

	def showPersonDetailsWidget(self):
			self.personDetailsSignal.emit(self.personInfo)


	def confirmDeletePerson(self):
		dialog = QDialog(self)
		dialog.setWindowTitle("Confirm Deletion")

		message = QMessageBox(dialog)
		message.setIcon(QMessageBox.Question)
		message.setText(f"Are you sure you want to delete {self.personInfo['name']}?")
		message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		message.setDefaultButton(QMessageBox.No)

		result = message.exec_()
		if result == QMessageBox.Yes:
			self.dataBaseManager.deletePerson(self.personInfo['id'] ,self.personInfo['name'])
			self.updateCardInfoGrid.emit()