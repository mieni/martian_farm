from time import sleep, strftime, time

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)#soil mousture
GPIO.setup(27, GPIO.OUT)#water_pump


GPIO.output(27,0)


def read_moist(moist):
    moist =  GPIO.input(11)
    return moist


def water():
#for 5 sec the amount of water is ~ 25 mm
    GPIO.output(27,1)
    sleep(5)
    GPIO.output(27,0)

#every two days
time_watering = time.time() + 60*60*24*2

while True:
    moist = 1
    moist = read_moist(moist)
    sleep(60*60)
    if moist == 0 or time.time() > timeout :
        water()
        time_watering = time.time() + 60*60*24*4
