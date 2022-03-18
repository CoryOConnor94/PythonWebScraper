import requests
import json
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
now = datetime.datetime.now()
from bs4 import BeautifulSoup

def main():

	content = getContent()
	sendEmail(content)
	

def getContent():

	url = 'https://www.empireonline.com/movies/features/best-movies-2/'
	result = requests.get(url)
	cnt = ''
	cnt +=('Top 100 Movies'+'\n'+'\n')
	doc = BeautifulSoup(result.text, "html.parser")
	for i, tag in enumerate(doc.find_all(re.compile("em"))):
		description = tag.parent
		
		cnt += ((str(i+1)+' - '+tag.text + '\n' + description.text +"\n"+"\n") if tag.text!='Empire' and tag.text!= 'feel' else '')
		
	return cnt


def sendEmail(content):

	SERVER = 'smtp.gmail.com'
	PORT = 587
	FROM = '<ENTER EMAILL ADDRESS>'
	TO = '<ENTER EMAILL ADDRESS>'
	PASS = '<ENTER EMAIL PASSWIORD>'

	msg = MIMEMultipart()

	msg['Subject'] = 'Top 100 Movies [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
	msg['From'] = FROM
	msg['To'] = TO
			
	msg.attach(MIMEText(content))

	print('Initiating Server...')

	server = smtplib.SMTP(SERVER, PORT)
	server.set_debuglevel(1)
	server.ehlo()
	server.starttls()
	server.login(FROM,PASS)
	server.sendmail(FROM, TO, msg.as_string())

	print('Email Sent')

	server.quit()		

		
if __name__=="__main__":
	main()	

