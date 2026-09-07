#Write a lambda function to filter out all songs longer than 4 minutes from a list of tuples representing Spotify songs (each tuple contains song name and duration in minutes).
songs = [
    ("Kesariya", 4.28),
    ("Tum Hi Ho", 4.22),
    ("Chaleya", 3.20),
    ("Apna Bana Le", 4.21),
    ("Heeriye", 3.14)
]

short_songs = list(filter(lambda song: song[1] <= 4, songs))

print(short_songs)