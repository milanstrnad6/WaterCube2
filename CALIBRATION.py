#CALIBRATION

import MEASUREMENTS

#PROPERTIES

NUMBER_OF_MEASUREMENTS = 10
NUMBER_OF_CALIBRATION_MEASUREMENTS = 10

#UTILITIES

def getMeasurements():
	ULTRASOUND.setup()
	measurements = []
	for x in range (0,NUMBER_OF_MEASUREMENTS):
		measurements.append(ULTRASOUND.getDistance())
	return measurements

#MAIN

acceptableMeasurements = []

for x in range (0,NUMBER_OF_CALIBRATION_MEASUREMENTS):
	acceptable = False

	while not acceptable:
		measurements = getMeasurements()
		print("CALIBRATION - GET MEASUREMENTS - VALUES:")
		print(measurements)

		totalsum = sum(measurements)
		count = len(measurements)
		average = totalsum / float(count)
		print("CALIBRATION - GET MEASUREMENTS - AVERAGE = [%.3f]" % average)

		minimum = min(measurements)
		maximum = max(measurements)
		minOffset = average - minimum
		print("CALIBRATION - GET MEASUREMENTS - MIN OFFSET = [%.3f]" % minOffset)
		maxOffset = maximum - average
		print("CALIBRATION - GET MEASUREMENTS - MAX OFFSET = [%.3f]" % maxOffset)

		acceptable = minOffset <= DIFF_TOLERANCE and maxOffset <= DIFF_TOLERANCE
		if acceptable:
			acceptableMeasurements.append(average)

print("CALIBRATION - ACCEPTABLE MEASUREMENTS:")
print(acceptableMeasurements)

totalsum = sum(acceptableMeasurements)
count = len(acceptableMeasurements)

average = totalsum / float(count)
print("CALIBRATION - ACCEPTABLE MEASUREMENTS - AVERAGE = [%.3f]" % average)










