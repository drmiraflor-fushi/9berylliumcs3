# Class Relationships: Association and Multiplicity

## Previous Work
- [Part 1 - Classes and Objects](classObjectUML.md)
- [Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
- **Class:** 'SpotifyPlaylist'
- **Description:** This represents individual song tracks within a "Spotify" system, storing various metadata such as artist, song title, album, genre, and access status.

## New Related Class
- **Class:** 'user'
- **Description:** Represents a Spotify account user who creates, manages, and saves songs into a playlist.

## Association
- **Relationship:** 'User' manages or contains 'SpotifyPlaylist' tracks.
- **Explanation:** A 'User' object maintains a list of references to 'SpotifyPlaylist'.

## Multiplicity
- **Multiplicity:** '1' to '0..*' (is One-to-Many)
- **Explanation:** Exactly 1 'user' can own and manage zero or many 'SpotifyPlaylist' tracks in their saved library.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
