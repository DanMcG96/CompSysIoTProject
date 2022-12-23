import BlynkLib
from picamera import PiCamera
from datetime import datetime
import storeFileDB
from time import sleep

camera = PiCamera()
camera.start_preview()

#Blynk Setup
BLYNK_AUTH = 'NVMf563ni5EENH8N_RW-PMhg-7O7wTi1'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

#handler for shutter
@blynk.on("V0")
def camera_handler(state):
  cameraState=state[0]
  print(f'{cameraState}')
  if cameraState=='1':
   frame = datetime.now().strftime("%H:%M:%S")
   fileLoc = f'/home/pi/fireCam/images/{frame}.jpg'
   timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
   camera.capture(fileLoc)
   storeFileDB.store_file(fileLoc)
   storeFileDB.push_db(fileLoc, timestamp)


while True:
  blynk.run()
  sleep(0.5)
