class Song:
    def __init__(self, name: str, genre: str, tempo: str, singer: str, popularity_score: int, release_year: int):
        self.name = name
        self.genre = genre
        self.tempo = tempo
        self.singer = singer
        self.popularity_score = popularity_score
        self.release_year = release_year

    def get_attributes(self) -> list:
        return [self.genre, self.tempo, self.singer, self.popularity_score, self.release_year]
