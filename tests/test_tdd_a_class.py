from lib.tdd_a_class import *

"""
when a new object is created from the class Music_list
A new empty list is created.
"""

def test__initialising_music_list_returns_blank_list():
    music_list= Music_list()    
    assert music_list.track_list() == []

"""
given a track name and artist name these are added to the list as a string.
in a string formatted "artist name: track name"
""" 

def test_adding_tracks_adds_to_list():
    music_list = Music_list()
    music_list.add_track("Hozier", "Son of Nyx")
    music_list.add_track("Beyonce", "Love on Top")    
    assert music_list.track_list() == ["Hozier: Son of Nyx", "Beyonce: Love on Top"]


