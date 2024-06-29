from dataclasses import dataclass, asdict


@dataclass
class Song:
    name: str
    genre: str
    tempo: str
    singer: str
    popularity_score: str
    release_year: str

    @property
    def attributes(self):
        return asdict(self)
