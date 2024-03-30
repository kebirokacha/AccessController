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
			customLabel  = CustomLabel('Loading' ,self.setting)
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
			
		captureIP = 'http://192.168.1.3:4747/video'
		cameraCardInfo = CameraCardInfo('My Phone' ,'http://192.168.1.3:4747/video')
		itemList = QListWidgetItem(self.cameraListWidget)
		self.cameraListWidget.addItem(itemList)
		itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
		self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)

		captureIP = 'http://192.168.1.4:4747/video'
		cameraCardInfo = CameraCardInfo('Mother Phone' ,'http://192.168.1.4:4747/video')
		itemList = QListWidgetItem(self.cameraListWidget)
		self.cameraListWidget.addItem(itemList)
		itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
		self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)

		captureIP = 'http://192.168.1.2:4747/video'
		cameraCardInfo = CameraCardInfo('Saadane Phone' ,captureIP)
		itemList = QListWidgetItem(self.cameraListWidget)
		self.cameraListWidget.addItem(itemList)
		itemList.setSizeHint(cameraCardInfo.minimumSizeHint())
		self.cameraListWidget.setItemWidget(itemList , cameraCardInfo)

	def closeCameras(self):
		for label in self.cameraLabels:
			label.close()

	@Slot(str)
	def removeItem(self ,cameraName):
		for i in range(self.cameraListWidget.count()):
			item = self.cameraListWidget.item(i)
			cameraCardInfo:CameraCardInfo = self.cameraListWidget.itemWidget(item)
			if cameraCardInfo.cameraNameLabel.text() == cameraName: # Assuming the camera ID is the text of the item
				self.cameraListWidget.takeItem(i)
				break
	