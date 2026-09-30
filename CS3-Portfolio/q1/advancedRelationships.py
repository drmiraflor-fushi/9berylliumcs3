class SpotifyPlaylist:
    """Parent Class: Represents a generic Audio Track in Spotify"""
    def __init__(self, title: str, creator: str, duration_sec: int, status: str = "Public"):
        self.title = title
        self.creator = creator
        self.duration_sec = duration_sec
        self.__status = status

    def get_status(self) -> str:
        return self.__status

    def update_status(self, new_status: str) -> None:
        if new_status in ["Public", "Private"]:
            self.__status = new_status

    def get_details(self) -> str:
        mins, secs = divmod(self.duration_sec, 60)
        return f"'{self.title}' by {self.creator} [{mins}:{secs:02d}] - Status: {self.__status}"


# --- STEP 3 & 5: INHERITANCE (IS-A Relationship) ---
class PodcastTrack(SpotifyPlaylist):
    """Child Class: PodcastTrack IS-A SpotifyPlaylist track with extra episode info"""
    def __init__(self, title: str, creator: str, duration_sec: int, episode_num: int, host: str):
        # Reusing parent class initialization using super()
        super().__init__(title, creator, duration_sec)
        self.episode_num = episode_num
        self.host = host

    # Overriding method to add specific podcast info (reusing parent method)
    def get_details(self) -> str:
        base_details = super().get_details()
        return f"[Podcast Ep. {self.episode_num}] {base_details} (Hosted by {self.host})"


# --- STEP 8: DEPENDENCY CLASS (USES-A Relationship) ---
class AudioPlayer:
    """Dependency Class: Used temporarily by User to output audio"""
    def play_audio(self, track: SpotifyPlaylist) -> None:
        print(f"▶ [NOW PLAYING] {track.get_details()}")


# --- STEP 6 & 7: AGGREGATION CLASS (HAS-A Relationship) ---
class User:
    """User Class: Aggregates tracks in saved_songs and uses AudioPlayer"""
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        # Aggregation: saved_songs holds external SpotifyPlaylist references
        self.saved_songs = []

    def add_song(self, song_object: SpotifyPlaylist) -> None:
        if isinstance(song_object, SpotifyPlaylist):
            self.saved_songs.append(song_object)
            print(f"Added '{song_object.title}' to {self.username}'s saved_songs.")

    # DEPENDENCY METHOD: User USES-A AudioPlayer temporarily to stream a song
    def stream_song(self, song_index: int, player: AudioPlayer) -> None:
        if 0 <= song_index < len(self.saved_songs):
            song_to_play = self.saved_songs[song_index]
            player.play_audio(song_to_play)
        else:
            print("Invalid song selection!")

    def display_saved_songs(self) -> None:
        print(f"\n--- {self.username}'s Saved Songs ({len(self.saved_songs)} items) ---")
        for idx, song in enumerate(self.saved_songs):
            print(f"{idx + 1}. {song.get_details()}")


if __name__ == "__main__":
    print("=== TEST 1: INHERITANCE (Parent & Child) ===")
    song1 = SpotifyPlaylist("SZA", "Good Days", 17)
    podcast1 = PodcastTrack("Jujutsu Kaisen Season 4", "Gege Talks", 1892, 37, "Danielle")

    print(song1.get_details())
    print(podcast1.get_details())  # Demonstrates inherited + child features

    print("\n=== TEST 2: AGGREGATION (User HAS-A saved_songs) ===")
    user1 = User("danielle_yass", "danielle@unicorns.com")
    user1.add_song(song1)
    user1.add_song(podcast1)
    user1.display_saved_songs()

    print("\n=== TEST 3: DEPENDENCY (User USES-A AudioPlayer) ===")
    player_device = AudioPlayer()
    # User uses player_device temporarily to stream the second saved track
    user1.stream_song(1, player_device)
