#SUBMODULE:TIMES

import datetime

#PROPERTIES

FORMAT = "%Y-%m-%d %H:%M"

#ACTIONS

def now():
    return datetime.datetime.now().strftime(FORMAT)

def dateFrom(string):
    return datetime.datetime.strptime(string,FORMAT)
