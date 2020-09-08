import os
import sys
from tkinter import *
from PIL import Image, ImageTk
import random
from playsound import playsound

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

# Class for the puzzles in Puzzle Mode
class Puzzle:
    def __init__(self, cards, sets):
        self.cards = cards
        self.sets = sets
        
# Game window setup
game = Tk()
game.geometry("588x175+675+300")
welcome = Label(text="Welcome to the Game Set!")

# Gathering the images associated with the cards from the DeckoCards directory
images = {}
for image in os.listdir("DeckoCards"):
    images[image.replace('.png','')] = ImageTk.PhotoImage(Image.open(os.path.join("DeckoCards", image)))

# Creating the Game Deck
deck = Deck()

# List of all the puzzles for Puzzle Mode
puzzles = []
p1 = Puzzle(['1121', '2233', '3321', '3222', '1113', '1223', '1332', '3213', '2131', '2221', '3111', '2313'], \
    [['1121', '2131', '3111'], ['1223', '2233', '3321'], ['1121', '2221', '3321'], ['1332', '2313', '3321'], ['1223', '2221', '3222'], ['1113', '2313', '3213']])

# List of Card objects related to the current set the player is working on
currentSet = []

# Global list variable to track the cards currently on the table
table = [None]*12

# Series of functions related to pressing one of the buttons numbered 1-12
def push1():
    currentSet.append(deck.cards[table[0]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push2():
    currentSet.append(deck.cards[table[1]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push3():
    currentSet.append(deck.cards[table[2]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push4():
    currentSet.append(deck.cards[table[3]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push5():
    currentSet.append(deck.cards[table[4]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push6():
    currentSet.append(deck.cards[table[5]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push7():
    currentSet.append(deck.cards[table[6]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push8():
    currentSet.append(deck.cards[table[7]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push9():
    currentSet.append(deck.cards[table[8]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push10():
    currentSet.append(deck.cards[table[9]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push11():
    currentSet.append(deck.cards[table[10]])
    if len(currentSet) == 3:
        checkSet(currentSet)

def push12():
    currentSet.append(deck.cards[table[11]])
    if len(currentSet) == 3:
        checkSet(currentSet)
    
# Checks the full set to determine if it is indeed a set
def checkSet(curSet):
    checkNum = set()
    checkShape = set()
    checkFill = set()
    checkColor = set()

    for x in range(3):
        checkNum.add(int(curSet[x].num))
        checkShape.add(curSet[x].shape)
        checkFill.add(curSet[x].fill)
        checkColor.add(curSet[x].color)

    if (len(checkNum)!=2) & (len(checkShape)!=2) & (len(checkFill)!=2) & (len(checkColor)!=2):
        congrats = Tk()
        congrats.geometry("120x70+900+505")
        messages = Label(congrats, text = "That's a set!")
        filler = Label(congrats, text = ' ')
        filler.pack()
        messages.pack()
        playsound("yay.mp3", block=False)

    else:
        # Error message for an incorrect set
        notASet = Tk()
        notASet.geometry("220x80+850+500")
        incorrectMessage = Label(notASet, text="Sorry, that isn't a set. Try again!")
        incorrectMessage.grid(row=1, column=2, columnspan=4)
        pusher = Label(notASet, text=' ', padx=10, pady=20)
        pusher.grid(row=1, column=1)
        playsound("oh no.mp3", block=False)

    curSet.clear()

# The function for when the Player presses the "Rules" button
def rulesPressed():
    ruleBook = Tk()
    ruleBook.geometry("+450+50")
    ruleBook.title('Rule Book')
    rulesLabel9 = Label(ruleBook, text="RULES OF THE GAME SET:")
    rulesLabel1 = Label(ruleBook, text="The rules of the game are simple and complex at the same time. To win you have to get through the entirety of the deck, much like solitaire.")
    rulesLabel2 = Label(ruleBook, text="To get rid of cards you much match them into sets of three. Now here's the kicker, every card of your set must be exactly the same or exactly different.")
    rulesLabel3 = Label(ruleBook, text="What that means is the Shape, color, and number of the 3 cards must be either the same on all 3 cards or different on all 3 cards.")
    rulesLabel4 = Label(ruleBook, text="For example- two open red ovals, two dashed red ovals, and two filled red ovals is a set. One dashed green squiggle, two dashed purple ovals, and three dashed red diamonds is a set.")
    rulesLabel5 = Label(ruleBook, text="Another example would be one dashed purple oval, two filled green diamonds, three open red squiggles.")
    rulesLabel6 = Label(ruleBook, text="Now an example that wouldn't work is one open purple oval, two open red ovals, and three open green diamonds. This is because the third was diamonds rather than ovals.")
    rulesLabel7 = Label(ruleBook, text="HINT:")
    rulesLabel8 = Label(ruleBook, text="If youre having trouble finding a set and get stuck, restart! Sometimes the cards won't actually contain a set. Part of your strategy should be eliminating the right cards to always have another set.")
    
    rulesLabel9.pack()
    rulesLabel1.pack()
    rulesLabel2.pack()
    rulesLabel3.pack()
    rulesLabel4.pack()
    rulesLabel5.pack()
    rulesLabel6.pack()
    rulesLabel7.pack()
    rulesLabel8.pack()

# Infinite gameplay setup
#     for x in range(12):
#         hold = list(deck.cards.keys())[random.randrange(len(deck.cards.keys()))]
#         if hold not in table:
#             table[x] = hold
#         else:
#             while hold in table:
#                 hold = list(deck.cards.keys())[random.randrange(len(deck.cards.keys()))]
#             table[x] = hold

def gameStart():
    for x in range(12):
        hold = list(deck.cards.keys())[random.randrange(len(deck.cards.keys()))]
        if hold not in table:
            table[x] = hold
        else:
            while hold in table:
                hold = list(deck.cards.keys())[random.randrange(len(deck.cards.keys()))]
            table[x] = hold

    game.geometry("825x475+547+300")

    button_1 = Button(game, text="Some", padx=50, pady=50, command= push1, image=deck.cards[table[0]].image)
    button_2 = Button(game, text="body", padx=50, pady=50, command= push2, image=deck.cards[table[1]].image)
    button_3 = Button(game, text="once", padx=50, pady=50, command= push3, image=deck.cards[table[2]].image)
    button_4 = Button(game, text="told", padx=50, pady=50, command= push4, image=deck.cards[table[3]].image)
    button_5 = Button(game, text="me", padx=50, pady=50, command= push5, image=deck.cards[table[4]].image)
    button_6 = Button(game, text="the", padx=50, pady=50, command= push6, image=deck.cards[table[5]].image)
    button_7 = Button(game, text="world", padx=50, pady=50, command= push7, image=deck.cards[table[6]].image)
    button_8 = Button(game, text="was", padx=50, pady=50, command= push8, image=deck.cards[table[7]].image)
    button_9 = Button(game, text="gonna", padx=50, pady=50, command= push9, image=deck.cards[table[8]].image)
    button_10 = Button(game, text="roll", padx=50, pady=50, command= push10, image=deck.cards[table[9]].image)
    button_11 = Button(game, text="me", padx=50, pady=50, command= push11, image=deck.cards[table[10]].image)
    button_12 = Button(game, text="I", padx=50, pady=50, command= push12, image=deck.cards[table[11]].image)
    retryButton = Button(game, text="Reset",padx=15,pady=5, command=gameStart)

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
    retryButton.grid(row=1,column=2)
    
    display_label=Label(game, text = "                           ")
    display_label.grid(row=5,column=0,columnspan=5)
    
    game.mainloop()

startButton = Button(game, text="Start",padx=15,pady=5, command=gameStart)
ruleButton = Button(game, text="Rules",padx=15,pady=5,command=rulesPressed)
startButton.grid(row=1,column=2)
ruleButton.grid(row=1,column=3)

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

game.mainloop()