from __future__ import print_function

playerItems = []
enteredRooms = []
openedDoors = []         
      
def living_room():
    global enteredRooms
    global playerItems
    exitRoom = False
    print('You have entered the Living Room')
    print('there is a door to the north.')
    print('There is a dresser with a drawer partly open against the wall.')
    print('There is a rug in the center of the room.') 
    if 'living_room' in enteredRooms:
        print('This room looks vaguely familiar.')
    if 'living_room' not in enteredRooms:
        enteredRooms =+['room3']
    dresser_items = ['key2', 'key3','machete']
    userAction = raw_input('What would you like to do? ')
    while exitRoom == False:
        if userAction == 'open North door':
            print('This door is locked. Is there a key that you can use to open the door?')
            exitRoom = True
        elif userAction == 'open North door with key3':
            print('you have opened the north door and entered the foyer')
            exitRoom = True
        elif userAction == 'move the rug':
             print('you have moved the rug')
             print('There is a trapdoor that was covered by the rug')
        elif userAction == 'open dresser drawer':
                print('You have opened the dresser drawer.')
                print('there is a key2, key3, and a machete in the drawer.')
        elif userAction == 'take dresser items':
            print('You have grabbed the key2, key3, and the Machete.')
        elif userAction ==         
            
    

        
            
        

