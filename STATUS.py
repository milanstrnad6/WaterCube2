#MANAGER:STATUS

import FILES

#PROPERTIES

FILENAME = '/home/pi/CUBE/DATA/status.txt'
ROW_POURING_POSSIBLE = 1
ROW_DISTANCE_FULL = 3
ROW_DISTANCE_EMPTY = 5
ROW_DISTANCE = 7
ROW_VOLUME_MAX = 9
ROW_VOLUME = 11
ROW_PERCENTAGE = 13
ROW_WARNING_PERCENTAGE = 15
ROW_DAYS_LEFT = 17
ROW_POUR_HAPPENED = 19
ROW_LAST_POUR = 21

#ACTIONS

def loadPouringPossible():
    print("STATUS - LOAD POURING POSSIBLE")
    return int(FILES.loadline(FILENAME,ROW_POURING_POSSIBLE))

def savePouringPossible(pouringPossible):
    print("STATUS - SAVE POURING POSSIBLE [%d]" % pouringPossible)
    FILES.saveline(FILENAME,ROW_POURING,str(pouringPossible))

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

def loadWarningPercentage():
    print("STATUS - LOAD WARNING PERCENTAGE")
    return float(FILES.loadline(FILENAME,ROW_WARNING_PERCENTAGE))

def loadDaysLeft():
    print("STATUS - LOAD DAYS LEFT")
    return int(FILES.loadline(FILENAME,ROW_DAYS_LEFT))

def saveDaysLeft(daysLeft):
    print("STATUS - SAVE DAYS LEFT [%d]" % daysLeft)
    FILES.saveline(FILENAME,ROW_DAYSLEFT,str(daysLeft))

def loadPourHappened():
    print("STATUS - LOAD POUR HAPPENED")
    return int(FILES.loadline(FILENAME,ROW_POUR_HAPPENED))

def savePourHappened(pourHappened):
    print("STATUS - SAVE POUR HAPPENED")
    FILES.saveline(FILENAME,ROW_POUR_HAPPENED,str(pourHappened))

def loadLastPour():
    print("STATUS - LOAD LAST POUR")
    return FILES.loadline(FILENAME,ROW_LAST_POUR)

def saveLastPour(lastPour):
    print("STATUS - SAVE LAST POUR")
    FILES.saveline(FILENAME,ROW_LAST_POUR,lastPour)
