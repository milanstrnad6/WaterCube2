#HW:PUMP

import RPi.GPIO as IO
import time

#PROPERTIES

PUMP = 12

#HELPERS

ON = 0
OFF = 1

#SETUP

def setup():
    print("PUMP - SETUP")
    IO.setmode(IO.BCM)
    IO.setwarnings(0)
    IO.setup(PUMP, IO.OUT)
    IO.output(PUMP, OFF)

#ACTIONS

def start(duration):
    print("PUMP - START [DURATION = %.1f]" % duration)
    setup()
    IO.output(PUMP, ON)
    time.sleep(duration)
    IO.output(PUMP, OFF)
    