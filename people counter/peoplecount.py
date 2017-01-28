import RPi.GPIO as GPIO
import time, datetime, csv
from dbhelper import DBHelper


####    Setup Global variables    ####
db = DBHelper()
GPIO.setmode(GPIO.BCM)
PIR_pin=23
GPIO.setup(PIR_pin, GPIO.IN)
peoplecount = 1
current_state = 0
previous_state = 0

def count():
    global peoplecount
    global previous_state
    print "presence detected total number %s" %peoplecount
    peoplecount += 1
    previous_state = 1

def save_record():
    global peoplecount
    t = datetime.datetime.now()
    date = t.strftime("%Y-%m-%d")
#    timeNow = t.strftime("%H-%M")
    timeNow = int(t.strftime("%H%M"))
    count = peoplecount / 2
    if timeNow > 859 and timeNow <=1700:
        db.add_record(date, timeNow, count)
        print "%s people added to record" %count
    else:
        print "Outside of recording time"
    count = 0
    peoplecount = 0
    time.sleep(2)

def main():
    db.setup()
    global previous_state
    print "test starting (CTRL-C to exit)"

    try:
        print "waitint for PIR to settle..."
        #loop until PIR output is 0
        while GPIO.input(PIR_pin) ==1:
            current_state = 0
        print "Ready"

        while True:
            current_state = GPIO.input(PIR_pin)
            if current_state == 1 and previous_state == 0:
             #PIR has been triggered
                count()
            elif current_state ==0 and previous_state ==1:
             #PIR has returned to ready state
                print "ready"
                previous_state=0

            #wait for 10 milliseconds
            time.sleep(0.01)

            t = datetime.datetime.now().strftime("%M:%S")
            if t == "00:00" or t == "15:00" or t == "30:00" or t == "45:00":
                save_record()

    except KeyboardInterrupt:
        print "Program Quit"

if __name__=='__main__':
    main()
