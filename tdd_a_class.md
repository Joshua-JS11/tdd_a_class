# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

adding name of track and artist.

making a list of tracks including name and artist 

output would be a list of strings

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE
class Music_list:

    def __init__(self)
    # sets a blanc starting list
    # returns nothing
    # side effects none
    pass

    def add_track(self, track_name:str, track_artist:str):
    # parameters: track name = string representing the name of the track. 
    # track artist = string representing the name of the artist
    # returns nothing
    # side effects: creates string which is the artist and track name into one string.
    # add that string to the end of the list
    pass

    def track_list(self)
     # parameters: none
     # returns updated list in the order the tracks was added.
     # side effects: none
     pass 


```


## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
when a new object is created from the class Music_list
A new empty list is created.
"""

music_list = Music_list()
music_list.track_list() # => empty list []


""""
given a track name and artist name these are added to the list as a string.

in a string formatted "artist name: track name"

""""
music_list = Music_list()
music_list.add_track("Hozier", "Son of nyx")
music_list.track_list() # => ["Hozier: Son of nyx"]






_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
