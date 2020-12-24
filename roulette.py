### LIST OF TASKS ###
# input asking player names
# their inventory
# List of items
# turn
# choose item
# confirm
# Roulette process
# results
# who won

import random

items = ["Pencil", "Eraser", "Diamond", "Gold", "Leather", "Keyboard"]

player1inv = ["Car", "House", "Mobile", "PC"]

player2inv = ["$100,000", "House", ""]


def instructions():
    print("HI, Welcome to Roulette!!")
    print("Here you gotta bet some items you have and the other player will bet too")
    print("Then there's a list of items that can come out as an outcome of the roulette. Before spinning the wheel, you gotta bet that which item won't come out. If that item comes out, you lose the bet and you gotta give your item to your opponent")
    print("Have fun and don't lose!")

def printItems():
    print("Here are the items present in the Roulette")
    for i in items:
        print(i)

def printPlayer1inv():
    print("Player 1, These are the items you have")
    for i in player1inv:
        print(i)

def printPlayer2inv():
    print("Player 2 These are the items you have")
    for i in player2inv:
        print(i)

def enterName():
    Player1 = str(input("Player 1 enter your name: "))
    Player2 = str(input("Player 2 enter your name: "))

def enterAnyKey(doQuit):
    if doQuit == True:
        skipOrQuit = input("Press any key to continue or quit to quit: ")
        if skipOrQuit.lower() == "quit":
            return
        else:
            pass

    else:
        skipOrQuit = input("Press any key to continue: ")
        if skipOrQuit.lower() == "blhasljbf":
            return
        else:
            pass


instructions()
enterAnyKey(False)
enterName()
printPlayer1inv()
printPlayer2inv()
enterAnyKey(True)



