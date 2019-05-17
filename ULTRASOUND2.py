#HW:ULTRASOUND2

import pigpio
import time

#PROPERTIES

TRIGGER=18
ECHO=24

high_tick = None # Global to hold high tick
measurement = 0.0

#ACTIONS

def cbfunc(gpio, level, tick):
	global high_tick
	global measurement

	if level == 0: # echo line changed from high to low.
		if high_tick is not None:
			echo = pigpio.tickDiff(high_tick, tick)
			cms = (echo / 1000000.0) * 34030 / 2
			#print("echo was {} micros long ({:.1f} cms)".format(echo, cms))
			print("callback called")
			measurement = cms
	else:
		high_tick = tick

def getDistance():
	pi = pigpio.pi() # Connect to local Pi.

	pi.set_mode(TRIGGER, pigpio.OUTPUT)
	pi.set_mode(ECHO, pigpio.INPUT)

	cb = pi.callback(ECHO, pigpio.EITHER_EDGE, cbfunc)

	pi.gpio_trigger(TRIGGER, 10)
	time.sleep(0.25)

	cb.cancel() # Cancel callback.
	pi.stop() # Close connection to Pi

	print("MEASUREMENT = %.2f" % measurement)
	return measurement
