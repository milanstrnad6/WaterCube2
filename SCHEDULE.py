#MODULE:SCHEDULE

import datetime

import DATA
import HISTORY
import TIMES
import CONVERTOR

import PUMP

#ACTIONS

def update(enabled,name,date,ml,skipDays):
	print("SCHEDULE - UPDATE")
	DATA.save_enabled(enabled)
	DATA.save_name(name)
	DATA.save_date(date)
	DATA.save_ml(ml)
	DATA.save_skipDays(skipDays)

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

			ml = DATA.load_ml()
			volume = DATA.load_volume()

			if volume >= ml:
				#Pouring...
				HISTORY.save_automaticPour(ml)
				duration = CONVERTOR.getDurationFrom(ml)
				PUMP.start(duration)
			else:
				HISTORY.save_automaticPourNotPossible(ml) #NOT ENOUGH WATER

			#Prepare next.
			scheduled = next + datetime.timedelta(days=skipDays+1)
			DATA.save_date(TIMES.stringFrom(scheduled))

		elif now > next:
			print("SCHEDULE - POUR IF NEEDED - [NEED TO UPDATE AUTOMATIC_POUR_SCHEDULED DATE]")

			while next <= now:
				HISTORY.save_automaticPourNotPossibleWithDate(ml,next) #DEVICE OFFLINE
				next = next + datetime.timedelta(days=skipDays+1)
			DATA.save_date(TIMES.stringFrom(next))

		else:
			print("SCHEDULE - POUR IF NEEDED - [IT IS NOT TIME YET]")
