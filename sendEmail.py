import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['subject'] = 'You won 10,00,00 Rs'
email['to'] = 'RecieverEmail@gmail.com'
email['from'] = 'manjeet kumar'

email.set_content('Just login and get your reward !')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('youremail@gmail.com', 'yourPassword')
	smtp.send_message(email)
	print('that\'s work')