#BOOT MODULE:SERVER

import FILES
import subprocess as SUB
import time

#PROPERTIES

FILENAME = '/home/pi/CUBE/DATA/cube.txt'
ROW_WAIT_FOR_INTERNET_CONNECTION = 3

#ACTIONS

def boot():
    duration = int(FILES.loadline(FILENAME,ROW_WAIT_FOR_INTERNET_CONNECTION))
    time.sleep(duration)
    SUB.call(['/home/pi/CUBE/serverStart.sh'])

#MAIN

boot()
