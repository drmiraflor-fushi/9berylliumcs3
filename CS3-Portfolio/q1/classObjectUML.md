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
### Why did you choose this class? - I choose this class because it's a situation that I often find myself 
                                    enjoy indulging in. Spotify Playlist, and perhaps Spotify in its entirety, 
                                    is interesting, fun, and customizable. 
### Which property is the most important? Why? - The most important property is the song. A playlist wouldn't be a 
                                                playlist without its songs -- songs is what makes up a playlist.
### Which method is the most useful? Why? - I personally believe that the most useful method is the 'play' method. 
                                            It allows the user to execute the songs, and again, a playlist would not exist 
                                            without its songs, and it would be useless if the songs cannot be played or listened to.
