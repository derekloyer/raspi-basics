#Raspi code to turn Blink LED
#LED connected to GPIO pin set to output


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)    #sets GPIO pinout to physical board
GPIO.setwarnings(False)     #turns warnings off
GPIO.setup(11,GPIO.OUT)     #sets physical pin 11 to output

speed = 1                   #sets blink to once per second

while True:
        print "LED on"      #prints led status to terminal
        GPIO.output(11,1)   #turns pin 11 high (led on)
        time.sleep(speed)   #1-second delay
        print "LED off"     #prints led status to terminal
        GPIO.output(11,0)   #turns pin 11 low (led off)
        time.sleep(speed)   #1-second delay
