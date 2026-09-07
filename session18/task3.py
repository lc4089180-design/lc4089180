#Write a Playlist class that can store a list of Song and Podcast objects. Add a method add_item() to add songs or podcasts to the playlist, and a method show_playlist() to print all items with their details.
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"Song: {self.title} - {self.artist} - {self.duration} minutes"


class Podcast(Song):
    def __init__(self, title, artist, duration, host):
        super().__init__(title, artist, duration)
        self.host = host

    def __str__(self):
        return f"Podcast: {self.title} - Host: {self.host} - {self.duration} minutes"


class Playlist:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_playlist(self):
        print("Playlist:")
        for item in self.items:
            print(item)


song1 = Song("Kesariya", "Arijit Singh", 4.28)
podcast1 = Podcast("Tech Talk", "Spotify", 45, "Rahul")

my_playlist = Playlist()

my_playlist.add_item(song1)
my_playlist.add_item(podcast1)

my_playlist.show_playlist()