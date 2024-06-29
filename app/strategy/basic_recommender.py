from itertools import product

from app.entities.library import Library
from app.entities.song import Song
from app.entities.user import User
from app.strategy.similarity_calculator import SimilarityCalculator
from app.strategy.strategy import RecommenderStrategy


class BasicRecommenderStrategy(RecommenderStrategy):
    """
    Basic recommender strategy based on Similarity Index.
    """

    def songs(self, user: User, library: Library) -> list[Song]:
        recommendations = []

        sim_calculator: SimilarityCalculator = SimilarityCalculator()
        for library_song, playlist_song in product(library.songs, user.playlist.songs):
            if user.playlist.contains(library_song):
                continue

            score = sim_calculator.calculate_similarity(library_song, playlist_song)
            recommendations.append((library_song, score))

        recommendations.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in recommendations]
