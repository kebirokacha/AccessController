from PySide6.QtWidgets import QWidget ,QLabel
from PySide6.QtCore import Slot ,Qt ,Signal
from .DataBase_ui import Ui_DataBase
from databasemanager import DataBaseManager

class DataBaseWidget(Ui_DataBase ,QWidget):
	updateInfo = Signal()
	PersonDetailsWidgetWindow = None
	
	def __init__(self):
		super(DataBaseWidget ,self).__init__()
		self.setupUi(self)
		self.registerIdButton.clicked.connect(lambda : self.showPersonDetailsWidget())
	
	def showPersonDetailsWidget(self ,personInfo:dict = None):
		if self.PersonDetailsWidgetWindow is None:
			from ..personDetails.PersonDetails import PersonDetailsWidget
			self.PersonDetailsWidgetWindow = PersonDetailsWidget()
			self.PersonDetailsWidgetWindow.sendInformation.connect(self.receiveData)
			if personInfo is not None:
				self.PersonDetailsWidgetWindow.fillPersonInfo(personInfo)
			self.PersonDetailsWidgetWindow.show()

	def populateCardInfoGrid(self):
		from ..cardInfo.CardInfo import CardInfo
		dataBaseManager = DataBaseManager()
		personsInfo = dataBaseManager.getAllPersonsInfo()
		self.clearCardInfoGrid()
		columnNum = 0
		rowNum = 0	
		for personInfo in personsInfo:
			if columnNum == 3:
				columnNum = 0
				rowNum += 1
			cardInfo = CardInfo(personInfo)
			cardInfo.personDetailsSignal.connect(lambda :self.showPersonDetailsWidget(personInfo))
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

	def clearCardInfoGrid(self):
		while self.cardInfoGrid.count():
			item = self.cardInfoGrid.takeAt(0)
			widget = item.widget()
			if widget:
				widget.deleteLater()

	@Slot()
	def receiveData (self):
		self.PersonDetailsWidgetWindow = None
		self.populateCardInfoGrid()
		self.updateInfo.emit()