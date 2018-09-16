#!/usr/bin/env python

import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

print("Sending email now")
fromaddr = "imos1986@gmail.com"
toaddr = "imaredia@centrilogic.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test to check to my code"

body = "Attached is port desnity report"
msg.attach(MIMEText(body,'plain'))

filename = "free-core-ports.txt"
attachment = open("/home/irfan/Projects/free-core-ports.txt" , "rb")

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= %s" % filename)

msg.attach(part)
server =smtplib.SMTP('smtp.gmail.com','587')
server.ehlo()
server.starttls()
server.login('imos1986@gmail.com','9821331198')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

os.remove('free-core-ports.txt')
 
