"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded Songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print()
    print("=" * 54)
    print("  Top Recommendations")
    print("=" * 54)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n  #{rank}  {song['title']}  —  {song['artist']}")
        print(f"       Score : {score:.2f} / 6.50")
        print(f"       Genre : {song['genre']}  |  Mood : {song['mood']}")
        print("       " + "-" * 40)
        for reason in explanation.split("\n  "):
            print(f"       {reason}")

    print()
    print("=" * 54)


if __name__ == "__main__":
    main()
