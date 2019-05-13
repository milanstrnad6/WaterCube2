#BOOT MODULE:CUBE

import RPi.GPIO as IO
import time

import ULTRASOUND
import PUMP
import LED

import FILES
import MEASUREMENTS
import SCHEDULE

#PROPERTIES

FILENAME = '/home/pi/CUBE/DATA/cube.txt'
ROW_WAIT_FOR_INTERNET_CONNECTION = 3

BOOTING_EXTRATIME = 2 #seconds
WAIT_FOR_NEXT_CHECK = 2 #seconds

#ACTIONS

def boot():
    print("*[CUBE - BOOT]*")
    IO.setmode(IO.BCM)
    IO.setwarnings(0)
    ULTRASOUND.setup()
    PUMP.setup()
    LED.setup()

    duration = int(FILES.loadline(FILENAME,ROW_WAIT_FOR_INTERNET_CONNECTION)) + BOOTING_EXTRATIME
    LED.bootBlinking(duration)

    start()

#UTILITIES

def start():
    print("*[CUBE - START]*")
    while True:
	print("*[CUBE - CHECK]*")
       	#MEASUREMENTS.measure()
    	#SCHEDULE.pourIfNeeded()
    	time.sleep(WAIT_FOR_NEXT_CHECK)

#MAIN

boot()
