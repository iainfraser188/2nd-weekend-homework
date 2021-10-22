class Room:
    def __init__(self,room_number):
        self.room_number = room_number
        self.guests_in_room = []



    def check_guest_into_room(self, name):
        self.guests_in_room.append(name)

    def check_guest_out_of_room(self,name):
        for guest in self.guests_in_room:
            if guest == name :
                self.guests_in_room.remove(name)   

          
            
        
        
