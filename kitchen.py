from __future__ import print_function
from player import Player
from foyer import foyer

def kitchen(player):
    exitRoom = False
    table_items = ["candle", "key_kitchen", "rope"]
    
    print("you have entered the Kitchen.")
    print("There is a table with some items lying there.")
    print("there is a door to the south and a door to the east.")
    
    player.add_room('kitchen')
    
    while exitRoom == False:
        userAction = raw_input('What would you like to do? ')
        
        if userAction == 'open east door' and not player.has('key_kitchen'):
            print("The door is locked. Do you have a key that you could use?")
        elif userAction == 'open east door' and player.has('key_kitchen'):
            exitRoom = True
            foyer(player)
        elif userAction == 'open south door':
            print("You have gone to the backyard.")
            exitRoom = True
        elif userAction == 'pick up items':
            print('you took', table_items)
            player.pick_up(table_items)
        elif userAction == "scream":
            print("Aaaaaahhhhhh")
        else:
            print('Invalid Action')

if __name__ == "__main__":
    kitchen(Player())
