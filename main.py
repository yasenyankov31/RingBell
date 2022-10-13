import os 
import datetime
from datetime import date
import calendar
import time as t


schedule=[]
def sleep(x):
    for x in range(x):
        t.sleep(1)

def main():
    command="mplayer schoolbell_yordan.mp3"
    f = open("schedule.txt", "r")
    for time in f:
        schedule.append(time.replace("\n",''))
    while True:
        my_date = date.today()
        day=calendar.day_name[my_date.weekday()]
        if day!="Sunday" and day!="Saturday":
            now = datetime.datetime.now().strftime('%H:%M:%S')
            print(now)
            if now in schedule:
                os.system(command)
                w=open("log.txt","a")
                w.write(now+"\n"+str(my_date))
                w.close()
                sleep(2)





if __name__ == "__main__":
    main()
