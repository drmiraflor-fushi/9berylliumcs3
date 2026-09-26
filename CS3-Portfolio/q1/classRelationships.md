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

## Analysis

### What is the association between your two classes?
The association between `User` and `SpotifyPlaylist` is a unidirectional "has-a" or "manages" relationship. A `User` object actively holds and organizes `SpotifyPlaylist` track objects within its profile library.

### What multiplicity did you choose and why?
I chose a 1 to 0..* (One-to-Many) multiplicity because a single user account can own anywhere from zero to multiple saved songs in their playlist. Conversely, in this specific system, each track instance in the user's library list belongs directly to that specific user's collection view.

### How did you implement the relationship in Python?
The relationship was implemented in Python by initializing an empty `savedsongs` list in the `User` class `__init__()` method. The `add_track()` method then appends the actual `SpotifyPlaylist` object reference directly into that list.

### Why did you store an object reference instead of copying its data?
Storing direct object references ensures data integrity and single-source truth across the application. If properties like `status` or track metadata change in the `SpotifyPlaylist` instance, the `User` object immediately reflects those updates without needing manual re-copying or string duplication.

### If your relationship uses many, why is a list appropriate?
A Python list is appropriate because it can dynamically grow or shrink as tracks are added or removed without requiring a fixed pre-defined size. Furthermore, a list stores memory references to complete object instances, allowing iteration and method calls (like `track.display_details()`) on each element during loops.
