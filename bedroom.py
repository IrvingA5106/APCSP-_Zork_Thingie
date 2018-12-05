def bedroom(player):
    global playerItems
    global enteredRooms
    global openedDoors
    
    if 'bedroom' in enteredRooms:
        print('This room looks vaguely familiar')
    if 'bedroom' not in enteredRooms:
        enteredRooms += ['bedroom']
    print("You have entered the bedroom. There is a comfy looking bed in the center of the room, a chest at the foot of the bed, the door you just entered through, and large curtains covering a window on the wall.")
    userAction = raw_input('What would you like to do? ')
    
    if userAction == 'open chest' and 'key1' in playerItems:
        print("You opened up the chest. Inside, there is a book, some matches, a red pocketknife, and a old jacket.")
        playerItems += 'book'
        playerItems += 'matches'
        playerItems += 'jacket'
        playerItems += 'pocketknife'
    elif userAction == 'open chest' and 'key1' not in playerItems:
        print("The chest is locked.")
        userAction = raw_input("What would you like to do next? ")
    elif userAction == 'read book' and 'book' in playerItems:
        print("The continent of Codalia, located on the continent of Normal West, is ruled by the gracious, intelligent and beautiful Queen Schermann. Its subjects are mostly teenage students, and occasionally other nobles, like Duke Scornovacco the Wise and Duke Beaty the Bearded")
        print("You get bored and put the book down.")
        userAction = raw_input("What would you like to do next? ")
    elif userAction == 'sleep on bed' or userAction == 'sit on bed':
        print("You lay down on the bed and close your eyes. When you open them again, the chair has moved to the other side of the room. Who was here?")
        userAction = raw_input("What would you like to do next? ")
    elif userAction == 'wear jacket':
            print("You poke your arms through the sleeves of the jacket. It is musty, but surprisingly comfortable. You find a golden coin in the pocket.")
            playerItems += 'coin'
    elif userAction == 'open door 3':
        print("You open the door and move on.")
        living_room()
    else:
        print("I can't do that! Try again.")
        userAction == raw_input("What would you like to do next? ")

# If you run this module as main
bedroom(Player())
