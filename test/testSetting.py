from PySide6.QtWidgets import QApplication
from custom_widgets.setting.Setting import Setting
import unittest


class MyTestCase(unittest.TestCase):
	def setUp(self):
		self.app = QApplication.instance() or QApplication([])
		self.setting = Setting()
		self.savedEmail = 'bahrib665@gmail.com'

	def test_SaveEmail(self):
		# set label value
		self.setting.emailInput.setText(self.savedEmail)
		self.setting.saveEmail()
		result = self.setting.loadSavedEmail() == self.savedEmail
		self.assertEqual(result, True)

	def test_LoadMailOnce(self):
		result = self.setting.loadSavedEmail() == self.savedEmail
		self.assertEqual(result, True)
	
	def test_LoadMailTwice(self):
		self.setting.loadSavedEmail() == self.savedEmail
		result = self.setting.loadSavedEmail() == self.savedEmail
		self.assertEqual(result ,True)


if __name__ == '__main__':
	unittest.main()