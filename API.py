#API

from flask import request
from flask_api import FlaskAPI

import DATA
import HISTORY
import SCHEDULE

import PUMP

#PROPERTIES

app = FlaskAPI(__name__)

#ENDPOINTS

@app.route('/deviceInit/', methods=["GET"])
def deviceInit():
    print("API - DEVICE INIT")
    if request.method == "GET":
        time = HISTORY.save_deviceInit()

    return {"data":{"time":time}}

@app.route('/getDevice/', methods=["GET"])
def getDevice():
    print("API - DEVICE")
    if request.method == "GET":
        volumeMax = DATA.load_volumeMax()
        warningPercentage = DATA.load_warningPercentage()
        warningDaysLeft = DATA.load_warningDaysLeft()

        pouringInProgress = DATA.load_pouringInProgress()
        percentage = DATA.load_percentage()
        volume = DATA.load_volume()
        daysLeft = DATA.load_daysLeft()

        name = DATA.load_name()
        date = DATA.load_date()
        duration = DATA.load_duration()
        skipDays = DATA.load_skipDays()

        events = HISTORY.load_allEvents()

    return {"data":{"volumeMax":volumeMax,"warningPercentage":warningPercentage,"warningDaysLeft":warningDaysLeft,"pouringInProgress":pouringInProgress,"percentage":percentage,"volume":volume,"daysLeft":daysLeft,"name":name,"date":date,"duration":duration,"skipDays":skipDays,"events":events}}

@app.route('/manualPouring/', methods=["POST"])
def manualPouring():
    print("API - POURING")
    if request.method == "POST":
	   seconds = float(request.data.get("duration"))
	   HISTORY.save_manualPour(seconds)
	   PUMP.start(seconds)

    return {"data":{}}

@app.route('/updateSchedule/', methods=["POST"])
def updateSchedule():
    print("API - UPDATE SCHEDULE")
    if request.method == "POST":
        enabled = int(request.data.get("enabled"))
        name = request.data.get("name")
        date = request.data.get("date")
        duration = float(request.data.get("duration"))
        skipDays = int(request.data.get("skipDays"))
        SCHEDULE.update(enabled,name,date,duration,skipDays)
    return {"data":{}}

#MAIN

if __name__ == "__main__":
    app.run()
