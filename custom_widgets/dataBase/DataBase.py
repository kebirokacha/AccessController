from PySide6.QtWidgets import QWidget 
from PySide6.QtCore import Slot ,QDate 
from .DataBase_ui import Ui_DataBase
from databasemanager import DataBaseManager


class DataBaseWidget(Ui_DataBase ,QWidget):
	dataBaseManager = DataBaseManager()
	PersonDetailsWidgetWindow = None
	
	def __init__(self):
		super(DataBaseWidget ,self).__init__()
		self.setupUi(self)
		
		self.registerIdButton.clicked.connect(self.showPersonDetailsWidget)
	
	def showPersonDetailsWidget(self):
		if self.PersonDetailsWidgetWindow is None:
			from ..personDetails.PersonDetails import PersonDetailsWidget
			self.PersonDetailsWidgetWindow = PersonDetailsWidget(self)
			self.PersonDetailsWidgetWindow.show()
			
		
	def populateTableWithPersonsInfo(self):
		from ..cardInfo.CardInfo import CardInfo
		# Get all persons' information from the database
		personsInfo = self.dataBaseManager.getAllPersonsInfo()
		# Clear the existing cardInfo widgets from cardInfoGrid
		while self.cardInfoGrid.count():
			item = self.cardInfoGrid.takeAt(0)
			widget = item.widget()
			if widget:
				widget.deleteLater()
		
		columnNum = 0
		rowNum = 0
		# Populate the cardInfoGrid with the data
			
		for personInfo in personsInfo:
			if columnNum == 3:
				columnNum = 0
				rowNum += 1
			# Initialize the cardInfoWidget
			cardInfo = CardInfo(self, personInfo)
			# Add it to the cardInfoGrid
			self.cardInfoGrid.addWidget(cardInfo, rowNum,  columnNum)
			columnNum += 1

	@Slot()
	def receiveData (self):
		print("receiveData Start")
		print('before')
		print(self.PersonDetailsWidgetWindow)
		self.PersonDetailsWidgetWindow = None
		print('after')
		self.populateTableWithPersonsInfo()
		print('receiveData END ')

