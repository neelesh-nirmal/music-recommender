import logging

from app.entities.library import Library
from app.entities.song import Song
from app.entities.user import User
from app.strategy.strategy import RecommenderStrategy

logger = logging.getLogger(__name__)


class FriendsPlaylistBasedRecommenderStrategy(RecommenderStrategy):
    def songs(self, user: User, library: Library) -> list[Song]:
        recommendations = []

        for song in library.songs:
            song_present_in_friends_list = 0

            if user.playlist.contains(song):
                continue

            for friend in user.friends:
                if friend.playlist.contains(song):
                    logger.info(f"{song.name} found in {friend.name}")
                    song_present_in_friends_list += 1
            recommendations.append((song, song_present_in_friends_list / len(user.friends)))

        recommendations.sort(key=lambda x: x[1], reverse=True)
        return [song for song, score in recommendations if score > 0]
