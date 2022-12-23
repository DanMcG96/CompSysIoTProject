import RPi.GPIO as GPIO
import time 
import os 

motionPin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motionPin, GPIO.IN)
dTime = time.ctime(time.time())
time.sleep(60)
dayCounter = 0

while True:
  motion = GPIO.input(motionPin)
  if motion == 1:
    os.system(f"echo 'motion was detected at {dTime}' >> motionCheck.txt")
  if dayCounter > 1728000:
   if not (os.system("grep 'motion' motionCheck.txt")):
     os.system("curl -X GET 'https://maker.ifttt.com/trigger/{sendSMS}/json/with/key/cydsvSYps_WZqDPgERFMHZ' ")
     os.system("echo '.' > motionCheck.txt")
     dayCounter = 0
   else:
     print("Motion was found")
  dayCounter = dayCounter + 1
  print(motion)
  time.sleep(0.1)
  

