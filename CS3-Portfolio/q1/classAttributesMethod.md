# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Artist | str | Public | This attribute is public because some users search up the name of the artist, not his/her album or song |
| Song | str | Public | This attribute is public because the titles of songs are more often searched up compared to other attributes
| Status | str | Privacy | This attribute is private because only the creator of the playlist can see if it (the playlist) is made private; on the other hand, the 'public' status will only be seen by other users, if it (the playlist) is made public. |
| Album | str | Public | This attribute is public because albums contain songs, and users may want to stream to the album's contents |
| Genre | str | Public | This attribute is public because songs -- or albums -- are categorized according to their music genre |

## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
I chose to make my chosen attribute, Status, private because it provides functionality, customization, and confidentiality to the users. Additionally, 
### Which method changes the state of your object?

### How did your two objects demonstrate that instances are independent?

### What is the difference between your class diagram and your object diagram?
