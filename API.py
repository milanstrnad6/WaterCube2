#API

from flask import request
from flask_api import FlaskAPI

import DATA
import HISTORY

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

@app.route('/device/', methods=["GET"])
def device():
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
	   seconds = float(request.data.get("seconds"))
	   HISTORY.save_manualPour(seconds)
	   PUMP.start(seconds)

    return {"data":{}}

#MAIN

if __name__ == "__main__":
    app.run()
