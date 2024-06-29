import logging

from app.entities.library import Library
from app.entities.playlist import Playlist
from app.entities.song import Song
from app.entities.user import User
from app.recommender import MusicRecommender
from app.strategy.basic_recommender import BasicRecommenderStrategy
from app.strategy.friends_playlist_based_recommender import FriendsPlaylistBasedRecommenderStrategy

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main():
    # Add songs to the system
    song1 = Song("Song1", "Rock", "Fast", "Singer1", 80, 2020)
    song2 = Song("Song2", "Pop", "Medium", "Singer2", 75, 2019)
    song3 = Song("Song3", "Jazz", "Slow", "Singer3", 85, 2018)
    song4 = Song("Song4", "Classical", "Slow", "Singer4", 95, 2017)
    song5 = Song("Song5", "Rock", "Medium", "Singer5", 70, 2021)
    song6 = Song("Song6", "Pop", "Fast", "Singer6", 90, 2022)
    song7 = Song("Song7", "Jazz", "Medium", "Singer7", 60, 2020)
    song8 = Song("Song8", "Classical", "Fast", "Singer8", 85, 2019)
    song9 = Song("Song9", "Rock", "Slow", "Singer9", 75, 2018)
    song10 = Song("Song10", "Pop", "Slow", "Singer10", 80, 2021)

    library: Library = Library(name='main', songs=[
        song1, song2,
        song3, song4,
        song5, song6,
        song7, song8,
        song9, song10
    ])

    playlist1 = Playlist(name="playlist1", songs=[song1, song3, song5])
    playlist2 = Playlist(name="playlist2", songs=[song1, song4, song8, song7])
    playlist3 = Playlist(name="playlist3", songs=[song2, song6, song10, song9])

    user1 = User(name="user1", playlist=playlist1)
    user2 = User(name="user2", playlist=playlist2, friends=[user1])
    user3 = User(name="user3", playlist=playlist3, friends=[user2, user1])
    user4 = User(name="user4", playlist=playlist1, friends=[user2, user1])

    basic_recommender = MusicRecommender(library=library, strategy=BasicRecommenderStrategy())
    songs: list[Song] = basic_recommender.recommended_songs(user3)
    logger.info(f"Recommended songs for user3 using basic recommender: {[s.name for s in songs]}")

    advance_recommender = MusicRecommender(library=library, strategy=FriendsPlaylistBasedRecommenderStrategy())
    songs: list[Song] = advance_recommender.recommended_songs(user3)
    logger.info(f"Recommended songs for user3 using advance recommender: {[s.name for s in songs]}")


if __name__ == "__main__":
    print(f'starting')
    main()
