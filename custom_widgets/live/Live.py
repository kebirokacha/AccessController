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
		self.refreshCapturesButton.clicked.connect(self.refreshCaptureList)
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
		for index ,camera in enumerate(cameras):
			captureid = camera.id().data().decode() 
			name = camera.description()
			cameraCardInfo = CameraCardInfo(name ,index)
			print(f"camera id are :{index}")
			itemList = QListWidgetItem(self.cameraListWidget)
			self.cameraListWidget.addItem(itemList)
			itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
			self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)
		else:
			#TODO: when there are no capture detected
			pass

	@Slot(str ,int)
	def addItem(self ,captureName:str ,captureId:int):
		captureId = int()
		if not self.isCameraInList(captureName ,captureId):
			cameraCardInfo = CameraCardInfo(captureName ,captureId)
			itemList = QListWidgetItem(self.cameraListWidget)
			self.cameraListWidget.insertItem(0 ,itemList)
			itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
			self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)

	def isCameraInList(self ,captureName:str ,captureId:int) -> bool:
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
	def removeItem(self ,captureName:str):
		for i in range(self.cameraListWidget.count()):
			item = self.cameraListWidget.item(i)
			cameraCardInfo:CameraCardInfo = self.cameraListWidget.itemWidget(item)
			if cameraCardInfo.cameraNameLabel.text() == captureName:
				self.cameraListWidget.takeItem(i)
				break
	
	def refreshCaptureList(self):
		cameras = QMediaDevices.videoInputs()
		busyCameras = self.setting.framReaderThreads.keys()
		availableCameras:dict[int ,str] = {}
		for index ,camera in enumerate(cameras):
			if index not in busyCameras and index not in availableCameras:
				availableCameras[index] = camera.description()
		self.cameraListWidget.clear()
		for captureId, captureName in availableCameras.items():
			cameraCardInfo = CameraCardInfo(captureName ,captureId)
			itemList = QListWidgetItem(self.cameraListWidget)
			self.cameraListWidget.addItem(itemList)
			itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
			self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)
		