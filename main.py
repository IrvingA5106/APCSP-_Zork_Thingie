from __future__ import print_function
from player import Player

def startGame():
    print('Welcome to the mysterious mansion.')
    # raw_input('Press enter to start the game. ')
    player = Player()
    
    basement(player)
    print('Congratulations! You escaped the house.')

startGame()

def library(player):
    in_library = True
    
    print('You entered the library!')
    print("Empty bookshelves line the walls. On the side of the room, there is a weathered desk with a worn leather chair and a small golden statue on it.")
    print("There is a door to the west.")
    
    player.add_room('library')
    
    while in_library:
        userAction = raw_input('What would you like to do? ')
        
        if userAction == 'open west door':
            print("The door is hard to open, but you get it eventually.")
            livingRoom()
        elif (userAction == 'take statue' or userAction == "pick up statue") and not player.has('statue'):
            print("\nYou cautiously pick up the statue. Nothing happens. Dang, that was anticlimactic.")
            print("...")
            print("...")
            print("Huh, what's that sound?\n")
            print("\nThe ceiling of the library disappears, revealing a huge wall of water. The water crashes down, filling the room. You take a deep breath before the water goes over your head...")
            player.pick_up('statue')
            attic()
        elif userAction == 'sit at desk':
            print('You sit at the desk. Nothing happens.')
        elif userAction in ['quit', 'q']:
            print('you have left the game')
            exitRoom = True
        elif userAction == "scream":
            print("Aaaaaahhhhhh")
        else:
            print("I don't know how to do that. Try again!")

def foyer(player):
    in_foyer = True
    dresser_items = ['key_foyer', 'flashlight']
    player.add_room('foyer')
    
    print('You have entered the foyer')
    print('There are two doors in this room.  One to the left and one to the right.')
    print('There is also a dresser with one drawer in the room.')
    
    while in_foyer == True:
        userAction = raw_input('What would you like to do? ')
        
        if userAction == 'open left door' and player.has('key_foyer'):
            print('The door slowly creaks open.')
            in_foyer = False
            bedroom(player)
        elif userAction == 'open right door' and player.has('flashlight'):
            print('You open the door and can now see inside with the flashlight.')
            in_foyer = False
            living_room(player)
        elif userAction == 'open dresser':
            print('You picked up', dresser_items)
            player.pick_up(dresser_items)
            dresser_items = []
        elif userAction == 'open left door' and not player.has('key_foyer'):
            print('The door will not open.')
        elif userAction == "scream":
            print("Aaaaaahhhhhh")
        elif userAction == 'open right door' and not player.has('flashlight'):
            print('You open the door, but it is so dark inside that you cannot see. You do not enter and you close the door.')
        else:
            print ("I don't understand '{}'".format(userAction))

def attic(player):
    wardrobe_open = False
    attic_items = ['knife', 'skull']
    
    in_attic = True
    if 'attic' in player.visited_rooms:
        print("This room looks familiar.")
    else:
        # Good idea, Idk how to work something like this into player.add_room
        print("You open your eyes slowly. What happened?")
        player.visited_rooms.append('attic')
    
    print("You are in a dusty attic. The walls and ceiling are covered in cobwebs. A soaked wardrobe is on the side of the wall.")
    print("There is a flight of stairs leading down to a doorway.")
    
    while in_attic:
        userAction = raw_input("What do you want to do? ")
        
        if userAction == 'open door':
            print('You walk down the stairs and open the door.')
            in_attic = False
            kitchen(player)
        elif userAction in ['quit', 'q']:
            print('you have left the game')
        elif userAction == 'open wardrobe':
            print('The wardrobe is filled with waterlogged coats. All of them look ruined. At the bottom of the wardrobe is a box carved out of stone.')
            wardrobe_open = True
        elif userAction == 'open box' and wardrobe_open == True:
            print("You open the box. Inside, there is a silver knife and a dusty skull. You take both.")
            player.pick_up(attic_items)
        elif userAction == 'scream':
            print("Aaaaaaahhh")
        else:
            print("I can't do that! Try again!")
def bedroom(player):
    in_bedroom = True
    player.add_room('bedroom')
    
    print("You have entered the bedroom. There is a comfy looking bed in the center of the room, a chest at the foot of the bed, the door you just entered through, and large curtains covering a window on the wall.")
    
    while in_bedroom:
        userAction = raw_input('What would you like to do? ')
        
        if userAction == 'open chest' and player.has('key1'):
            print("You opened up the chest. Inside, there is a book, some matches, a red pocketknife, and a old jacket.")
            chest_items = ['book', 'matches', 'jacket', 'pocketknife']
            player.pick_up(chest_items)
        elif userAction in ['quit', 'q']:
            print('you have left the game')
            exitRoom = True
        elif userAction == 'open chest' and not player.has('key1'):
            print("The chest is locked.")
        elif userAction == 'read book' and player.has('book'):
            print("The continent of Codalia, located on the continent of Normal West, is ruled by the gracious, intelligent and beautiful Queen Schermann. Its subjects are mostly teenage students, and occasionally other nobles, like Duke Scornovacco the Wise and Duke Beaty the Bearded")
            print("You get bored and put the book down.")
        elif userAction == 'sleep on bed' or userAction == 'sit on bed':
            print("You lay down on the bed and close your eyes. When you open them again, the chair has moved to the other side of the room. Who was here?")
        elif userAction == 'wear jacket':
            print("You poke your arms through the sleeves of the jacket. It is musty, but surprisingly comfortable. You find a golden coin in the pocket.")
            player.pick_up('coin')
        elif userAction == 'open door 3':
            print("You open the door and move on.")
            living_room()
        else:
            print("I can't do that! Try again.")
            
def basement(player):
    print ("You're in a cold, pitch black room.")
    in_basement = True
    
    while in_basement:
        userAction = raw_input("> ")
        if userAction == "move forward" or userAction == "walk forward":
            if player.direction.direction == 180:
                print ("You trip over a box and fall to the floor.")
            else:
                print ("You walk forward until you run into a damp, slimy wall.")
        elif userAction == "turn left":
            print ("Turned left.")
            player.direction.turn_left()
        elif userAction == "turn right":
            print ("Turned right.")
            player.direction.turn_right()
        elif userAction == "open box":
            print ("You found a flashlight in the box!")
            print ("+1 flashlight")
            player.pick_up("flashlight")
        elif userAction == "look around":
            if player.has("flashlight"):
                print ("The room is small and damp with no windows or doors. There is a trapdoor in the ceiling.")
            else:
                print ("I can't see anything!")
        elif userAction in ["open trapdoor", "enter trapdoor"]:
            if not player.has("flashlight"):
                print ("I don't understand '{}'".format(userAction))
            else:
                print ("Exiting trapdoor")
                in_basement = False
        elif userAction in ['quit', 'q']:
            print('you have left the game')
            in_basement = False
        elif userAction == "scream":
            print("Aaaaaahhhhhh")
        else:
            print ("I don't understand '{}'".format(userAction))
    
    living_room(player)

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
        elif userAction == 'look around':
            print('You are in the Living Room')
            print('There is a door to the north.')
            print('There is a dresser with a drawer partly open against the wall.')
            print('There is a rug in the center of the room.')
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
            print("I don't know how to do that!")
