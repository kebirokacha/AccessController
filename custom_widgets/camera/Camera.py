from PySide6.QtWidgets import  QWidget ,QListWidgetItem
from ..cameraCardInfo.cameraCardInfo import CameraCardInfo
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtGui import QPixmap ,QImage  ,Qt
from ..customLabel.DraggableLabel import DraggableLabel
from PySide6.QtCore import Slot
from .Camera_ui import Ui_Camera

class CameraWidget(Ui_Camera ,QWidget):

	def __init__(self):
		self.cameraLabels:list[DraggableLabel] = []
		super(CameraWidget, self).__init__()
		self.setupUi(self)
		self.setCameraList()
		self.setUI()
		self.oneCamButton.clicked.connect(self.oneCam)
		self.twoCamButton.clicked.connect(self.twoCam)
		self.fourCamButton.clicked.connect(self.fourCam)

	def setUI(self):
		for _ in range(4):
			customLabel  = DraggableLabel('Loading' ,self.cameraListWidget)
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

	def closeCamera(self):
		for label in self.cameraLabels:
			if label.cameraWorker is not None and label.cameraWorker.isRunning():
				label.killWorker()

	@Slot(str)
	def removeItem(self ,cameraName):
		for i in range(self.cameraListWidget.count()):
			item = self.cameraListWidget.item(i)
			draggableLabel:DraggableLabel = self.cameraListWidget.itemWidget(item)
			print(f"item text is {draggableLabel.cameraNameLabel.text()} cameraName is {cameraName}")
			if draggableLabel.cameraNameLabel.text() == cameraName: # Assuming the camera ID is the text of the item
				self.cameraListWidget.takeItem(i)
				break
	