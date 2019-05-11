#SUBMODULE:VOLUME

import STATUS
import LED

#PROPERTIES

PERCENTAGE_TOLERANCE = 0.1 #10%

#ACTIONS

def update():
    print("VOLUME - UPDATE")
    distanceFull = STATUS.loadDistanceFull()
    distanceEmpty = STATUS.loadDistanceEmpty()
    distance = STATUS.loadDistance()

    range = distanceEmpty - distanceFull

    percentage = 0.0
    if distance < distanceEmpty:
        diffFromEmpty = distanceEmpty - distance
	percentage = diffFromEmpty / range
    print("VOLUME - UPDATE - PERCENTAGE = [%.2f]" % percentage)

    volumeMax = STATUS.loadVolumeMax()
    volume = volumeMax * percentage
    print("VOLUME - UPDATE - VOLUME = [%d]" % volume)

    STATUS.saveVolume(volume)
    STATUS.savePercentage(percentage)

    if percentage < PERCENTAGE_TOLERANCE:
	LED.red()
    else:
	LED.blue()
