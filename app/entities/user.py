from app.entities.playlist import Playlist


class User:
    def __init__(self, name: str, playlist: Playlist = None, friends: list['User'] = None):
        self.name: str = name
        self.__playlist: Playlist | None = playlist
        self.__friends: list['User'] = friends if friends else []

    @property
    def playlist(self) -> Playlist:
        return self.__playlist

    @property
    def friends(self) -> list['User']:
        return self.__friends

    def set_playlist(self, playlist: Playlist):
        self.__playlist = playlist

    def add_friend(self, friend: 'User'):
        self.__friends.append(friend)
