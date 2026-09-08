# SG4 - Understanding Classes and objects
## Spotify Playlist
## Spotify Playlist features a fun variety of songs and customizable options for the user to access and use. 
## Properties
| Property | Data Type | Description |
|---|---|---|
| Artist | str | The 'artist' property is the name of the song's singer |
| Song | str | The 'song' property is the name of the song |
| Album | str | The 'album' property |
| Genre | str | The 'genre' is what category the album or the song falls under |
## Methods
| Method | Description |
|---|---|
| Play | 'Play' method allows the user to play or execute their desired song / album. |
| Stop | 'Stop' method allows the user to halt or pause their desired song / album. |
| Repeat | 'Repeat' method allows the user to repeat their desired song or album without 
            switching to a different song. This method can be used once or twice depending 
            on its purpose: once for the album repetition; twice for a selected song repetition. |
| Shuffle | 'Shuffle' method allows user to shuffle songs without following a strict song queue. |
| AddToLikedSongs | 'AddToLikedsongs' method allows the user to add their desired song or album 
                     to their liked songs.|
| DoNotPlayThisArtist | 'DoNotPlayThisArtist' allows the user to restrict an artist and his/her 
                        songs from showing up or playing. |
## Class Diagram
![Class Diagram](classObjectsUML.md.png)
## Design Explanation - I chose this design because it's simple and easy to follow. Every crucial item and information is featured.         
### Why did you choose this class? - I choose this class because it's a situation that I often find myself enjoy indulging in. Spotify Playlist, and perhaps Spotify in its entirety, is interesting, fun, and customizable. 
### Which property is the most important? Why? - playlist without its songs -- songs is what makes up a playlist.
### Which method is the most useful? Why? - I personally believe that the most useful method is the 'play' method. It allows the user to execute the songs, and again, a playlist would not exist without its songs, and it would be useless if the songs cannot be played or listened to.

## Design Revision
Changes from my previous design:
- Added attribute: Status
- Data Type: str
- Description: 'Status' attribute refers to the publicity / privacy of the Spotify playlist.

 
## Public & Private
|---|---|---|---|
| Attribute | Data Type | Visibility | Why Public / Private? |
| Artist | str | Public | This attribute is public because some users search up the name of the artist, not his/her album or song |
| Song | str | Public | This attribute is public because the titles of songs are more often searched up compared to other attributes
| Status | str | Privacy | This attribute is private because only the creator of the playlist can see if it (the playlist) is made private; on the other hand, the 'public' status will only be seen by other users, if it (the playlist) is made public. |
| Album | str | Public | This attribute is public because albums contain songs, and users may want to stream to the album's contents |
| Genre | str | Public | This attribute is public because songs -- or albums -- are categorized according to their music genre |

##Updated UML
+--------------------------------------------+
| Spotify Playlist |
+--------------------------------------------+
| + Artist : str |
| + Song : str |
| - Status : str |
| + Album : str |
| + Genre : str |
+--------------------------------------------+
| + Play() |
| + AddToLikedSongs(Song : str)|
| + Shuffle()
+--------------------------------------------+

