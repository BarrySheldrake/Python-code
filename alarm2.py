#import modules needed
import datetime
import webbrowser
import random

#alarm should pick one a random link listed in a text file
urls = open('alarm_links.txt', 'r').read().split('\n')
play = urls[random.randint(0,4)]

#Get the current time and convert to a string
t = datetime.datetime.now()
hour = t.strftime("%H")
minute = t.strftime("%M")
print t.strftime("Today's date is: %d-%m-%y")
print "The time is currently: %s:%s" % (hour, minute)

#get the user input for the time of the alarm
print "What time would you like the alarm set for?"
target_hour = raw_input("24-hour clock, what hour?")
target_minute = raw_input("24-hour clock, what minute?")
print "The alarm is set for %s:%s" % (target_hour, target_minute)

#Compare the two to get the duration of a countdown

while True:
	t = datetime.datetime.now()
	if t.strftime("%M")  == target_minute:
		webbrowser.get('firefox').open(play)
		urls.close()
		break
