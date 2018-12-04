def library(player):
    global enteredRooms
    global playerItems
    global openedDoors
    
    libraryItems = ['statue']
    print('You entered the library!')
    print("Empty bookshelves line the walls. On the side of the room, there is a weathered desk with a worn leather chair and a small golden statue on it.")
    print("There is a door to the west (door 4)")
    
    if 'library' in player.visited_rooms:
        print('This room looks vaguely familiar')
    else:
        enteredRooms += ['library']
    
    print('You entered the library!')
    print("Empty bookshelves line the walls. On the side of the room, there is a weathered desk with a worn leather chair and a small golden statue on it.")
    print("There is a door to the west (door 4)")
    userAction = raw_input('What would you like to do? ')
    
    if userAction == 'open door 4':
        print("The door is hard to open, but you get it eventually.")
        livingRoom()
    elif userAction == 'take statue' and 'statue' not in player.items:
        print("\nYou cautiously pick up the statue. Nothing happens. Dang, that was anticlimactic.")
        print("...")
        print("...")
        print("Huh, what's that sound?\n")
        print("\nThe ceiling of the library disappears, revealing a huge wall of water. The water crashes down, filling the room. You take a deep breath before the water goes over your head...")
        player.items.append('statue')
        libraryItems.remove('statue')
        openedDoors.append('door 4')
        attic()
    elif userAction == 'sit at desk':
        print('You sit at the desk. Nothing happens.')
        userAction == input('What would you like to do next?')
    else:
        print("I don't know how to do that. Try again!")
        userAction = input('What would you like to do next?')
