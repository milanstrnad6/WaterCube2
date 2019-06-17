#MANAGER:DATA

import FILES

#PROPERTIES:CUBE

FILENAME_CUBE = '/home/pi/CUBE3/WaterCube2/DATA/cube.txt'
ROW_WAIT_FOR_INTERNET_CONNECTION = 3
ROW_WARNING_PERCENTAGE = 6
ROW_WARNING_DAYS_LEFT = 8
ROW_VOLUME_MAX = 11
ROW_DISTANCE_FULL = 13 
ROW_DISTANCE_EMPTY = 15

#PROPERTIES:NOW

FILENAME_NOW = '/home/pi/CUBE3/WaterCube2/DATA/now.txt'
ROW_POURING_IN_PROGRESS = 3 
ROW_DISTANCE = 6
ROW_PERCENTAGE = 8 
ROW_VOLUME = 11
ROW_DAYS_LEFT = 13 

#PROPERTIES:SCHEDULE

FILENAME_SCHEDULE = '/home/pi/CUBE3/WaterCube2/DATA/schedule.txt'
ROW_ENABLED = 3
ROW_NAME = 6
ROW_DATE = 9
ROW_ML = 11 
ROW_SKIP_DAYS = 13

#PROPERTIES:NOTIFICATIONS

FILENAME_NOTIFICATION = '/home/pi/CUBE3/WaterCube2/DATA/notification.txt'
ROW_TOKEN = 3
ROW_SHOULD_SEND = 6

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
    return FILES.loadline(FILENAME_SCHEDULE,ROW_NAME).rstrip()

def load_date():
    return FILES.loadline(FILENAME_SCHEDULE,ROW_DATE).rstrip()

def load_ml():
    return int(FILES.loadline(FILENAME_SCHEDULE,ROW_ML))

def load_skipDays():
    return int(FILES.loadline(FILENAME_SCHEDULE,ROW_SKIP_DAYS))

def save_enabled(enabled):
    FILES.saveline(FILENAME_SCHEDULE,ROW_ENABLED,str(enabled))

def save_name(name):
    FILES.saveline(FILENAME_SCHEDULE,ROW_NAME,name.rstrip())

def save_date(date):
    FILES.saveline(FILENAME_SCHEDULE,ROW_DATE,date)

def save_ml(ml):
    FILES.saveline(FILENAME_SCHEDULE,ROW_ML,str(ml))

def save_skipDays(skipDays):
    FILES.saveline(FILENAME_SCHEDULE,ROW_SKIP_DAYS,str(skipDays))

#ACTIONS:NOTIFICATIONS

def load_token():
    return FILES.loadline(FILENAME_NOTIFICATION,ROW_TOKEN).rstrip()

def load_shouldSend():
    return int(FILES.loadline(FILENAME_NOTIFICATION,ROW_SHOULD_SEND).rstrip())

def save_token(token):
    print("DATA SAVE TOKEN")
    print(token)
    FILES.saveline(FILENAME_NOTIFICATION,ROW_TOKEN,token)

def save_shouldSend(shouldSend):
    FILES.saveline(FILENAME_NOTIFICATION,ROW_SHOULD_SEND,str(shouldSend))
