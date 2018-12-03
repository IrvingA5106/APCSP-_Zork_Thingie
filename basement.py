# This is a class that abstracts a direction that a player
# can face.
class Direction:
    def __init__():
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
    def __init__():
        self.items = [] # strings please

    def has(self, item):
        return item in self.items

    def pick_up(self, item):
        self.items.add(item)

def basement(player):
    print "You're in a cold, pitch black room."
    direction = Direction()


    while True:
        cmd = raw_input("> ")
        if cmd == "move forward" or cmd == "walk forward":
            if direction == 180:
                print "You trip over a box and fall to the floor."
            else:
                print "You walk forward until you run into a damp, slimy wall."
        elif cmd == "turn left":
            print "Turned left."
            direction.turn_left()
        elif cmd == "turn right":
            print "Turned right."
            direction.turn_right()
        elif cmd == "open box":
            print "You found a flashlight in the box!"
        elif cmd == "pick up flashlight":
            print "+1 flashlight"
            player.pick_up("flashlight")
        elif cmd == "look around":
            if player.has("flashlight"):
                print "The room is small and damp with no windows or doors. There is a trapdoor in the ceiling."
            else:
                print "I can't see anything!"
        elif cmd == "open trapdoor":
            if not player.has("flashlight"):
                print "I don't understand '{}'".format(cmd)
            else:
                print "Exiting trapdoor"
                # go to a new room
        else:
            print "I don't understand '{}'".format(cmd)
