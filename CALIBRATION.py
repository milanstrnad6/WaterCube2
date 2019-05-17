#CALIBRATION

import MEASUREMENTS

#PROPERTIES

NUMBER_OF_CALIBRATION_MEASUREMENTS = 10

#MAIN

cMeasurements = []

for x in range (0,NUMBER_OF_CALIBRATION_MEASUREMENTS):
    cMeasurements.append(MEASUREMENTS.measure())

totalsum = sum(cMeasurements)
count = len(cMeasurements)

average = totalsum / float(count)
print("CALIBRATION - DISTANCE = [%.3f]" % average)
