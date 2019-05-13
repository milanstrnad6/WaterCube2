#API

from flask import request
from flask_api import FlaskAPI

import HISTORY
import STATUS

import PUMP

#PROPERTIES

app = FlaskAPI(__name__)

#ENDPOINTS

@app.route('/deviceInit/', methods=["GET"])
def deviceInit():
    print("API - DEVICE INIT")
    if request.method == "GET":
        time = HISTORY.saveEventDeviceInit()
    return {"data":{"time":time}}

# @app.route('/history/', methods=["GET"])
# def api_history():
#     print("API - HISTORY")
#     if request.method == "GET":
# 	   events = HISTORY.loadAllEvents()
#     return {"data":{"events":events}}

# @app.route('/volume/', methods=["GET"])
# def api_volume():
#     print("API - VOLUME")
#     if request.method == "GET":
#     	volumeMax = STATUS.loadVolumeMax()
#    	    volume = STATUS.loadVolume()
#       	percentage = STATUS.loadPercentage()
#         warningPercentage = STATUS.loadWarningPercentage()
#     return {"data":{"volumeMax":volumeMax,"volume":volume,"percentage":percentage,"warningPercentage":warningPercentage}}

@app.route('/manualPouring/', methods=["POST"])
def manualPouring():
    print("API - POURING")
    if request.method == "POST":
	   seconds = float(request.data.get("seconds"))
	   HISTORY.saveEventManualPour(seconds)
	   PUMP.start(seconds)
    return {"data":{}}

#MAIN

if __name__ == "__main__":
    app.run()
