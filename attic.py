from player import Player

def attic():
    global enteredRooms
    global playerItems
    global openedDoors
    
    wardrobeOpen = False
    atticItems = ['cobwebs', 'knife', 'skull']
    
    if 'attic' in enteredRooms:
        print("This room looks familiar.")
    else:
        print("You open your eyes slowly. What happened?")
        enteredRooms.append('attic')
        
    print("You are in a dusty attic. The walls and ceiling are covered in cobwebs. A soaked wardrobe is on the side of the wall.")
    print("There is a flight of stairs leading down to a doorway (door 5).")
    userAction == raw_input("What do you want to do? ")
    
    if userAction == 'open door 5':
        print('You walk down the stairs and open the door.')
        #next room function yay!
    elif userAction == 'open wardrobe':
        print('The wardrobe is filled with waterlogged coats. All of them look ruined. At the bottom of the wardrobe is a box carved out of stone.')
        wardrobeOpen == True
        userAction = raw_input("What would you like to do now? ")
    elif userAction == 'open box' and 'wardrobeOpen' == True:
        print("You open the box. Inside, there is a silver knife and a dusty skull.You take both.")
        playerItems.append("knife")
        playerItems.append("skull")
        atticItems.remove("knife")
        atticItems.remove("skull")
        userAction = raw_input("What would you like to do now? ")
    else:
        print("I can't do that! Try again!")
        userAction = raw_input("What would you like to do now? ")
        

    