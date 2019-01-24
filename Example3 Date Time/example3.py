#using datetime library
from datetime import datetime

#getting current time
now = datetime.now()

#print the current time
print "This is our third example just printing date and time"
print "Current Date: %02d-%02d-%04d Current Time: %02d:%02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute, now.second)