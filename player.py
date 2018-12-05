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
    
    """Determine if the user has an item in their inventory"""
    def has(self, item):
        return item in self.items

    """Add an Item to a player's inventory"""
    def pick_up(self, item):
        if isinstance(item, types.ListType):
            self.items.extend(item)
        else:
            self.items.append(item)
    
    """Add a room to the list of rooms a player has visted.
    If they've already been there, print a message"""
    def add_room(self, room):
        if room in self.visited_rooms:
            print('This room looks vaguely familiar.')
        else:
            self.visited_rooms.append(room)
