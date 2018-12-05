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

# If you run this module as main
bedroom(Player())
