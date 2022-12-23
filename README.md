# IoT GreenHouse Monitor
 A homemade DIY project from monitoring a greenhouse for SETU Computer Systems and Networks Module assignment 2.
## What is it?
This project is designed to use a number of different IoT devices to basically moniter conditions in a greenhouse and then to send notifications to the user in the case of certian predetermined events. The project is ran from a raspberry pi 4 and was designed using python as the coding language. There is also a rudimentary website that displays data taken from the raspberry pi about the current temperature, pressure and humidity conditions in the greenhouse; as well as a picture of the inside of the greenhouse that is updated daily. (Although feel free to employ a more frequent schedule if you wish). Pictures are stored on FireBase.
<img width="80" alt="Screenshot 2022-12-23 at 04 22 25" src="https://user-images.githubusercontent.com/97414396/209270456-472f0be5-e150-4f1c-8b64-3c4eb7d06c08.png">
### The Website: (https://pineapple-rambunctious-sauroposeidon.glitch.me) 
## Pre-requisites?
In order to get started with this project you'll need:
The Hardware: 
* Raspberry Pi (I use a Pi 4 Model B) but I'm fairly sure a Pi 3 should be fine
* Raspberry Camera Module V2 (Again different pi cameras should be fine)
* PIR motion sensor (NB: Make sure it's one that can be easily connected to GPIO board)
* Fly Cables
* Raspberry Pi SenseHat
* Smart Light (I use a WiX smart bulb, but you can go for a Philips Hue if you're feeling fancy)
* Bluetooth Speaker
The Software:
* Raspbian OS (I use headless and connect over ssh but GUI is fine too)
* IFTTT (https://ifttt.com)
* ThingSpeak (https://thingspeak.com)
* FireBase (https://firebase.google.com)
* Blynk (https://blynk.io)
## The Parts
### Raspberry Pi
![rpi](https://user-images.githubusercontent.com/97414396/209255774-4d2619de-9d87-42f0-9e3b-edb9d873a96c.jpg)
### SenseHat
![SenseHat](https://user-images.githubusercontent.com/97414396/209256036-ff615347-7664-4f42-bf50-28f8cc872884.jpg) 
### PIR Sensor (Top)
![pir](https://user-images.githubusercontent.com/97414396/209256061-19833bfb-0efc-4d23-b2b3-a97be52bc3bc.jpg)
### PIR (Bottom)
![pirback](https://user-images.githubusercontent.com/97414396/209256071-578341c2-805a-4321-8540-01a9eb581ac4.jpg)
### Pi Camera Module
![picam](https://user-images.githubusercontent.com/97414396/209256075-0f9ae391-2389-4299-90c0-d200ce787975.jpg)
### Raspberry Pi Setup
![setup](https://user-images.githubusercontent.com/97414396/209256083-64edeb81-a5b6-4ea5-a255-406eb1ac94c3.jpg)
###  The Smart Bulb
![bulb](https://user-images.githubusercontent.com/97414396/209256842-71060244-c5e4-452d-b778-fe3a20e206f6.jpg)
### The Speaker
![speaker](https://user-images.githubusercontent.com/97414396/209256854-a002fa8c-be90-4336-a16a-8d8fc1ba5833.jpg)
## The Setup
 
This tutorial assumes you already have a Raspberry Pi setup. If not here is a useful video for setting up your raspberry Pi [Tom's Hardware] (https://www.tomshardware.com/how-to/set-up-raspberry-pi) 

#### Step 1: Attach the Camera module to the raspberry pi as shown. NB: Be sure to put the camera cable through the sensehat before connecting it to the pi as trying to attach the camera with the sensehat already on the pi is next to impossible.
![camPi](https://user-images.githubusercontent.com/97414396/209258802-26bdf978-0233-4342-9d2a-76ef3326954a.jpg)
 
### Step 2:
Connect the PIR Sensor to the PI as shown. Ideally you would use a pin extender to attach the PIR sensor on top of the SenseHat but since I don't have an extender I had to improvise.
 
* Connect the VCC pin on the PIR to Pin 2 on the Pi
* Connect the OUT pin on the PIR to Pin 6 on the Pi
* Connect the GROUND pin on the PIR to pin 12 on the Pi

![20221223_023228](https://user-images.githubusercontent.com/97414396/209259407-3ca5ef7b-b622-43c4-83d7-c37364958097.jpg)
### Step 3:

Attach the SenseHat to the Pi as shown

![20221223_024303-1](https://user-images.githubusercontent.com/97414396/209261011-ead6fd92-183a-4547-bdb9-3da01b12a0ae.jpg)
That's the Pi setup complete. 👍

## The External Hardware

### Connecting your bluetooth speaker.

#### The following step requires that you know the bluetooth name of your speaker or its MAC address

Connecting your speaker to your raspberry pi requires a few commands to be entered into the command line. Luckily though, when you have the speaker connected to the pi it should automatically reconnect whenever you need. 
To find your speaker enter the following commands :
* $bluetoothctl
* $power on
* $agent on
* $scan on

You should see a list begin to populate with different MAC addresses. Look for the one that corresponds to your bluetooth speaker and take note of its MAC address

<img width="700" alt="Screenshot 2022-12-23 at 03 05 22" src="https://user-images.githubusercontent.com/97414396/209262738-e2b5d3f7-4ae8-4ee1-87e1-7e2215157e91.png">
<img width="500" alt="Screenshot 2022-12-23 at 03 05 22" src="https://user-images.githubusercontent.com/97414396/209262738-e2b5d3f7-4ae8-4ee1-87e1-7e2215157e91.png">

To connect your speaker:
* $pair <SPEAKER_MAC_ADDRESS>
@@ -122,7 +122,7 @@ Your smart bulb is ready to go 👍

This project uses a number of IFTTT applets to fire events based on triggers

![Screenshot 2022-12-23 at 03 39 32](https://user-images.githubusercontent.com/97414396/209266464-34a8a2bb-69ea-45c2-b2b3-827619301448.jpg)
<img width="500" alt="Screenshot 2022-12-23 at 03 39 32" src="https://user-images.githubusercontent.com/97414396/209330419-6afa6798-0239-4334-9059-f1f0bc5e68be.png">

* The first applet turns the WiZ light blue if the humidity rises above 85% in your local area
* The second applet turns the WiZ light red if the temperature rises above 21°C
* The third applet sends a SMS if a WebHooks GET request is sent. (The GET request is sent based on a    condition in the python script)
* The fourth applet triggers the WiZ light to turn on from a WebHooks GET request
You can set your IFTTT applets to do basically whatever you want

## <img width="80" alt="Screenshot 2022-12-23 at 04 47 09" src="https://user-images.githubusercontent.com/97414396/209272767-26221ec8-f791-4764-a503-5e91a12d5fda.png">

This project uses the BLYNK.io app to allow you to take pictures of the greenhouse remotely from your phone. These photos are then emailed to you 
uploaded to the your firebase dateabase. This is just a bit of fun functionality. It doesn't do much other than just allow you do see what things are looking like in your greenhouse. Such as maybe checking if you left the door open and you don't want to go back outside to check.

To Download and setup blynk go to (https://blynk.io/en/getting-started)

NB: You'll also need to download the mobile version if you want to use blynk on your mobile
## <img width="60" alt="Screenshot 2022-12-23 at 04 48 11" src="https://user-images.githubusercontent.com/97414396/209272868-31bf8cc5-ac4b-457f-a303-65bcec640f28.png">

Images taken with the PiCamera are uploaded to FireBase and then from FireBase they go to the Glitch website

## Some things to note

### SSH Broken-Pipe

Since this project runs on the pi over ssh the programs are at risk of being terminated if the current ssh session is unexpectedly disconnected (Which seems to happen more often than you'd like)

Thankfully though. There is a good solution using Screen. Screen is a useful tool in linux that allows processes to continue running on your server even if the ssh connection is dropped.

To use Screen:
* Download Screen: $ sudo apt-get install screen
* To start a new Screen session: $ screen
* Run your program
* To check what Screens you have running: $ screen -ls
* To pass into a specific Screen session: $ screen -r <ID of your screen session >

### Scheduling Functions
Linux has the crontab utility to allow you to schedule certian programs to run at specific times. However I have found crontab to be a little unreliable. Therefore I have decided to use the 'Schedule' library to schedule some of the functions in my script:

* $ pip install schedule
 
<img width="500" alt="Screenshot 2022-12-23 at 04 15 30" src="https://user-images.githubusercontent.com/97414396/209269825-36ca1d0f-e240-4519-87fc-4de61be12a1d.png">
 
 ## Issues 😦
 
It's worth noting that the temperature, pressure, and humidity information on the website is being taken from measurements made on the SenseHat. The SenseHat has a notable issue when it comes to its temperature readings being significantly off from the actual value. This is due to the temperature sensor recieving heat from the pi's CPU and also the SenseHat just isn't that great of a temperature sensor. To compensate for this issue I have used to following formula:
 
 * temp = sense.get_temperature - (sense.get_temperature()/100)*33)
 
This gives a much more accurate reading but it is still by no means perfect. 

