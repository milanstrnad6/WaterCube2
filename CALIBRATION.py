#CALIBRATION

import MEASUREMENTS

#PROPERTIES

NUMBER_OF_CALIBRATION_MEASUREMENTS = 10

#MAIN

measurements = []

for x in range (0,NUMBER_OF_CALIBRATION_MEASUREMENTS):
    measurements.append(MEASUREMENTS.measure())

totalsum = sum(measurements)
count = len(measurements)

average = totalsum / float(count)
print("CALIBRATION - DISTANCE = [%.3f]" % average)
