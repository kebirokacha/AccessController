from PySide6.QtWidgets import QApplication ,QMainWindow  ,QTabBar
from PySide6.QtGui import QIcon ,QPixmap 
from resources.ui.Main_ui import Ui_MainWindow
from custom_widgets.live.Live import Live
from custom_widgets.records.records import Records
from custom_widgets.dataBase.DataBase import DataBaseWidget
from custom_widgets.setting.Setting import Setting
import numpy as np
from deepface.DeepFace import represent

dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8) # Example dummy frame
_ = represent(dummy_frame, model_name='Facenet512', detector_backend='yolov8' ,enforce_detection=False)

class MainPage (Ui_MainWindow ,QMainWindow):

	def __init__(self):
		super(MainPage ,self).__init__()
		self.setupUi(self)
		self.setting = Setting()
		self.live = Live(self.setting)
		self.liveTab ,self.recordsTab ,self.dataBaseTab ,self.settingTab= None ,None ,None ,None
		self.liveTabName ,self.recordsTabName ,self.dataBaseTabName ,self.settingTabName = 'Live' ,'records' ,'Data Base' ,'Setting'
		self.liveTabIcon = QIcon(QPixmap('./resources/Icons/circle-dot.png'))
		self.recordsTabIcon = QIcon(QPixmap('./resources/Icons/Play-back.png'))
		self.settingTabIcon = QIcon(QPixmap('./resources/Icons/gear.png'))
		self.dataBaseTabIcon = QIcon(QPixmap('./resources/Icons/Data-Base.png'))
		self.tabWidget.setTabEnabled(0,False)
		self.tabWidget.currentChanged.connect(self.onTabChange)
		tabs = self.tabWidget.tabBar()
		tabs.setTabButton(0 ,QTabBar.ButtonPosition.RightSide ,None)
		tabs.setTabButton(1 ,QTabBar.ButtonPosition.RightSide ,None)
		self.tabWidget.tabCloseRequested.connect(lambda index :self.closeTab(index))
		self.liveButton.clicked.connect(self.setLiveTab)
		self.recordsButton.clicked.connect(self.setRecordsTab)
		self.dataBaseButton.clicked.connect(self.setDtataBaseTab)
		self.settingbutton.clicked.connect(self.setSettingTab)

	def closeTab(self ,index):
		if self.liveTab is not None and self.tabWidget.tabText(index) == self.liveTabName:
			self.liveTab.hide()

		elif self.recordsTab is not None and self.tabWidget.tabText(index) == self.recordsTabName:
			self.recordsTab.deleteLater()
			self.recordsTab = None

		elif self.dataBaseTab is not None and self.tabWidget.tabText(index) == self.dataBaseTabName:
			self.dataBaseTab.deleteLater()
			self.dataBaseTab = None

		elif self.settingTab is not None and self.tabWidget.tabText(index) == self.settingTabName:
			self.settingTab.hide()

		self.tabWidget.removeTab(index)

	def closeEvent(self, event):
		if self.setting is not None:
			self.setting.killAllThreads()
		if self.dataBaseTab is not None and self.dataBaseTab.PersonDetailsWidgetWindow is not None:
			self.dataBaseTab.PersonDetailsWidgetWindow.close()
		event.accept()

	def setLiveTab(self):
		if self.liveTab is None:
			self.liveTab = self.live
		elif self.liveTab.isHidden():
			self.liveTab.show
		self.tabWidget.addTab(self.liveTab ,self.liveTabIcon ,self.liveTabName)
		self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

	def setRecordsTab(self):
		if self.recordsTab is None:
			self.recordsTab = Records()
			self.tabWidget.addTab(self.recordsTab ,self.recordsTabIcon ,self.recordsTabName)
			self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

	def setDtataBaseTab(self):
		if self.dataBaseTab is None:
			self.dataBaseTab = DataBaseWidget()
			self.dataBaseTab.populateCardInfoGrid()
			self.tabWidget.addTab(self.dataBaseTab ,self.dataBaseTabIcon ,self.dataBaseTabName)
			self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

	def setSettingTab(self):
		if self.settingTab is None:
			self.settingTab = self.setting
		elif self.settingTab.isHidden():
			self.settingTab.show
		self.tabWidget.addTab(self.settingTab ,self.settingTabIcon ,self.settingTabName)
		self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

	def onTabChange(self ,index):
		print(f'tab changed {index}')
		if self.tabWidget.tabText(index) == self.recordsTabName:
			self.recordsTab.hideSideBar()
			#FIXME check it later if ()
			# self.recordsTab.fillListWidget()
		if self.tabWidget.tabText(index) == self.dataBaseTabName: 
			self.dataBaseTab.populateCardInfoGrid()	

if __name__=="__main__":
	import sys
	app = QApplication(sys.argv)
	myapp = MainPage()
	myapp.show()
	sys.exit(app.exec())