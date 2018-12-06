from __future__ import print_function
from player import Player
from foyer import foyer

def kitchen(player):
    
    player.add_room('kitchen')
    exitRoom = False    
    print("you have entered the Kitchen.")
    print("There is a table with some items lying there.")
    print("there is a door to the South and a door to the East.")
    
    table_items= ["candle", "key_kitchen", "rope"]
    while exitRoom == False:
        userAction = raw_input('What would you like to do? ')
        if userAction == 'open East door' and not player.has('key_kitchen'):
            print("The door is locked. Do you have a key that you could use?")
        elif userAction == 'open South door':
            print("you have gone to the backyard")
            exitRoom = True
        elif userAction == 'grab the items from the table':
            print('you took', table_items)
            player.pick_up(table_items)
            
        elif userAction == 'open East door' and player.has('key_kitchen'):
            print('You have entered the foyer')
            exitRoom = True
            foyer(player)
        else:
            print('Invalid Action')

kitchen(Player())
