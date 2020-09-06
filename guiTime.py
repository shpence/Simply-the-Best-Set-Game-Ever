from tkinter import *

game = Tk()
game.geometry
welcome = Label(text="Welcome to the Game Set!")
startButton = Button(game, text="Start",padx=15,pady=5)
retryButton = Button(game, text="Reset",padx=15,pady=5)

startButton.grid(row=1,column=2)#, command=start)
retryButton.grid(row=1,column=3)#, command=start)
welcome.grid(row=0,column=0,columnspan=5)

game.mainloop()

def buttonPush():
    display_label=Label(game,text="testing")
    display_label.grid(row=5,column=0,columnspan=5)
# image assignment is "certainImg = ImageTk.PhotoImage(Image.open("filename.jpg"))""

def start():

    button_1 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_2 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_3 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_4 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_5 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_6 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_7 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_8 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_9 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_10 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_11 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)
    button_12 = Button(game, text="summ", padx=50, pady=50, command= buttonPush)#, image=null)

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


    root.mainloop()










# https://github.com/aloverso/setgame