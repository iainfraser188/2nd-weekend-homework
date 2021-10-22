import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(1)
        self.guest_1 = Guest("iain")
        self.guest_2 = Guest("steve")

    
    def test_check_room(self):
        self.assertEqual(1,self.room_1.room_number)    

    def test_check_guest_into_room(self):
        self.room_1.check_guest_into_room(self.guest_1)  
        self.assertEqual("iain",self.room_1.guests_in_room[0].name) 
    
    def test_check_guests_out_of_room(self):
        self.room_1.check_guest_into_room(self.guest_1)  
        self.room_1.check_guest_into_room(self.guest_2)  
        self.room_1.check_guest_out_of_room(self.guest_2)
        self.assertEqual(1,len(self.room_1.guests_in_room))

        


