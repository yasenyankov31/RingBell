import datetime
from datetime import date
import calendar
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
    subprocess.call("mplayer songs/"+command, shell=True)

def get_all_songs():
    songs = os.listdir("songs/") 
    return songs

def main():
    schedule=[]
    bigBreakschedule=[]
    command_bell="mplayer breakBell/bell.mp3"
    all_songs=get_all_songs()
    prevhour=""

    
    #fill schedule list
    f = open("schedule.txt", "r")
    for time in f:
        schedule.append(time.replace("\n",''))
    #fill big break schedule list
    a = open("scheduleBigBreaks.txt", "r")
    for time in a:
        bigBreakschedule.append(time.replace("\n",''))

    while True:
        my_date = date.today()
        day=calendar.day_name[my_date.weekday()]
        if day!="Sunday" and day!="Saturday":
            now = datetime.datetime.now().strftime('%H:%M')
            print(now)
            if now in schedule and now!=prevhour:
                prevhour=now
                subprocess.call(command_bell,shell=True)
                sleep(5)
                #write log
                w=open("log.txt","a")
                w.write(now+" "+str(my_date)+"\n")
                w.close()
            if now in bigBreakschedule:
                breakSongs={}
                fullDuration=0
                #add random songs in list
                while True:
                    rng_song=random.choice(all_songs)
                    print(rng_song)
                    if rng_song not in breakSongs:
                        duration = int(MP3("songs/"+rng_song).info.length)
                        if fullDuration+duration>=1200:  
                            duration=1200-fullDuration
                            breakSongs[rng_song]=str(duration-20)
                            break
                        breakSongs[rng_song]=str(duration)
                        fullDuration+=int(duration)
                print(breakSongs)
                for song, duration in breakSongs.items():
                    task=mp.Process(target=play_song,args=(song,))
                    task.start()
                    sleep(int(duration))
                    subprocess.call('pkill mplayer', shell=True)
                    task.kill()
                        
        sleep(10)




if __name__ == "__main__":
    main()
    
