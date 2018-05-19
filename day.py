from time import sleep, strftime, time

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)



if not GPIO.input(27):
   GPIO.output(27,1)
   GPIO.output(19,0)
