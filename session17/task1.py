#Create a Python class called Playlist that represents a music playlist with properties: name and songs (a list). Write a method add_song(song_name) to add a song to the playlist and print the updated list.
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def add_song(self, song_name):
        self.songs.append(song_name)
        print("Updated playlist:", self.songs)


my_playlist = Playlist("My Favorites", ["Kesariya", "Chaleya"])

my_playlist.add_song("Tum Hi Ho")