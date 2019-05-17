#HW:ULTRASOUND

import RPi.GPIO as IO
import time

#PROPERTIES

US_OUT = 18
US_IN = 24

#SETUP

def setup():
    print("ULTRASOUND - SETUP")
    IO.setmode(IO.BCM)
    IO.setwarnings(0)
    IO.setup(US_OUT, IO.OUT)
    IO.setup(US_IN, IO.IN)

#ACTIONS

def getDistance():
    print("ULTRASOUND - GET DISTANCE...")

    #For sure.
    time.sleep(0.02)

    #Sending sound for duration 0.00001 seconds.
    IO.output(US_OUT, 1)
    time.sleep(0.00005) #0.00001
    IO.output(US_OUT, 0)

    #Prepare properties for measuring time.
    timeStartFixed = time.time()
    timeStart = time.time()
    timeStop = time.time()

    #Listen for sound coming back.
    while IO.input(US_IN) == 0:
 	timeStart = time.time()
	diff = timeStart - timeStartFixed
	if diff > 1:
	    return 1000.0
    while IO.input(US_IN) == 1:
	timeStop = time.time()

    #Calculate distance.
    timeElapsed = timeStop - timeStart
    print("timeElapsed = %.10f" % timeElapsed)
    distance = (timeElapsed * 34300) / 2 # 34300
    #distance = timeElapsed / 29.1

    print("ULTRASOUND - GET DISTANCE... [%.3f CM]" % distance)
    return distance

#MAIN

setup()
getDistance()
