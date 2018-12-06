from player import Player

def attic(player):
    wardrobe_open = False
    attic_items = ['cobwebs', 'knife', 'skull']
    
    in_attic = True
    if 'attic' in enteredRooms:
        print("This room looks familiar.")
    else:
        # Good idea, Idk how to work something like this into player.add_room
        print("You open your eyes slowly. What happened?")
        enteredRooms.append('attic')
    
    print("You are in a dusty attic. The walls and ceiling are covered in cobwebs. A soaked wardrobe is on the side of the wall.")
    print("There is a flight of stairs leading down to a doorway (door 5).")
    
    while in_attic:
        userAction == raw_input("What do you want to do? ")
        
        if userAction == 'open door 5':
            print('You walk down the stairs and open the door.')
            in_attic = False
            #next room function yay!
        elif userAction == 'open wardrobe':
            print('The wardrobe is filled with waterlogged coats. All of them look ruined. At the bottom of the wardrobe is a box carved out of stone.')
            wardrobeOpen == True
        elif userAction == 'open box' and 'wardrobeOpen' == True:
            print("You open the box. Inside, there is a silver knife and a dusty skull.You take both.")
            player.pick_up(attic_items)
        else:
            print("I can't do that! Try again!")

# For testing, run this file as main
attic(Player())
