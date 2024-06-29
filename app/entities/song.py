from dataclasses import dataclass, asdict


@dataclass
class Song:
    name: str
    genre: str
    tempo: str
    singer: str
    popularity_score: int
    release_year: int

    @property
    def attributes(self):
        return asdict(self)

    def __str__(self):
        return f"Song(name='{self.name}')"

    def __repr__(self):
        return f"Song(name='{self.name}')"
