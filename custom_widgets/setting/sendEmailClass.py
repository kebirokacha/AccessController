import smtplib
from email.message import EmailMessage

class Emailsender ():
    def __init__(self) -> None:
        
        self.msg = EmailMessage()
        self.msg['Subject'] = 'Alert Email '
        self.msg['From'] = 'okachakebir@gmail.com'
        self.msg['To'] = 'bahrib665@gmail.com'
        self.msg.set_content('rani nsiyi matt9ala9ch w say : be carful there is a unknown person close from  your house  .')

		# Set up the SMTP server and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('okachakebir@gmail.com', 'couhkbrsfupmckyp')
            smtp.send_message(self.msg)