import datetime
from datetime import date
import calendar
import time as t
import subprocess
import multiprocessing as mp
import os
import random
from mutagen.mp3 import MP3

songs = os.listdir("songs/") 
for song in songs:
    print(song)
    os.rename("songs/"+song,"songs/"+song.strip().replace(" ", ""))