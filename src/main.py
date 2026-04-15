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

    profiles = [
        ("Pop Happy", {
            "genre": "pop", "mood": "happy",
            "energy": 0.80, "valence": 0.82, "tempo_bpm": 120,
            "danceability": 0.80, "acousticness": 0.20,
        }),
        ("Chill Lofi", {
            "genre": "lofi", "mood": "chill",
            "energy": 0.38, "valence": 0.58, "tempo_bpm": 76,
            "danceability": 0.60, "acousticness": 0.78,
        }),
        ("Deep Intense Rock", {
            "genre": "rock", "mood": "intense",
            "energy": 0.91, "valence": 0.45, "tempo_bpm": 150,
            "danceability": 0.65, "acousticness": 0.10,
        }),
        ("Slow and Melodic", {
            "genre": "folk", "mood": "dreamy",
            "energy": 0.30, "valence": 0.70, "tempo_bpm": 82,
            "danceability": 0.45, "acousticness": 0.90,
        }),

        # --- Adversarial / Edge Case Profiles ---

        # Only one melancholic song exists (Rainy Season, energy 0.55).
        # Does the +1.5 mood bonus rescue a song with a terrible energy fit?
        ("High Energy Melancholic", {
            "genre": "hip-hop", "mood": "melancholic",
            "energy": 0.95, "valence": 0.25, "tempo_bpm": 140,
            "danceability": 0.90, "acousticness": 0.05,
        }),

        # "reggae" does not exist in the catalog — zero genre matches are possible.
        # The entire ranking must fall back to numeric proximity alone.
        ("Genre Not in Catalog", {
            "genre": "reggae", "mood": "uplifting",
            "energy": 0.65, "valence": 0.80, "tempo_bpm": 95,
            "danceability": 0.78, "acousticness": 0.45,
        }),

        # No song in the catalog is simultaneously high-energy AND highly acoustic.
        # Every song will lose points on one of these two axes — what compromise wins?
        ("Acoustic Banger", {
            "genre": "folk", "mood": "intense",
            "energy": 0.97, "valence": 0.60, "tempo_bpm": 155,
            "danceability": 0.70, "acousticness": 0.95,
        }),

        # No genre, no mood, all numeric features at dead-center 0.5.
        # Without categorical anchors, do scores collapse into an indistinguishable blob?
        ("Perfectly Neutral", {
            "energy": 0.50, "valence": 0.50, "tempo_bpm": 110,
            "danceability": 0.50, "acousticness": 0.50,
        }),
    ]

    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print()
        print("=" * 54)
        print(f"  Profile : {profile_name}")
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
