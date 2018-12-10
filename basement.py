from player import Player
from living_room import living_room

def basement(player):
    print "You're in a cold, pitch black room."
    in_basement = True
    
    while in_basement:
        cmd = raw_input("> ")
        if cmd == "move forward" or cmd == "walk forward":
            if player.direction.direction == 180:
                print "You trip over a box and fall to the floor."
            else:
                print "You walk forward until you run into a damp, slimy wall."
        elif cmd == "turn left":
            print "Turned left."
            player.direction.turn_left()
        elif cmd == "turn right":
            print "Turned right."
            player.direction.turn_right()
        elif cmd == "open box":
            print "You found a flashlight in the box!"
        elif cmd == "pick up flashlight" or cmd == "take flashlight":
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
                in_basement = False
        elif cmd == "scream":
            print("Aaaaaahhhhhh")
        else:
            print "I don't understand '{}'".format(cmd)
    
    living_room(player)

if __name__ == "__main__":
    basement(Player())
