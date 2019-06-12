#BOOT MODULE:CUBE

import RPi.GPIO as IO
import time

import DATA

import MEASUREMENTS
import SCHEDULE

import ULTRASOUND
import PUMP
import LED

#PROPERTIES

BOOTING_EXTRATIME = 5 #seconds
WAIT_FOR_NEXT_CHECK = 2 #seconds

#ACTIONS

def boot():
    print("*[CUBE - BOOT]*")
    IO.setmode(IO.BCM)
    IO.setwarnings(0)
    ULTRASOUND.setup()
    PUMP.setup()
    LED.setup()

    duration = DATA.load_waitForInternetConnection() + BOOTING_EXTRATIME
    LED.bootBlinking(duration)

    start()

#UTILITIES

def start():
    print("*[CUBE - START]*")
    while True:
	print("*[CUBE - CHECK]*")
       	MEASUREMENTS.measure()
    	SCHEDULE.pourIfNeeded()
    	time.sleep(WAIT_FOR_NEXT_CHECK)

#MAIN

boot()
