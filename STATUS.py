#MANAGER:STATUS

import FILES

#PROPERTIES

FILENAME = '/home/pi/CUBE/DATA/status.txt'
ROW_POURING = 1
ROW_DISTANCE_FULL = 3
ROW_DISTANCE_EMPTY = 5
ROW_DISTANCE = 7
ROW_VOLUME_MAX = 9
ROW_VOLUME = 11
ROW_PERCENTAGE = 13
ROW_DAYS_LEFT = 15

#ACTIONS

def loadPouring():
    print("STATUS - LOAD POURING")
    return FILES.loadline(FILENAME,ROW_POURING)

def savePouring(pouring):
    print("STATUS - SAVE POURING [%d]" % pouring)
    FILES.saveline(FILENAME,ROW_POURING,pouring)

def loadDistanceFull():
    print("STATUS - LOAD DISTANCE FULL")
    return float(FILES.loadline(FILENAME,ROW_DISTANCE_FULL))

def loadDistanceEmpty():
    print("STATUS - LOAD DISTANCE EMPTY")
    return float(FILES.loadline(FILENAME,ROW_DISTANCE_EMPTY))

def loadDistance():
    print("STATUS - LOAD DISTANCE")
    return float(FILES.loadline(FILENAME,ROW_DISTANCE))

def saveDistance(distance):
    print("STATUS - SAVE DISTANCE [%.3f]" % distance)
    FILES.saveline(FILENAME,ROW_DISTANCE,str(distance))

def loadVolumeMax():
    print("STATUS - LOAD VOLUME MAX")
    return int(FILES.loadline(FILENAME,ROW_VOLUME_MAX))

def loadVolume():
    print("STATUS - LOAD VOLUME")
    return int(FILES.loadline(FILENAME,ROW_VOLUME))

def saveVolume(volume):
    print("STATUS - SAVE VOLUME [%d]" % volume)
    FILES.saveline(FILENAME,ROW_VOLUME,str(int(volume)))

def loadPercentage():
    print("STATUS - LOAD PERCENTAGE")
    return float(FILES.loadline(FILENAME,ROW_PERCENTAGE))

def savePercentage(percentage):
    print("STATUS - SAVE PERCENTAGE [%.2f]" % percentage)
    FILES.saveline(FILENAME,ROW_PERCENTAGE,str(percentage))

def loadDaysLeft():
    print("STATUS - LOAD DAYS LEFT")
    return FILES.loadline(FILENAME,ROW_DAYS_LEFT)

def saveDaysLeft(daysLeft):
    print("STATUS - SAVE DAYS LEFT [%d]" % daysLeft)
    FILES.saveline(FILENAME,ROW_DAYSLEFT,daysLeft)
