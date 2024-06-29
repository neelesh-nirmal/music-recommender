from app.song import Song


class User:
    def __init__(self, name: str):
        self.name = name
        self.playlist = []
        self.friends = []

    def add_song_to_playlist(self, song: Song):
        self.playlist.append(song)

    def add_friend(self, friend: 'User'):
        self.friends.append(friend)