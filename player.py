import types

# This is a class that abstracts a direction that a player
# can face.
class Direction:
    def __init__(self):
        self.direction = 0

    def turn_left(self):
        if self.direction == 0:
            self.direction = 270
        else:
            self.direction -= 90

    def turn_right(self):
        if self.direction == 270:
            self.direction = 0
        else:
            self.direction += 90

class Player:
    def __init__(self):
        self.items = [] # strings please
        self.visited_rooms = [] # strings please
        self.direction = Direction()

    def has(self, item):
        return item in self.items

    def pick_up(self, item):
        if isinstance(item, types.ListType):
            self.items.extend(item)
        else:
            self.items.append(item)
    
    def add_room(self, room):
        if room in self.visited_rooms:
            print('This room looks vaguely familiar.')
        else:
            self.visited_rooms.append(room)
