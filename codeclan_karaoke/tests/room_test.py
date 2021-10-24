import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(1,2,5,100)
        self.room_2 = Room(2,5,10,80)
        self.guest_1 = Guest("iain",50,"another one bytes the dust")
        self.guest_2 = Guest("steve",5,"wonderfirewall")
        self.guest_3 = Guest("peter",2,"paranoid android")
        self.song_1 = Song("another one bytes the dust")

    
    def test_check_room(self):
        self.assertEqual(1,self.room_1.room_number)  

    def test_room_has_enrty_fee(self):
        self.assertEqual(5,self.room_1.entry_fee)      

    def test_check_guest_into_room(self):
        self.room_1.check_guest_into_room(self.guest_1)  
        self.assertEqual("iain",self.room_1.guests_in_room[0].name) 
    
    def test_check_guests_out_of_room(self):
        self.room_1.check_guest_into_room(self.guest_1)  
        self.room_1.check_guest_into_room(self.guest_2)  
        self.room_1.check_guest_out_of_room(self.guest_2)
        self.assertEqual(1,len(self.room_1.guests_in_room))

    def test_add_song_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_1)
        self.assertEqual("another one bytes the dust",self.room_1.playlist[0].song_name)  

    def test_over_crowded(self):
        self.room_1.check_guest_into_room(self.guest_1)  
        self.room_1.check_guest_into_room(self.guest_2) 
        self.room_1.check_guest_into_room(self.guest_3)
        self.assertEqual(2,len(self.room_1.guests_in_room))
        # self.assertEqual(1,len(self.room_2.guests_in_room))

    def test_take_entry_fee(self):
        self.room_1.take_entry_fee()
        self.assertEqual(105,self.room_1.till)

    def test_fav_song(self):
        self.room_1.add_song_to_playlist(self.song_1)
        self.room_1.check_guest_into_room(self.guest_1)

        self.assertEqual("whoo",self.room_1.fav_song(self.guest_1))



            


