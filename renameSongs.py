import os

songs = os.listdir("songs/")
for song in songs:
    print(song)
    os.rename("songs/"+song,"songs/"+song.strip().replace(" ", "").replace("'", ""))