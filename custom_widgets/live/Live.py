from PySide6.QtWidgets import  QWidget ,QListWidgetItem
from ..cameraCardInfo.cameraCardInfo import CameraCardInfo
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtGui import Qt
from ..customLabel.customLabel import CustomLabel
from PySide6.QtCore import Slot
from .Live_ui import Ui_Live
from ..setting.Setting import Setting

class Live(Ui_Live ,QWidget):

	def __init__(self ,setting:Setting):
		self.cameraLabels:list[CustomLabel] = []
		super(Live, self).__init__()
		self.setupUi(self)
		self.setting = setting
		self.setCameraList()
		self.setUI()
		self.oneCamButton.clicked.connect(self.oneCam)
		self.twoCamButton.clicked.connect(self.twoCam)
		self.fourCamButton.clicked.connect(self.fourCam)

	def setUI(self):
		for _ in range(4):
			customLabel  = CustomLabel(self.setting)
			customLabel.addItem.connect(self.addItem)
			customLabel.removeItem.connect(self.removeItem)
			customLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
			self.cameraLabels.append(customLabel)

		for i, label in enumerate(self.cameraLabels):
			row = i // 2
			col = i % 2
			self.cameraGrid.addWidget(label, row, col)
		for label in self.cameraLabels[1:]:
			label.hide()
	
	def oneCam(self):
		for label in self.cameraLabels[1:]:
			label.hide()

	def twoCam(self):
		self.cameraLabels[1].show()
		for label in self.cameraLabels[2:]:
			label.hide()
	
	def fourCam(self):
		for label in self.cameraLabels[1:]:
			label.show()

	def setCameraList(self):
		cameras = QMediaDevices.videoInputs()
		for camera in cameras:
			name = camera.description()
			cameraCardInfo = CameraCardInfo(name ,camera.id().data().decode())
			print(f"camera id are :{camera.id().data().decode()}")
			itemList = QListWidgetItem(self.cameraListWidget)
			self.cameraListWidget.addItem(itemList)
			itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
			self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)
		#FIXME: Testing purpose (Remove Later)
			
		captureIP = 'http://192.168.222.11:4747/video'
		cameraCardInfo = CameraCardInfo('My Phone' ,captureIP)
		itemList = QListWidgetItem(self.cameraListWidget)
		self.cameraListWidget.addItem(itemList)
		itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
		self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)

		captureIP = 'http://192.168.1.4:4747/video'
		cameraCardInfo = CameraCardInfo('Mother Phone' ,captureIP)
		itemList = QListWidgetItem(self.cameraListWidget)
		self.cameraListWidget.addItem(itemList)
		itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
		self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)

		captureIP = 'http://192.168.42.129:4747/video'
		cameraCardInfo = CameraCardInfo('Saadane Phone' ,captureIP)
		itemList = QListWidgetItem(self.cameraListWidget)
		self.cameraListWidget.addItem(itemList)
		itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
		self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)

	@Slot(str ,str)
	def addItem(self ,captureName:str ,captureId):
		if not self.isCameraInList(captureName ,captureId):
			cameraCardInfo = CameraCardInfo(captureName ,captureId)
			itemList = QListWidgetItem(self.cameraListWidget)
			self.cameraListWidget.addItem(itemList)
			itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
			self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)

	def isCameraInList(self ,captureName ,captureId) -> bool:
		for i in range(self.cameraListWidget.count()):
			item = self.cameraListWidget.item(i)
			cameraCardInfo:CameraCardInfo = self.cameraListWidget.itemWidget(item)
			if cameraCardInfo.cameraNameLabel.text() == captureName and cameraCardInfo.cameraId == captureId:
				return True
		return False
	
	def getCustomLabel(self ,captureId) -> CustomLabel:
		for customLabel in self.cameraLabels:
			if customLabel.captureId == captureId:
				return customLabel
		return None 
	
	@Slot(str)
	def removeItem(self ,captureName):
		for i in range(self.cameraListWidget.count()):
			item = self.cameraListWidget.item(i)
			cameraCardInfo:CameraCardInfo = self.cameraListWidget.itemWidget(item)
			if cameraCardInfo.cameraNameLabel.text() == captureName:
				self.cameraListWidget.takeItem(i)
				break
	