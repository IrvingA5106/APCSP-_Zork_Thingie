from __future__ import print_function

from basement import *
from player import Player
from foyer import foyer

def living_room(player):
    dresser_items = ['key2', 'key3','machete']
    exitRoom = False
    rug_up = False
    trapdoor_shut = True
    
    print('You have entered the Living Room')
    print('There is a door to the north.')
    print('There is a dresser with a drawer partly open against the wall.')
    print('There is a rug in the center of the room.')
    
    player.add_room('living_room')
    
    while exitRoom == False:
        userAction = raw_input('What would you like to do? ')
        
        if userAction == 'open north door' and not player.has('key3'):
            print('This door is locked. Is there a key that you can use to open the door?')
        elif userAction == 'open north door' and player.has('key3'):
            print('you have opened the north door and entered the foyer')
            exitRoom = True
            foyer(player)
        elif userAction in ['move the rug', 'roll up the rug', 'move rug']:
            print('you have moved the rug')
            print('There is a trapdoor here that was covered by the rug')
            rug_up = True
        elif userAction in ['open dresser', 'open dresser drawer', 'pull the dresser drawer open', 'pull open drawer', 'pull open dresser drawer'] :
            print('You have opened the dresser drawer.')
            print('there are two keys and a machete in the drawer.')
        elif userAction in ['take dresser items', 'grab items', 'take items', 'grab dresser items']:
            print('You have grabbed the keys and the Machete.')
            player.pick_up(dresser_items)
        elif userAction in ['open trapdoor', ' enter trapdoor'] and (rug_up and trapdoor_shut):
            print('The trapdoor is tied closed by a thick string.')
        elif userAction in ['cut the string' ' cut string with the machete'] and player.has('machete'):
            print('You have cut the string and opened the trapdor.')
            trapdoor_shut = False
        elif userAction in ['go into the trapdoor', ' enter trapdoor', 'exit trapdoor'] and (rug_up and not trapdoor_shut):
            print('You have entered the west end of the basement')
            exitRoom = True
            basement(player)
        elif userAction == 'scream':
            print("Aaaaaahhhhh")
        elif userAction in ['quit', 'q']:
            print('you have left the game')
            exitRoom = True
        else:
            print("I don't know what " + userAction + " means.")

if __name__ == "__main__":
    living_room(Player())
