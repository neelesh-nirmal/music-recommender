from abc import ABC, abstractmethod

from app.entities.library import Library
from app.entities.song import Song
from app.entities.user import User


class RecommenderStrategy(ABC):
    @abstractmethod
    def songs(self, user: User, library: Library) -> list[Song]:
        pass
