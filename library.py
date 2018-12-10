from player import Player
from living room import living room 

def library(player):
    in_library = True
    
    print('You entered the library!')
    print("Empty bookshelves line the walls. On the side of the room, there is a weathered desk with a worn leather chair and a small golden statue on it.")
    print("There is a door to the west.")
    
    player.add_room('library')
    
    while in_library:
        user_action = raw_input('What would you like to do? ')
        
        if user_action == 'open west door':
            print("The door is hard to open, but you get it eventually.")
            livingRoom()
        elif (user_action == 'take statue' or user_action == "pick up statue") and not player.has('statue'):
            print("\nYou cautiously pick up the statue. Nothing happens. Dang, that was anticlimactic.")
            print("...")
            print("...")
            print("Huh, what's that sound?\n")
            print("\nThe ceiling of the library disappears, revealing a huge wall of water. The water crashes down, filling the room. You take a deep breath before the water goes over your head...")
            player.pick_up('statue')
            attic()
        elif user_action == 'sit at desk':
            print('You sit at the desk. Nothing happens.')
        elif userAction in ['quit', 'q']:
            print('you have left the game')
            exitRoom = True
        elif cmd == "scream":
            print("Aaaaaahhhhhh")
        else:
            print("I don't know how to do that. Try again!")

if __name__ == "__main__":
    library(Player())
