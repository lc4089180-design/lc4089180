#Build a subclass called Podcast that inherits from the Song class, adds a new attribute host, and overrides the __str__ method to display all details including the host.
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration} minutes"


class Podcast(Song):
    def __init__(self, title, artist, duration, host):
        super().__init__(title, artist, duration)
        self.host = host

    def __str__(self):
        return f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration} minutes, Host: {self.host}"


podcast1 = Podcast("Tech Talk", "Spotify", 45, "Rahul")

print(podcast1)