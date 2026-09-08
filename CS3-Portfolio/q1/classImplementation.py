class SpotifyPlaylist:
    def __init__(self, artist: str, song: str, album: str, genre: str, status: str = "Public"):
        # Public attributes
        self.artist = artist
        self.song = song
        self.album = album
        self.genre = genre
        
        # Private attribute (prefixed with double underscore)
        self.__status = status

    # Method 1: Returns/reads private status information
    def get_status(self) -> str:
        return self.__status

    # Method 2: Takes a parameter and modifies private attribute safely
    def update_status(self, new_status: str) -> None:
        valid_statuses = ["Public", "Private"]
        if new_status in valid_statuses:
            self.__status = new_status
            print(f"Playlist status changed to '{self.__status}'.")
        else:
            print("Invalid status! Use 'Public' or 'Private'.")

    # Method 3: Reads details about the song track
    def display_details(self) -> None:
        print(f"'{self.song}' by {self.artist} | Album: {self.album} | Genre: {self.genre} | Status: {self.__status}")


if __name__ == "__main__":
    # Step 6: Create two independent track/playlist objects
    track1 = SpotifyPlaylist("Niki", "Tsunami", "KidsThatFly", "Indie", "Public")
    track2 = SpotifyPlaylist("MingyuKalbo", "SEVENTEEN", "Habit", "K-Pop", "Public")

    # Step 7: Display initial state
    print("=== BEFORE ===")
    track1.display_details()
    track2.display_details()

    # Call method on track1 ONLY
    print("\n--- Modifying track1 status ---")
    track1.update_status("Private")

    # Display final state demonstrating independence
    print("\n=== AFTER ===")
    track1.display_details()  # Status is updated to Private
    track2.display_details()  # Status remains Public
