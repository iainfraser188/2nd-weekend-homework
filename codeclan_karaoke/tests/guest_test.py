import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
   
    def setUp(self):
        self.guest_1 = Guest("iain", 50, "another one bytes the dust")
        self.room_1 = Room(1,2,5,10)
        self.song_1 = Song("another one bytes the dust")

    def test_guest_name(self):
        self.assertEqual("iain", self.guest_1.name)   

    def test_guest_has_money(self):
        self.assertEqual(50,self.guest_1.money) 

    def test_guest_has_favorite_song(self):
        self.assertEqual("another one bytes the dust",self.guest_1.fav_song)      

    def test_pay_entry_fee(self):
        self.guest_1.pay_entry_fee()
        self.assertEqual(45,self.guest_1.money)  

    






        