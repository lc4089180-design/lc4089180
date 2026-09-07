#Create a Python class called Song representing a Spotify song with attributes title, artist, and duration. Instantiate two Song objects and print their details.
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def display_details(self):
        print("Title:", self.title)
        print("Artist:", self.artist)
        print("Duration:", self.duration, "minutes")


song1 = Song("Kesariya", "Arijit Singh", 4.28)
song2 = Song("Tum Hi Ho", "Arijit Singh", 4.22)

song1.display_details()
print()
song2.display_details()