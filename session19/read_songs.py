#Write a Python script that reads a list of song names from a text file called songs.txt and prints each song name with its line number, like a Spotify playlist.
#task1.py
with open("songs.txt", "r") as file:
    songs = file.readlines()

for number, song in enumerate(songs, start=1):
    print(number, song.strip())