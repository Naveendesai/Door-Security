import RPi.GPIO as gpio
import picamera
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
fromaddr="raspberrypimailadress@mail.com"  #use the raspberrypi mail address
toaddr="usermailadress@mail.com"  #use the user mail adress
mail=MIMEMultipart()
mail['From']=fromaddr
mail['To']=toaddr
mail['Subject']="Attachment"
body="Please find the atteachement"
led=17
pir=18
High=1
Low=0
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led,gpio.OUT)
gpio.setup(pir,gpio.IN)
data=""
def sendMail(data):
  mail.attach(MIMEText(body,'plain'))
  print data
  dat='%s.jpg'%data
  print dat
  attachment=open(dat,'rb')
  image=MIMEImage(attachment.read())
  attachment.close()
  mail.attach(image)
  server=smtplib.SMTP('smtp.google.com',587)
  server.starttls()
  server.login(fromaddr,"USER PASSWORD")
  text=mail.as_string()
  server.sendmail(fromaddr,toaddr,text)
  server.quit()
def capture_image():
  data=time.strftime("%d_%b_%y|%H:%M:%S")
  camera.start_preview()
  time.sleep(5)
  print data
  camera.capture('%s.jpg'%data)
  camera.stop_preview()
  time.sleep(1)
  sendMail(data)
gpio.output(led,0)
camera.picamera.Picamera()
camera.rotation=180
camera.awb_mode='auto'
camera.brightness=55
while=1:
  if gpio.input(pir)==1:
    gpio.output(led,High)
    capture_image()
    while(gpio.input(pir)==1):
      time.sleep(1)
  else
    gpio.output(led,Low)
    time.sleep(0.01)
