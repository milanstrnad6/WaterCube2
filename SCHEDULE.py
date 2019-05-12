#MANAGER:SCHEDULE

import datetime

import FILES
import TIMES
import HISTORY
import STATUS
import PUMP

#PROPERTIES

FILENAME = '/home/pi/CUBE/DATA/schedule.txt'
ROW_SCHEDULE_ON = 1
ROW_SKIP_DAYS = 3
ROW_PUMP_DURATION = 5

#ACTIONS

def pourIfNeeded():
    print("SCHEDULE - POUR IF NEEDED")

    isScheduleOn = int(FILES.loadline(FILENAME,ROW_SCHEDULE_ON))
    if isScheduleOn == 1:

	nextPour = STATUS.loadAutomaticPourScheduled()
	next = TIMES.dateFrom(nextPour)
	print("SCHEDULE - POUR IF NEEDED - NEXT:")
	print(next)
	now = datetime.datetime.now()
	print("SCHEDULE - POUR IF NEEDED - NOW:")
	print(now)

	skipDays = int(FILES.loadline(FILENAME,ROW_SKIP_DAYS))

	if now.date() == next.date() and now.time().hour == next.time().hour and now.time().minute == next.time().minute:
	    print("SCHEDULE - POUR IF NEEDED - [IT IS TIME!]")

	    #Check water!

	    #Pouring...
	    duration = float(FILES.loadline(FILENAME,ROW_PUMP_DURATION))
	    HISTORY.saveEventAutomaticPour(duration)
	    STATUS.saveAutomaticPourLast(TIMES.nowAsString())
	    PUMP.start(duration)

	    #Prepare next.
	    scheduled = next + datetime.timedelta(days=skipDays+1)
	    STATUS.saveAutomaticPourScheduled(TIMES.stringFrom(scheduled))

	elif now > next:
	    print("SCHEDULE - POUR IF NEEDED - [NEED TO UPDATE AUTOMATIC_POUR_SCHEDULED DATE]")
	    while next <= now:
		next = next + datetime.timedelta(days=skipDays+1)
	    STATUS.saveAutomaticPourScheduled(TIMES.stringFrom(next))
	else:
	    print("SCHEDULE - POUR IF NEEDED - [IT IS NOT TIME YET]")
