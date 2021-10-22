import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
   
    def setUp(self):
        self.guest_1 = Guest("iain")

    def test_guest_name(self):
        self.assertEqual("iain", self.guest_1.name)    



        