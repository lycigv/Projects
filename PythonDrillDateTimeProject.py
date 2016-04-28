
import datetime
import time

from time import strftime

from datetime import  datetime
from pytz import timezone



def branch():    
    timezonelist = ['US/Eastern','US/Pacific','Europe/London']
    fmt = "%Y-%m-%d %H:%M %Z"
    for zone in timezonelist:
        now_time = datetime.now(timezone(zone))
        print now_time.strftime(fmt)
        
        Branchtime=int(now_time.strftime('%H'))
##        print Branchtime
##        print type(Branchtime)
        if Branchtime > 9 and Branchtime < 21:
            print "This Branch is OPEN"

        else:
            print "This Branch is CLOSED"
      
branch()

print "EDT= NYC time, PDT= Portland time, BST= London time"

