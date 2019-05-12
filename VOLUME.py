#MODULE:VOLUME

import STATUS
import LED

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

    warningPercentage = STATUS.loadWarningPercentage()
    if percentage < warningPercentage:
	LED.red()
    else:
	LED.blue()
