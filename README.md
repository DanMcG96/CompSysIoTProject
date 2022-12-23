# IoT GreenHouse Monitor
 A homemade DIY project from monitoring a greenhouse for SETU Computer Systems and Networks Module assignment 2.

## What is it?
This project is designed to use a number of different IoT devices to basically moniter conditions in a greenhouse and then to send notifications to the user in the case of certian predetermined events. The project is ran from a raspberry pi 4 and was designed using python as the coding language. There is also a rudimentary website that displays data taken from the raspberry pi about the current temperature, pressure and humidity conditions in the greenhouse; as well as a picture of the inside of the greenhouse that is updated daily. (Although feel free to employ a more frequent schedule if you wish). Pictures are stored on FireBase.

## Pre-requisites?
In order to get started with this project you'll need:

The Hardware: 

* Raspberry Pi (I use a Pi 4 Model B) but I'm fairly sure a Pi 3 should be fine
* Raspberry Camera Module V2 (Again different pi cameras should be fine)
* PIR motion sensor (NB: Make sure it's one that can be easily connected to GPIO board)
* Raspberry Pi SenseHat
* Smart Light (I use a WiX smart bulb, but you can go for a Philips Hue if you're feeling fancy)
* Bluetooth Speaker

The Software:

* Raspbian OS (I use headless and connect over ssh but GUI is fine too)
* IFTTT [IFTTT] (https://ifttt.com)
* ThingSpeak
* FireBase
* Blynk

