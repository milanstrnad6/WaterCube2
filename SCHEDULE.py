#MODULE:SCHEDULE

import datetime

import FILES
import TIMES
import HISTORY
import STATUS
import PUMP

#PROPERTIES

FILENAME = '/home/pi/CUBE/DATA/schedule.txt'
ROW_SCHEDULE_ON = 1
ROW_DATETIME = 3 #not needed
ROW_SKIP_DAYS = 5
ROW_PUMP_DURATION = 7

#ACTIONS

def pourIfNeeded():
    print("SCHEDULE - POUR IF NEEDED")
    isScheduleOn = int(FILES.loadline(FILENAME,ROW_SCHEDULE_ON))
    if isScheduleOn == 1:
	#check if there was pour

    	lastPour = STATUS.loadLastPour()
	print("SCHEDULE - POUR IF NEEDED - LAST POUR:")
	print(lastPour)
	lastPourDate = TIMES.dateFrom(lastPour.rstrip())
	print("SCHEDULE - POUR IF NEEDED - LAST POUR DATE:")
	print(lastPourDate)

	skipDays = int(FILES.loadline(FILENAME,ROW_SKIP_DAYS))
	nextPourDate = lastPourDate + datetime.timedelta(days=skipDays)
	print("SCHEDULE - POUR IF NEEDED - NEXT POUR DATE:")
	print(nextPourDate)

	dateNow = datetime.datetime.now()

	if dateNow >= nextPourDate:
	    duration = float(FILES.loadline(FILENAME,ROW_PUMP_DURATION))
	    HISTORY.saveEventAutomaticPour(duration)
	    STATUS.saveLastPour(TIMES.now())
	    PUMP.start(duration)
