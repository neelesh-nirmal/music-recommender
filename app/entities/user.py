from app.entities.playlist import Playlist


class User:
    def __init__(self, name: str, playlists: list[Playlist] = None, friends: list['User'] = None):
        self.name = name
        self.__playlist: list[Playlist] = playlists if playlists else []
        self.__friends: list['User'] = friends if friends else []

    @property
    def playlist(self) -> list[Playlist]:
        return self.__playlist

    @property
    def friends(self) -> list['User']:
        return self.__friends

    def add_playlist(self, playlist: Playlist):
        self.__playlist.append(playlist)

    def add_friend(self, friend: 'User'):
        self.__friends.append(friend)
