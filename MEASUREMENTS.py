#MODULE:MEASUREMENTS

import statistics

import ULTRASOUND
import STATUS
import VOLUME

#PROPERTIES

NUMBER_OF_MEASUREMENTS = 10
DIFF_TOLERANCE = 0.5 #CM

#ACTIONS

def measure():
    print("MEASUREMENTS - MEASURE")
    ULTRASOUND.setup()

    measurements = []
    for x in range (0,NUMBER_OF_MEASUREMENTS):
        measurements.append(ULTRASOUND.getDistance())
    print("MEASUREMENTS - MEASURE - VALUES:")
    print(measurements)

    totalsum = sum(measurements)
    count = len(measurements)
    average = totalsum / float(count)
    print("MEASUREMENTS - MEASURE - AVERAGE = [%.3f]" % average)

    minimum = min(measurements)
    maximum = max(measurements)
    minOffset = average - minimum
    print("MEASUREMENTS - MEASURE - MIN OFFSET = [%.3f]" % minOffset)
    maxOffset = maximum - average
    print("MEASUREMENTS - MEASURE - MAX OFFSET = [%.3f]" % maxOffset)

    if minOffset > DIFF_TOLERANCE:
	measure()
    elif maxOffset > DIFF_TOLERANCE:
	measure()
    else:
	median = statistics.median(measurements)
	print("MEASUREMENTS - MEASURE - MEDIAN = [%.3f]" % median)
	STATUS.saveDistance(median)

    VOLUME.update()
