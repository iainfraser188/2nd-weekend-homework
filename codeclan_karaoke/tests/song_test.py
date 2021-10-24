import unittest
# from classes.guest import Guest
# from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("another one bytes the dust")


    def test_check_song_name(self):
        self.assertEqual("another one bytes the dust", self.song_1.song_name)    
  