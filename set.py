import os
import sys
from tkinter import *
from PIL import Image, ImageTk

class Deck:
    cards = {}

    # The deck is created by filling the dictionary with each of the 81 cards needed to
    # complete the deck via a sequence of nested for loops that assigns the key of each   
    # card to be a unique four-digit code and the value to be the card object itself.
    def __init__(self):
        for n in range(1,4):
            for s in range(1,4):
                for f in range(1,4):
                    for c in range(1,4):
                        self.cards[str(n) + str(s) + str(f) + str(c)] = \
                            Card(n,s,f,c, str(n) + str(s) + str(f) + str(c))

class Card:
    def __init__(self, num, shape, fill, color, image):
        shapes = {1 : "Diamond", 2 : "Oval", 3 : "Squiggle"}
        fills = {1 : "Empty", 2 : "Full", 3 : "Striped"}
        colors = {1 : "Red", 2 : "Green", 3 : "Purple"}

        self.num = num
        self.shape = shapes[shape]
        self.fill = fills[fill]
        self.color = colors[color]
        self.image = images[image]

game = Tk()
game.geometry("588x475+675+300")
welcome = Label(text="Welcome to the Game Set!")

# Gathering the images associated with the cards from the DeckoCards directory
images = {}
for image in os.listdir("DeckoCards"):
    images[image.replace('.png','')] = ImageTk.PhotoImage(Image.open(os.path.join("DeckoCards", image)))

# Creating the Game Deck
deck = Deck()

# Array of Card objects related to the current set the player is working on
currentSet = []

def buttonPush():
    display_label=Label(game,text="testing")
    display_label.grid(row=5,column=0,columnspan=5)

shrek=ImageTk.PhotoImage(Image.open("shrek.jpg"))

def checkSet():
    checkNum = 0

notASet = Tk()
notASet.geometry("320x180+800+450")
incorrectMessage = Label(notASet, text="Sorry, that isn't a set. Try again!")
incorrectMessage.grid(row=3, column=0, columnspan=5)

def press1():
    if len(currentSet) < 3:
        currentSet.append()
    else:
        if checkSet() == True:
            0
        else:
            0

def gameStart():

    button_1 = Button(game, text="Some", padx=50, pady=50, command= buttonPush)#, image=null)
    button_2 = Button(game, text="body", padx=50, pady=50, command= buttonPush)#, image=null)
    button_3 = Button(game, text="once", padx=50, pady=50, command= buttonPush)#, image=null)
    button_4 = Button(game, text="told", padx=50, pady=50, command= buttonPush)#, image=null)
    button_5 = Button(game, text="me", padx=50, pady=50, command= buttonPush)#, image=null)
    button_6 = Button(game, text="the", padx=50, pady=50, command= buttonPush)#, image=null)
    button_7 = Button(game, text="world", padx=50, pady=50, command= buttonPush)#, image=null)
    button_8 = Button(game, text="was", padx=50, pady=50, command= buttonPush)#, image=null)
    button_9 = Button(game, text="gonna", padx=50, pady=50, command= buttonPush)#, image=null)
    button_10 = Button(game, text="roll", padx=50, pady=50, command= buttonPush)#, image=null)
    button_11 = Button(game, text="me", padx=50, pady=50, command= buttonPush)#, image=null)
    button_12 = Button(game, text="I", padx=50, pady=50, command= buttonPush)#, image=shrek)

    button_1.grid(row=2,column=1)
    button_2.grid(row=2,column=2)
    button_3.grid(row=2,column=3)
    button_4.grid(row=2,column=4)
    button_5.grid(row=3,column=1)
    button_6.grid(row=3,column=2)
    button_7.grid(row=3,column=3)
    button_8.grid(row=3,column=4)
    button_9.grid(row=4,column=1)
    button_10.grid(row=4,column=2)
    button_11.grid(row=4,column=3)
    button_12.grid(row=4,column=4)

    display_label=Label(game, text = "                         ")
    display_label.grid(row=5,column=0,columnspan=5)

    game.mainloop()

startButton = Button(game, text="Start",padx=15,pady=5, command=gameStart)
retryButton = Button(game, text="Reset",padx=15,pady=5, command=gameStart)
startButton.grid(row=1,column=2)
retryButton.grid(row=1,column=3)
welcome.grid(row=0,column=0,columnspan=5)

# This is to center the Starting Screen

fill1 = Label(game,text=' ',padx=70,pady=55)
fill2 = Label(game,text=' ',padx=70,pady=55)
fill3 = Label(game,text=' ',padx=70,pady=55)
fill4 = Label(game,text=' ',padx=70,pady=55)
fill5 = Label(game,text=' ',padx=70,pady=55)
fill6 = Label(game,text=' ',padx=70,pady=55)
fill7 = Label(game,text=' ',padx=70,pady=55)
fill8 = Label(game,text=' ',padx=70,pady=55)
fill9 = Label(game,text=' ',padx=70,pady=55)
fill10 = Label(game,text=' ',padx=70,pady=55)
fill11 = Label(game,text=' ',padx=70,pady=55)
fill12 = Label(game,text=' ',padx=70,pady=55)

fill1.grid(row=2,column=1)
fill2.grid(row=2,column=2)
fill3.grid(row=2,column=3)
fill4.grid(row=2,column=4)
fill5.grid(row=3,column=1)
fill6.grid(row=3,column=2)
fill7.grid(row=3,column=3)
fill8.grid(row=3,column=4)
fill9.grid(row=4,column=1)
fill10.grid(row=4,column=2)
fill11.grid(row=4,column=3)
fill12.grid(row=4,column=4)

startButton.grid(row=1,column=2)
retryButton.grid(row=1,column=3)
welcome.grid(row=0,column=0,columnspan=5)

game.mainloop()
notASet.mainloop()