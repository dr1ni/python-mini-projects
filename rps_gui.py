import tkinter as tk
from tkinter import Entry, filedialog, Text
import os
from tkinter import *
from tkinter import ttk
import random
import tkinter
import time
from tkinter.constants import W, Y

root = tkinter.Tk()
canvas = tkinter.Canvas(root, height=400, width=600, bg="#808080")
canvas.pack()
menuoptions = [
    "Rock",
    "Paper",
    "Scissors"
]
variable = StringVar(root)
variable.set(menuoptions[0])
menu = tk.OptionMenu(root, variable, *menuoptions)
menu.place(x=200, y= 8)
def close():
    quit()
def mc():
    clearlabel1 = tk.Label(root, width=50, bg="#808080")
    clearlabel1.place(x=220, y= 125)
    clearlabel2 = tk.Label(root, width=50, bg="#808080")
    clearlabel2.place(x=220, y= 125)
    clearlabel3 = tk.Label(root, width=50, bg="#808080")
    clearlabel3.place(x=220, y= 200)
    rn=random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    e = variable.get().lower()
    if e not in ["rock", "paper", "scissors", "q"]:
        blanklabel = tk.Label(root, width=100, bg="#808080", text="")
        blanklabel.place(x=100, y=50)
        errlabel = tkinter.Label(root, fg="red", bg="black", text="Please enter Rock, Paper or Scissors: ")
        errlabel.place(x=200, y=50)
    else:
        options = ["rock", "paper", "scissors"]
        options[0]
        ui=str(e)
        ui=ui.lower()
        if ui.lower()=="q":
            print("")
            #Label1 = tkinter.Label(root, bg="green", fg="black", text="Final Score Was: AI-"+cw+" vs User-"+uw+" with "+draw+" draws.")
            #Label1.place(x=200, y=50)
        if ui.lower() in ["rock", "paper", "scissors"]:
            cg = options[rn]
            Label2 = tkinter.Label(root, width=20,  bg="#808080", fg="black", text="AI Picked: " + cg.capitalize() + "")
            Label2.place(x=220, y= 125)  
            blanklabel1 = tk.Label(root, width=100, bg="#808080", text="")
            if ui.lower() == "rock" and cg == "scissors":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label3 = tkinter.Label(root, width=22, fg="black", bg="lime", text="You won! Congrats")
                blanklabel1.place(x=220, y= 200)
                Label3.place(x=225, y= 200)
            elif ui.lower() == "paper" and cg == "rock":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label4 = tkinter.Label(root, width=22, fg="black", bg="lime", text="You won! Congrats")
                blanklabel1.place(x=220, y= 200)
                Label4.place(x=225, y= 200)
            elif ui.lower() == "scissors" and cg == "paper":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label5 = tkinter.Label(root, width=22, fg="black", bg="lime", text="You won! Congrats")
                blanklabel1.place(x=220, y= 200)
                Label5.place(x=225, y= 200)
            elif ui.lower() == "rock" and cg == "rock":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label6 = tkinter.Label(root, width=22, bg="orange", fg="black", text="Its a draw!")
                blanklabel1.place(x=220, y= 200)
                Label6.place(x=225, y= 200)
            elif ui.lower() == "scissors" and cg == "scissors":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label7 = tkinter.Label(root, width=22, bg="orange", fg="black", text="Its a draw!")
                blanklabel1.place(x=220, y= 200)
                Label7.place(x=225, y= 200)
            elif ui.lower() == "paper" and cg == "paper":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label8 = tkinter.Label(root, width=22, bg="orange", fg="black", text="Its a draw!")
                blanklabel1.place(x=220, y= 200)
                Label8.place(x=225, y= 200)  
            else:
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label9 = tkinter.Label(root, width=22, bg="red", fg="black", text="You Lost!")
                blanklabel1.place(x=220, y= 200)
                Label9.place(x=220, y= 200)      
mb = tkinter.Button(root, text="Start", command=mc)
mb.place(x=350, y= 10)
cb = tkinter.Button(root, bg="red", text="Exit", command=close)
cb.place(x=550, y= 350)
root.mainloop()