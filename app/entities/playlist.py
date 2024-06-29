from app.entities.song import Song


class Playlist:
    def __init__(self, name: str, songs: list[Song] = None):
        self.__name: str = name

        self.__songs: dict[str, Song] = {}
        if not songs:
            self.__songs = {song.name: song for song in songs}

    @property
    def songs(self) -> list[Song]:
        return list(self.__songs.values())

    @property
    def name(self) -> str:
        return self.__name

    def add(self, song: Song):
        self.__songs[song.name] = song

    def remove(self):
        raise NotImplementedError()

    def sort(self):
        raise NotImplementedError()
