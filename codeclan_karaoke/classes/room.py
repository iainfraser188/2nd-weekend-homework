class Room:
    def __init__(self,room_number,room_capacity,entry_fee,till):
        self.room_number = room_number
        self.guests_in_room = []
        self.playlist = []
        self.room_capacity = room_capacity
        self.entry_fee = entry_fee
        self.till = till



    def check_guest_into_room(self, name):
       if len(self.guests_in_room) < self.room_capacity :
          self.guests_in_room.append(name)
          
       else:
           print("sorry room full")
        #    self.room_2.check_guest_into_room(name) 
       
    def check_guest_out_of_room(self,name):
        for guest in self.guests_in_room:
            if guest == name :
                self.guests_in_room.remove(name)   

    def add_song_to_playlist(self,song):
        self.playlist.append(song) 

    def take_entry_fee(self) :
        self.till += self.entry_fee  

    def fav_song(self, guest):
        for song in self.playlist:
            if song.song_name == guest.fav_song:
                return "whoo"

    # def overcrowded(self):
    #     if len(self.guests_in_room) == 2:
    #         return True

            

          
            
        
        
