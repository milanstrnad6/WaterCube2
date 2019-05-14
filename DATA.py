#MANAGER:DATA

import FILES

#PROPERTIES:CUBE

FILENAME_CUBE = '/home/pi/CUBE/DATA/cube.txt'
ROW_WAIT_FOR_INTERNET_CONNECTION = 3
ROW_WARNING_PERCENTAGE = 6
ROW_WARNING_DAYS_LEFT = 8
ROW_VOLUME_MAX = 11
ROW_DISTANCE_FULL = 13 
ROW_DISTANCE_EMPTY = 15

#PROPERTIES:NOW

FILENAME_NOW = '/home/pi/CUBE/DATA/now.txt'
ROW_POURING_IN_PROGRESS = 3 
ROW_DISTANCE = 6
ROW_PERCENTAGE = 8 
ROW_VOLUME = 11
ROW_DAYS_LEFT = 13 

#PROPERTIES:SCHEDULE

FILENAME_SCHEDULE = '/home/pi/CUBE/DATA/schedule.txt'
ROW_ENABLED = 3
ROW_NAME = 6
ROW_DATE = 9
ROW_DURATION = 11 
ROW_SKIP_DAYS = 13

#ACTIONS:CUBE

def load_waitForInternetConnection():
    return int(FILES.loadline(FILENAME_CUBE,ROW_WAIT_FOR_INTERNET_CONNECTION))

def load_warningPercentage():
    return float(FILES.loadline(FILENAME_CUBE,ROW_WARNING_PERCENTAGE))

def load_warningDaysLeft():
    return int(FILES.loadline(FILENAME_CUBE,ROW_WARNING_DAYS_LEFT))

def load_volumeMax():
    return int(FILES.loadline(FILENAME_CUBE,ROW_VOLUME_MAX))

def load_distanceFull():
    return float(FILES.loadline(FILENAME_CUBE,ROW_DISTANCE_FULL))

def load_distanceEmpty():
    return float(FILES.loadline(FILENAME_CUBE,ROW_DISTANCE_EMPTY))

#ACTIONS:NOW

def load_pouringInProgress():
    return int(FILES.loadline(FILENAME_NOW,ROW_POURING_IN_PROGRESS))

def load_distance():
    return float(FILES.loadline(FILENAME_NOW,ROW_DISTANCE))

def load_percentage():
    return float(FILES.loadline(FILENAME_NOW,ROW_PERCENTAGE))

def load_volume():
    return int(FILES.loadline(FILENAME_NOW,ROW_VOLUME))

def load_daysLeft():
    return int(FILES.loadline(FILENAME_NOW,ROW_DAYS_LEFT))

def save_pouringInProgress(pouringInProgress):
    FILES.saveline(FILENAME_NOW,ROW_POURING_IN_PROGRESS,str(pouringInProgress))

def save_distance(distance):
    FILES.saveline(FILENAME_NOW,ROW_DISTANCE,str(distance))

def save_percentage(percentage):
    FILES.saveline(FILENAME_NOW,ROW_PERCENTAGE,str(percentage))

def save_volume(volume):
    FILES.saveline(FILENAME_NOW,ROW_VOLUME,str(int(volume)))

def save_daysLeft(daysLeft):
    FILES.saveline(FILENAME_NOW,ROW_DAYS_LEFT,str(daysLeft))

#ACTIONS:SCHEDULE

def load_enabled():
    return int(FILES.loadline(FILENAME_SCHEDULE,ROW_ENABLED))

def load_name():
    return FILES.loadline(FILENAME_SCHEDULE,ROW_NAME)

def load_date():
    return FILES.loadline(FILENAME_SCHEDULE,ROW_DATE).rstrip()

def load_duration():
    return float(FILES.loadline(FILENAME_SCHEDULE,ROW_DURATION))

def load_skipDays():
    return int(FILES.loadline(FILENAME_SCHEDULE,ROW_SKIP_DAYS))

def save_enabled(enabled):
    FILES.saveline(FILENAME_SCHEDULE,ROW_ENABLED,str(enabled))

def save_name(name):
    FILES.saveline(FILENAME_SCHEDULE,ROW_NAME,name)

def save_date(date):
    FILES.saveline(FILENAME_SCHEDULE,ROW_DATE,date)

def save_duration(duration):
    FILES.saveline(FILENAME_SCHEDULE,ROW_DURATION,str(duration))

def save_skipDays(skipDays):
    FILES.saveline(FILENAME_SCHEDULE,ROW_SKIP_DAYS,str(skipDays))
