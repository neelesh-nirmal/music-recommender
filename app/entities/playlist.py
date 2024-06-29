import logging

from app.entities.song import Song

logger = logging.getLogger(__name__)


class Playlist:
    def __init__(self, name: str, songs: list[Song] = None):
        self.__name: str = name

        self.__songs: dict[str, Song] = {}
        if songs:
            self.__songs = {song.name: song for song in songs}

        logger.info(f"Playlist {self.__name} created with {len(songs)} songs")

    @property
    def songs(self) -> list[Song]:
        return list(self.__songs.values())

    @property
    def name(self) -> str:
        return self.__name

    def add(self, song: Song):
        self.__songs[song.name] = song
        logger.info(f"Song {song.name} added to the Playlist {self.__name}")

    def contains(self, song: Song):
        return song.name in self.__songs

    def remove(self):
        raise NotImplementedError()

    def sort(self):
        raise NotImplementedError()
