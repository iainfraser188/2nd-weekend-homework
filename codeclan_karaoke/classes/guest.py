from classes.room import Room
class Guest:
    def __init__(self,name,money,fav_song):
        self.name = name
        self.money = money
        self.fav_song = fav_song
        self.room_1 = Room(1,2,5,100)
   

    def pay_entry_fee(self):
        self.money -= self.room_1.entry_fee

    
                

