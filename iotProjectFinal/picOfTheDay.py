from picamera import PiCamera
from datetime import datetime
import os
import storeFileDB
import schedule
from time import sleep

#Setup PiCamera and Establsh Date
camera = PiCamera()


#Take a picture at 12:00am every day. Script is scheduled to run via crontab
def greenHousePic():
  camera.start_preview()
  camera.capture('picOfTheDay.jpg')
  camera.stop_preview()
  os.system("mv 'picOfTheDay.jpg' images")

#Upload the picture to FireBase and the Glitch website

  frame = f'picOfTheDay.jpg'
  fileLoc = f'/home/pi/iotProjectFinal/images/picOfTheDay.jpg'
  timestamp = timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  storeFileDB.store_file(fileLoc)
  storeFileDB.push_db(fileLoc, timestamp)

schedule.every().day.at("12:30").do(greenHousePic)

 
while True:
  schedule.run_pending()
  sleep(1)
