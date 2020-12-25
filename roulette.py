### LIST OF TASKS ###
# input asking player names
# their inventory
# List of items
# turn
# choose item
# Roulette process
# results
# who won

import random

items = ["Pencil", "Eraser", "Diamond", "Gold", "Leather", "Keyboard"]

player1inv = ["Car", "House", "Mobile", "PC"]

player2inv = ["$100,000", "House", ""]

global Player1
global Player2
global player1chosenItem
global player2chosenItem
global player1turnItem
global player2turnItem
global player
global gameover

gameover = False

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
    print(Player1 + ", These are the items you have")
    for i in player1inv:
        print(i)

def printPlayer2inv():
    print(Player2 + ", These are the items you have")
    for i in player2inv:
        print(i)

def enterName():
    global Player1
    global Player2
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

def player1bet():
    global player1chosenItem
    player1chosenItem = ""
    itemChosen = input(Player1 + ", Choose an item you'll give to " + Player2 + " if you lose: ")
    while player1chosenItem == "":
        if itemChosen in player1inv:
            player1chosenItem = itemChosen
        else:
            itemChosen = input("You don't have that item choose another: ")

def player2bet():
    global player2chosenItem
    player2chosenItem = ""
    itemChosen = input(Player2 + ", Choose an item you'll give to " + Player1 + " if you lose: ")

    while player2chosenItem == "":
        if itemChosen in player2inv:
            player2chosenItem = itemChosen
        else:
            itemChosen = input("You don't have that item choose another: ")

def player1turn():
    global player
    global player1turnItem
    player = 1
    player1turnItem = ""
    itemChosen = str(input(Player1 + ", bet which item won't come out of the Roulette: "))

    while player1turnItem == "":
        if itemChosen in items:
            player1turnItem = itemChosen
            player = 2
        else:
            itemChosen = input("Invalid item!! Choose another: ")
    
def player2turn():
    global player2turnItem
    global player
    player = 2
    player2turnItem = ""
    itemChosen = str(input(Player2 + ", bet which item won't come out of the Roulette: "))

    while player2turnItem == "":
        if itemChosen in items:
            player2turnItem = itemChosen
            player = 1
        else:
            itemChosen = input("Invalid item!! Choose another: ")

def logic():
    printPlayer1inv()
    printPlayer2inv()
    enterAnyKey(True)
    player1bet()
    player2bet()
    enterAnyKey(False)
    printItems()

def move():
    global gameover
    global player
    player = 1
    logic()
    while gameover == False:
        if player == 1:
            player1turn()
        if player == 2:
            player2turn()


instructions()
enterAnyKey(False)
enterName()
move()
