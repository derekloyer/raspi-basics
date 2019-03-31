
#Raspi code to turn an LED on/off with the press off a button
#LED connected to GPIO pin set to output
#Button connected to GPIO pin set to input

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)    #sets GPIO pinout to physical board
GPIO.setwarnings(False)     #turns warnings off

ledPin = 11                 #Variable to set ledPin to physical pin number
buttonPin = 13              #Variable to set ButtonPin to physical pin number

GPIO.setup(ledPin,GPIO.OUT) #ledPin (pin 11) set to output
GPIO.setup(buttonPin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   #buttonPin set as input and pulled to logic low

def toggleLEDcallback(channel):     #function to toggle LED state at button press
        if (GPIO.input(ledPin) == True):
                GPIO.output(ledPin, False)
        else:
                GPIO.output(ledPin, True)

GPIO.add_event_detect(buttonPin,GPIO.RISING,callback=toggleLEDcallback, bouncetime=100) #detects button press, debounced 100ms

while 1:
        x=1

GPIO.cleanup() #cleanup GPIO pins on exit
