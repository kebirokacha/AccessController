from PySide6.QtWidgets import QWidget ,QLabel
from PySide6.QtCore import Slot ,Qt
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
		for personInfo in personsInfo:
			if columnNum == 3:
				columnNum = 0
				rowNum += 1
			cardInfo = CardInfo(self, personInfo)
			self.cardInfoGrid.addWidget(cardInfo, rowNum,  columnNum)
			columnNum += 1

		if len(personsInfo)!=0 and len(personsInfo)<=3:
			columnNum = len(personsInfo)
			rowNum = 0
			for _ in range(columnNum ,6):
				if columnNum == 3:
					columnNum = 0
					rowNum += 1
				self.cardInfoGrid.addWidget(QWidget(), rowNum,  columnNum)
				columnNum += 1
		else:
			label = QLabel("DataBase Empty")
			label.setAlignment(Qt.AlignmentFlag.AlignCenter)		
			self.cardInfoGrid.addWidget(label)

	@Slot()
	def receiveData (self):
		self.PersonDetailsWidgetWindow = None
		self.populateTableWithPersonsInfo()