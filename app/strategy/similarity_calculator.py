from dataclasses import fields

from app.entities.song import Song


class SimilarityCalculator:
    def calculate_similarity(self, song1: Song, song2: Song) -> float:
        common_attributes: int = 0
        attributes = [field.name for field in fields(Song)]

        for attr in attributes:
            if getattr(song1, attr) == getattr(song2, attr):
                common_attributes += 1

        total_attributes = len(attributes)
        return common_attributes / total_attributes
