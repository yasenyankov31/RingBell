import os 
import datetime
from datetime import date
import calendar
import time as t
import subprocess
import multiprocessing as mp



def sleep(x):
    for x in range(x):
        t.sleep(1)

def main():
    schedule=[]
    command="mplayer /songs/schoolbell_yordan.mp3"
    prevhour=""
    #fill schedule list
    f = open("schedule.txt", "r")
    for time in f:
        schedule.append(time.replace("\n",''))

    while True:
        my_date = date.today()
        day=calendar.day_name[my_date.weekday()]
        if day!="Sunday" and day!="Saturday":
            now = datetime.datetime.now().strftime('%H:%M')
            if now in schedule and now!=prevhour:
                prevhour=now
                os.system(command)
                #write log
                w=open("log.txt","a")
                w.write(now+" "+str(my_date)+"\n")
                w.close()
        sleep(10)

def play_song():
    subprocess.call('cd mplayer && mplayer songs/song.mp3', shell=True)


if __name__ == "__main__":
    # task1=mp.Process(target=play_song)
    # task1.start()
    # sleep(5)
    # subprocess.call('taskkill /f /im mplayer.exe', shell=True)
    # print("end")
    main()
