#MODULE:MEASUREMENTS

import DATA
import VOLUME

import ULTRASOUND
import ULTRASOUND2

#PROPERTIES

NUMBER_OF_MEASUREMENTS = 10
DIFF_TOLERANCE = 0.3 #CM

#ACTIONS

def measure():
    print("MEASUREMENTS - MEASURE")
    #ULTRASOUND.setup()
    measurements = []

    for x in range (0,NUMBER_OF_MEASUREMENTS):
        #distance = ULTRASOUND.getDistance()
        distance = ULTRASOUND2.getDistance()
        measurements.append(distance)
    
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
        DATA.save_distance(average)
        VOLUME.update()    
