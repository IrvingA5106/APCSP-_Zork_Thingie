from __future__ import print_function

from basement import basement
from player import Player

playerItems = []
enteredRooms = []
openedDoors = []

def startGame():
    print('Welcome to the mysterious mansion')
    # raw_input('Press enter to start the game. ')
    player = Player()
    
    basement(player)

startGame()
