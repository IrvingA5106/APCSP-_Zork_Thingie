from __future__ import print_function
import random

playerItems = []
enteredRooms = []
openedDoors = []

def startGame():
    print('Welcome to the mysterious mansion')
    raw_input('Press enter to start the game. ')
    room1()
