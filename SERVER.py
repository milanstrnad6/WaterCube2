#BOOT MODULE:SERVER

import FILES
import subprocess as SUB
import time

#PROPERTIES

FILENAME = '/home/pi/CUBE/DATA/booting.txt'
ROW_BOOTING = 1

#ACTIONS

def boot():
    duration = int(FILES.loadline(FILENAME,ROW_BOOTING))
    time.sleep(duration)
    SUB.call(['/home/pi/CUBE/serverStart.sh'])

#MAIN

boot()
