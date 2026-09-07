#Create a Python dictionary called playlist with three songs, where each song has a title and artist, and print the artist of the second song.
playlist = {
    "song1": {
        "title": "Kesariya",
        "artist": "Arijit Singh"
    },
    "song2": {
        "title": "Tum Hi Ho",
        "artist": "Arijit Singh"
    },
    "song3": {
        "title": "Chaleya",
        "artist": "Arijit Singh"
    }
}

print("Artist of second song:", playlist["song2"]["artist"])