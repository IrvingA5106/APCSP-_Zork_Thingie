import types

"""
This is a class that abstracts a direction that a player
can face. Direction.direction is public, and in degrees,
so it's possible to compare against it for game logic
"""
# TODO: Add some comparison methods and a direction enum
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

"""
This class is responsible for holding on to global state things: namely
the items that a player has picked up, but also the rooms they've visited,
and dealing with directions if the logic for a room requires that (see basement)
"""
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
        # Basically handle a list passed in differently than
        # a single item
        if isinstance(item, types.ListType):
            self.items.extend(item)
        else:
            self.items.append(item)
    
    """
    Add a room to the list of rooms a player has visted.
    If they've already been there, print a message
    """
    def add_room(self, room):
        if room in self.visited_rooms:
            print('This room looks vaguely familiar.')
        else:
            self.visited_rooms.append(room)
