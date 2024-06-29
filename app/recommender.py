import logging

from app.entities.library import Library
from app.entities.song import Song
from app.entities.user import User
from app.strategy.strategy import RecommenderStrategy

logger = logging.getLogger(__name__)


class MusicRecommender:
    def __init__(self, library: Library, strategy: RecommenderStrategy):
        self.__library: Library = library
        self.__strategy: RecommenderStrategy = strategy

        logger.info(f"Recommender created with {self.__strategy.__class__.__name__} strategy")

    def recommended_songs(self, user: User) -> list[Song]:
        return self.__strategy.songs(user=user, library=self.__library)
