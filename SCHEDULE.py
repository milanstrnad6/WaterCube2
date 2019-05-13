#MANAGER:SCHEDULE

import datetime

import DATA
import HISTORY
import TIMES

import PUMP

#ACTIONS

def pourIfNeeded():
    print("SCHEDULE - POUR IF NEEDED")

    isScheduleEnabled = DATA.load_enabled()
    if isScheduleEnabled == 1:

		next = TIMES.dateFrom(DATA.load_date())
		print("SCHEDULE - POUR IF NEEDED - NEXT:")
		print(next)

		now = datetime.datetime.now()
		print("SCHEDULE - POUR IF NEEDED - NOW:")
		print(now)

		skipDays = DATA.load_skipDays()

		if now.date() == next.date() and now.time().hour == next.time().hour and now.time().minute == next.time().minute:
	    	print("SCHEDULE - POUR IF NEEDED - [IT IS TIME!]")

	    	#Check water!

	    	#Pouring...
	    	HISTORY.save_automaticPour(duration)
	    	PUMP.start(DATA.load_duration())

	    	#Prepare next.
	    	scheduled = next + datetime.timedelta(days=skipDays+1)
	    	DATA.save_date(TIMES.stringFrom(scheduled))

		elif now > next:
	  		print("SCHEDULE - POUR IF NEEDED - [NEED TO UPDATE AUTOMATIC_POUR_SCHEDULED DATE]")
	  		
	  		while next <= now:
			next = next + datetime.timedelta(days=skipDays+1)
			DATA.save_date(TIMES.stringFrom(next))

		else:
	    	print("SCHEDULE - POUR IF NEEDED - [IT IS NOT TIME YET]")
