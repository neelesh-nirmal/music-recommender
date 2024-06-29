import logging

from app.entities.song import Song

logger = logging.getLogger(__name__)


class Library:
    def __init__(self, name: str, songs: list[Song] = None):
        self.__name: str = name

        self.__songs: dict[str, Song] = {}
        if songs:
            self.__songs = {song.name: song for song in songs}

        logger.info(f"Library {self.__name} created with {len(self.__songs)} songs")

    @property
    def songs(self) -> list[Song]:
        return list(self.__songs.values())

    def add_song(self, song: Song):
        self.__songs[song.name] = song
        logger.info(f"Song {song.name} added to the library")

    def remove_song(self, song: Song) -> None:
        del self.__songs[song.name]
        logger.info(f"Song {song.name} removed from the library")

    def search(self, ):
        raise NotImplemented()
