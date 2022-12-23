import os
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
from datetime import datetime

camera = PiCamera() 
motionPin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motionPin, GPIO.IN)
check = 0
datetime = datetime.now()
timestamp = datetime.now().strftime("%H:%M:%S")
sleep(60)


try:
    while True:
     motion=GPIO.input(motionPin)
     print(motion)
     if motion == 1:
       
       if check < 1:
         camera.start_preview()
         print("motion was detected!")
         camera.capture(f'{timestamp}.jpg')
         os.system("curl -X GET 'https://maker.ifttt.com/trigger/{wizLight}/json/with/key/cydsvSYps_WZqDPgERFMHZ' ")
         os.system("curl -X GET 'https://maker.ifttt.com/trigger/{sendSMS}/json/with/key/cydsvSYps_WZqDPgERFMHZ' ")       
         os.system(f"mpack -s 'Motion in the GreenHouse' -a '{timestamp}.jpg' rpiprojectemail96@gmail.com")        
         os.system(f'mv {timestamp}.jpg images')
         check = check + 1
         camera.stop_preview()

     sleep(0.1)   
except KeyboardInterrupt:
     GPIO.cleanup()
     print("All Set")


 
