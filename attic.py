from kitchen import kitchen
from player import Player

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
        elif userAction == 'open wardrobe':
            print('The wardrobe is filled with waterlogged coats. All of them look ruined. At the bottom of the wardrobe is a box carved out of stone.')
            wardrobe_open = True
        elif userAction == 'open box' and wardrobe_open == True:
            print("You open the box. Inside, there is a silver knife and a dusty skull. You take both.")
            player.pick_up(attic_items)
        else:
            print("I can't do that! Try again!")

if __name__ == "__main__":
    attic(Player())
