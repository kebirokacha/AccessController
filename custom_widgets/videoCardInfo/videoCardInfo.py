from PySide6.QtWidgets import QWidget
from .VideoCardInfo_ui import Ui_VideoCardInfo
from PySide6.QtMultimedia import QMediaPlayer
from moviepy.editor import VideoFileClip
import os
import time

class VideoCardInfo(Ui_VideoCardInfo ,QWidget):
	def __init__(self):
		super(VideoCardInfo ,self).__init__()
		self.setupUi(self)
		self.player = QMediaPlayer()
		self.player.durationChanged.connect(lambda duration : self.format_time(duration))
		self.videoSource = None
		self.videoFilePath = None
		self.videoDate = None
		self.videoTime = None
		self.videoSize = None

	def setupCard(self ,info:dict):
		videoFilePath = os.path.join(info['videoFolderPath'], info['videoFile'])
		videoSize = os.path.getsize(videoFilePath) # Size in bytes
		videoCreationTime = time.ctime(os.path.getctime(videoFilePath)) # Creation time in readable format
		# videoDuration = self.get_video_duration(videoFilePath) # Assuming you have a method to get video duration
		self.player.setSource(videoFilePath)
		# videoDuration = self.format_time(player.duration())
		self.sourceInfo.setText( info['videoFile'])
		self.sizeInfo.setText(str(videoSize)) # Convert size to a readable format if needed
		self.dateInfo.setText(videoCreationTime)
		# self.timeInfo.setText(str(videoDuration)) # Assuming video_duration is in a readable format
		self.videoFilePath = videoFilePath
		# print(f'videoDuration :{videoDuration}')

	def get_video_duration(self, video_path):
		with  VideoFileClip(video_path) as clip:
			duration = clip.duration # Duration in seconds
		return str(duration) + " seconds" # Convert to a readable format if needed
	
	def format_time(self ,ms):
		seconds = ms // 1000
		minutes = seconds // 60
		hours = minutes // 60
		self.timeInfo.setText(f"{hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}")