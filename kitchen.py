from __future__ import print_function

playerItems = []
enteredRooms = []
openedDoors = []

def kitchen():
    global enteredRooms
    global playerItems
    exitRoom = False    
    print("you have entered the Kitchen.")
    print("There is a table with some items lying there.")
    print("there is a door to the South and a door to the East.")
    if kitchen in enteredRooms:
        print('This room looks vaguely familiar')
    if kitchen not in enteredRooms:
        enteredRooms += ['room2']
    table_items= ["candle", "key1", "rope"]
    userAction = raw_input('What would you like to do? ')
    while exitRoom == False:
        if userAction == 'open East door':
            print("The door is locked. Do you have a key that you could use?")
            exitRoom = True
        elif userAction == 'open South door':
            print("you have gone to the backyard")
            exitRoom = True
        elif userAction == 'grab the items from the table':
            print('you took', table_items)
        else:
            print('Invalid Action')
            userAction = raw_input('What would you like to do? ')
            