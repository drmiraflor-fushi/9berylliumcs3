class SpotifyPlaylist:
  def __init__(self, artist: str, song: str, album: str, genre: str, status: str = "Public"):
    self.artist = artist
    self.song = song
    self.album = album
    self.genre = genre
    self.status = status

def get_status(self) -> str:
  return self.status

def update_status(self, new_status: str) -> None:
  real_statuses = ["Public", "Private"]
  if new_status in real_statuses:
    self.status = new_status
  else:
    print("Invalid status! Choose 'Public' or 'Private' only.")

def display_details(self) -> str:
  return f"'{self.song}' by {self.artist} ({self.album}) [{self.genre}] - Status:{self.status}"

class User:
  def --init--(self, username: str, email:str):
  self.username = username
  self.email = email
  self.savedsongs = []
  def add_track(self, track_object, SpotifyPlaylist):
    if ininstance(track_obkect, SpotifyPlaylist):
      self.savedsongs.append(track_object)
      print(f"Added '{track_object.song}' to {self.username}'s library.")
    else:
      print("Error: That is an invalid object type. Try again!")
  def display_library(self) -> None:
    print(f"\n---{self.username}'s Spotify Library ({len(self.savedsongs)} tracks) ---")
    if not self.savedsongs:
      print("Sorry. No tracks saved in library.")
    else: 
      for index, track in enumerate(self.savedsongs, start=1):
        print(f"{index}. {track.display_details()}")

if __name__ = "__main__":
  # Code some example outputs / instantiating objects with 1 user and 3 tracks
  user1 = User("danielle_yass", "danielle@unicorns.com")
  track1 = SpotifyPlaylist("SZA", "Normal Girl", "SOS", "RNB")
  track2 = SpotifyPlaylist("Will Wood", "Love, Me Normally", "Indie", "Wow")
  track3 = SpotifyPlaylist("Dove Cameron", "If Only", "Disney", "Descendants")

  # Produce test run outputs
  print("==BEFORE RELATIONSHIP==")
  print(f"User Created: {user1.username}")
  print(f"Track 1 Created: {track1.song}")
  print(f"Track 2 Created: {track2.song}")
  print(f"Track 3 Created: {track3.song}")
  user1.display_library()
  print("\n===BUILDING THE RELATIONSHIP===")
  user1.add_track(track1)
  user1.add_track(track2)
  user1.add_track(track3)

  # Access to track details through user1's savedsongs references
  print("\n==="AFTER RELATIONSHIP===")
  user1.display_library()
    

