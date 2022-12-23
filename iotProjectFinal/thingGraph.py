import os
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
waitTime = 0
check = 1

while True:
  temp = round(sense.get_temperature() - ((sense.get_temperature()/100)*33))
  pressure = sense.get_pressure()
  humidity = sense.get_humidity()
  os.system(f"curl -X GET 'https://api.thingspeak.com/update?api_key=0CNLQVDWS1RDL7E3&field1={temp}&field2={pressure}&field3={humidity}' ")
  print('Graph Updated')
  os.system(f'echo {temp} >> tempLog.txt')
  if check > waitTime: 
   if os.system("grep '20' tempLog.txt"): 
      os.system("mpack -s 'Green House' -a 'openADoor.mp3' rpiprojectemail96@gmail.com < emailMessage.txt")
      os.system("echo '.' > tempLog.txt")
   waitTime = waitTime + 300
  print(temp)
  check = check + 15
  sleep(300)
  
