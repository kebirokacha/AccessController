import unittest
from custom_widgets.setting.sendEmailClass import Emailsender


class MyTestCase(unittest.TestCase):
	def setUp(self):
		self.emailSender = Emailsender(receiver='bahrib665@gmail.com')

	def test_EmailSenderSentMail(self):
		self.assertEqual(self.emailSender.sendEmail(), True)	


if __name__ == '__main__':
	unittest.main()
