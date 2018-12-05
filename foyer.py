from player import Player

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
            bedroom()
        elif userAction == 'open right door' and player.has('flashlight'):
            print('You open the door and can now see inside with the flashlight.')
            in_foyer = False
            living_room()
        elif userAction == 'open dresser':
            print('You picked up', dresser_items)
            player.pick_up(dresser_items)
            dresser_items = []
        elif userAction == 'open left door' and not player.has('key_foyer'):
            print('The door will not open.')
        elif userAction == 'open right door' and not player.has('flashlight'):
            print('You open the door, but it is so dark inside that you cannot see. You do not enter and you close the door.')
        else:
            print "I don't understand '{}'".format(userAction)

# If you run this module as main
foyer(Player())
