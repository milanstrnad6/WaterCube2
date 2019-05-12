#HW:LED

import RPi.GPIO as IO
import time

#PROPERTIES

LED_BLUE = 20
LED_RED = 16

#SETUP

def setup():
    print("LED - SETUP")
    IO.setmode(IO.BCM)
    IO.setup(LED_BLUE, IO.OUT)
    IO.setup(LED_RED, IO.OUT)

#BOOT

def bootBlinking(duration):
    print("LED - BOOT BLINKING...")
    off()
    for x in range (0,duration):
	time.sleep(0.5)
	red()
	time.sleep(0.5)
	off()

#ACTIONS

def blue():
    print("LED - BLUE")
    off()
    IO.output(LED_BLUE, 1)

def red():
    print("LED - RED")
    off()
    IO.output(LED_RED, 1)

def off():
    print("LED - OFF")
    IO.output(LED_BLUE, 0)
    IO.output(LED_RED, 0)
