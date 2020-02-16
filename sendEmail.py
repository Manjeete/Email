import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()

email['subject'] = 'You won 10,00,00 Rs'
email['to'] = 'RecieverEmail@gmail.com'
email['from'] = 'manjeet kumar'

email.set_content(html.substitute({'name' : 'Raju'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('youremail@gmail.com', 'yourPassword')
	smtp.send_message(email)
	print('that\'s work')