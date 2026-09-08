# Class Attributes and Methods

## Previous Design
Link to my previous activity: [classObjectUML.md](classObjectUML.md)

## Design Revision
Changes from my previous design:
- Added attribute: `Status`
- Data Type: `str`
- Description: `Status` attribute refers to the publicity/privacy of the Spotify playlist.

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
| --- | --- | --- | --- |
| Artist | str | Public | Users search for tracks using artist names directly. |
| Song | str | Public | Track names are publicly accessible metadata. |
| Status | str | Private | Only playlist creators should be able to toggle whether a playlist is public or private to prevent unauthorized exposure. |
| Album | str | Public | Album titles are public music metadata used for grouping tracks. |
| Genre | str | Public | Genre information is open descriptive metadata. |

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
I made the `Status` attribute private so external code cannot directly change the privacy state without passing proper validation rules[cite: 1]. Direct access could accidentally expose private user playlists or bypass access permission checks.

### Which method changes the state of your object?
The `update_status()` method changes the state of the object by taking a `new_status` string parameter and updating the private `__status` attribute after checking if the input is valid[cite: 1].

### How did your two objects demonstrate that instances are independent?
When `update_status("Private")` was executed on `track1`, its status changed to "Private", while `track2` remained completely unaffected with a status of "Public"[cite: 1]. This confirms each instantiated object manages its own distinct memory space[cite: 1].

### What is the difference between your class diagram and your object diagram?
The class diagram acts as an abstract template defining general properties, methods, visibility symbols, and data types. The object diagram displays concrete runtime instances (`track1` and `track2`) holding specific field values like `"Niki"` and `"Tsunami"` are independent.

\
