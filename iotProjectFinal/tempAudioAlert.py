from sense_hat import SenseHat
from time import sleep
import schedule
import os

sense = SenseHat()


def checkTemp():
  sense.clear()
  temperature = sense.get_temperature()
  temp_corrections = round(temperature - ((temperature/100)*33), 2)
  if temperature > 21:
    os.system('mpg123 openADoor.mp3')

def checkHumidity():
  sense.clear()
  humidity = sense.get_humidity()
  if humidity > 88:
    os.system('mpg123 humid.mp3') 

schedule.every(10).minutes.do(checkTemp)
schedule.every(11).minutes.do(humidityCheck)



while True:
    schedule.run_pending()
    time.sleep(1)
