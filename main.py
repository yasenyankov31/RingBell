import datetime
from datetime import date
import calendar
from imaplib import Commands
import time as t
import subprocess
import multiprocessing as mp
import os
import random
from mutagen.mp3 import MP3




def sleep(x):
    for x in range(x):
        t.sleep(1)

def play_song(command):
    subprocess.call(command, shell=True)

def get_all_songs():
    songs = os.listdir("songs/") 
    return songs

def main():
    schedule=[]
    command_bell="mplayer songs/bell.mp3"
    command_song="mplayer "
    all_songs=get_all_songs()
    prevhour=""
    counter=0
    #fill schedule list
    f = open("schedule.txt", "r")
    for time in f:
        schedule.append(time.replace("\n",''))

    while True:
        my_date = date.today()
        day=calendar.day_name[my_date.weekday()]
        if day!="Sunday" and day!="Saturday":
            now = datetime.datetime.now().strftime('%H:%M')
            print(now)
            if now in schedule and now!=prevhour:
                counter+=1
                prevhour=now
                subprocess.call(command_bell,shell=True)
                sleep(5)
                if counter==6:
                    rng_song=command_song+random.choice(all_songs)
                    task1=mp.Process(target=play_song,args=(rng_song,))
                    task1.start()
                    duration = int(MP3(rng_song).info.length)
                    sleep(duration)
                    subprocess.call('pkill mplayer', shell=True)
                    task1.kill()
                elif counter==14:
                    counter=0
                #write log
                w=open("log.txt","a")
                w.write(now+" "+str(my_date)+"\n")
                w.close()
        sleep(10)




if __name__ == "__main__":
    main()
    
