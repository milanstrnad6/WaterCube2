#BOOT MODULE:SERVER

import subprocess as SUB
import time

import DATA

#ACTIONS

def boot():
    duration = DATA.load_waitForInternetConnection()
    time.sleep(duration)
    SUB.call(['/home/pi/CUBE/serverStart.sh'])

#MAIN

boot()
