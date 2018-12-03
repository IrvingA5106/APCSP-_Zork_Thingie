from __future__ import print_function
import random

playerItems = []
enteredRooms = []
openedDoors = []

def startGame():
    print('Welcome to the mysterious mansion')
    raw_input('Press enter to start the game. ')
    room1()

def room1():
    global playerItems
    global enteredRooms
    global openedDoors
    exitRoom = False
    dresserItems = ['key1', 'flashlight']
    print('You have entered the foyer')
    print('There are two doors in this room.  One to the left(door 1) and one to the right(door2).')
    print('There is also a dresser with one drawer in the room.')
    userAction = raw_input('What would you like to do? ')
    while exitRoom == False:
        if userAction == 'open door 1' and 'key1' in playerItems:
            print('The door slowly creaks open')
            openedDoors += ['door1']
            exitRoom = True
        elif userAction == 'open door 2' and 'flashlight' in playerItems:
            print('You open the door and can now see inside with the flashlight.')
            openedDoors += ['door2']
            exitRoom = True
        elif userAction == 'open dresser':
            print('You picked up', dresserItems)
            playerItems += dresserItems
            dresserItems = []
            userAction = raw_input('What would you like to do now? ')
        elif userAction == 'open door 1' and 'key1' not in playerItems:
            print('The door will not open')
            userAction = raw_input('What would you like to do now? ')
        elif userAction == 'open door 2' and 'flashlight' not in playerItems:
            print('You open the door, but it is so dark inside that you cannot see.  You do not enter and you close the door.')
            userAction = raw_input('What would you like to do now? ')
        else:
            userAction = raw_input('Not a valid action.  Try Again! ')
    if 'door1' in openedDoors:
        bedroom()
    else:
        room3()
        
def bedroom():
    global playerItems
    global enteredRooms
    global openedDoors 
    if 'bedroom' in enteredRooms:
        print('This room looks vaguely familiar')
    if 'bedroom' not in enteredRooms:
        enteredRooms += ['bedroom']
    print("You have entered the bedroom. There is a comfy looking bed in the center of the room, a chest at the foot of the bed, the door you just entered through, and large curtains covering a window on the wall.")
    if userAction == 'open chest' and 'key1' in playerItems:
        print("You opened up the chest. Inside, there is a book, some matches, a red pocketknife, and a old jacket.")
        playerItems += 'book'
        playerItems += 'matches'
        playerItems += 'jacket'
        playerItems += 'pocketknife'
    elif userAction == 'open chest' and 'key1' not in playerItems:
        print("The chest is locked.")
        userAction == raw_input("What would you like to do next?")
    elif userAction == 'read book' and 'book' in playerItems:
        print("The continent of Codalia, located on the continent of Normal West, is ruled by the gracious, intelligent and beautiful Queen Schermann. Its subjects are mostly teenage students, and occasionally other nobles, like Duke Scornovacco the Wise and Duke Beaty the Bearded") 
        print("You get bored and put the book down.")
        userAction = raw_input("What would you like to do next?")
    elif userAction == 'sleep on bed':
        print("You lay down on the bed and close your eyes. When you open them again, the chair has moved to the other side of the room. Who was here?")
    elif userAction == 'wear jacket':
            print("You poke your arms through the sleeves of the jacket. It is musty, but surprisingly comfortable. You find a golden coin in the pocket.")
            playerItems += 'coin'
    elif userAction == 'open door 3':
        print("You open the door and move on.")
        room1()
        
def room3():
    global enteredRooms
    print('You entered Room 3')
    if 'room3' in enteredRooms:
        print('This room looks vaguely familiar')
    if 'room3' not in enteredRooms:
            enteredRooms += ['room3']
