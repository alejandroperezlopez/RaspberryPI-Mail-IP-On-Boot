import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
from urllib2 import urlopen
import datetime

#ACCOUNT WHERE THE MAIL WILL BE SENT
to = 'XXXXX@XXXX.XXX'
#CREDENTIALS FOR THE ACCOUNT USED TO SEND THE MAIL
gmail_user = 'XXXXXXX@XXXX.XXX'
gmail_password = 'XXXXX'
#GMAIL SMTP CONFIGURATION
smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()

#Works on linux. Modify it for other os
#Get the local ip
publicIPCmd='ip route list'
p=subprocess.Popen(publicIPCmd,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
localIP = split_data[split_data.index('src')+1]
#Get public ip from the ipecho service
publicIP = urlopen('http://ipecho.net/plain')
#Prepare mail content and from/to config
my_ip = 'Your local IP is %s and your public IP is %s' %  (localIP,publicIP.read())
msg = MIMEText(my_ip)
msg['Subject'] = '[%s] IP For RaspberryPi on %s' % (socket.gethostname(),today.strftime('%b %d %Y'))
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
