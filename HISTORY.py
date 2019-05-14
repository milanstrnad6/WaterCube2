#MANAGER:HISTORY

import FILES
import TIMES

#PROPERTIES

FILENAME = '/home/pi/CUBE/DATA/history.txt'

#ACTIONS: LOAD

def load_allEvents():
    print("HISTORY - LOAD: ALL EVENTS")
    return FILES.load(FILENAME)

#ACTIONS: SAVE

def save_deviceInit():
    print("HISTORY - SAVE EVENT: DEVICE INIT")
    saveEvent("deviceInit")
    return TIMES.nowAsString()

def save_manualPour(ml):
    print("HISTORY - SAVE EVENT: MANUAL POUR")
    saveEvent("manualPour",ml)

def save_automaticPour(ml):
    print("HISTORY - SAVE EVENT: AUTOMATIC POUR")
    saveEvent("automaticPour",ml)

def save_automaticPourNotPossible(ml):
    print("HISTORY - SAVE EVENT: AUTOMATIC POUR NOT POSSIBLE")
    saveEvent("automaticPourNotPossible",ml)

def save_warningPercentage():
    print("HISTORY - SAVE EVENT: WARNING PERCENTAGE")
    saveEvent("warningPercentage")

#UTILITIES

def saveEvent(type,ml=0):
    data = FILES.load(FILENAME)
    record = type + "|" + TIMES.nowAsString() + "|" + str(ml) + "\n"
    data.append(record)
    FILES.save(FILENAME,data)

def reset():
    data = 'HISTORY\n'
    FILES.save(FILENAME,data)
