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
e = Entry(root)
e.place(x=200, y= 8)
e.get()
def mc():
    
    rn=random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    if e.get().lower() not in ["rock", "paper", "scissors"]:
        errlabel = tkinter.Label(root, fg="red", bg="black", text="Please enter Rock, Paper or Scissors: ")
        errlabel.place(x=200, y=50)
    
    else:
        uw = 0
        cw = 0
        draw = 0
        options = ["rock", "paper", "scissors"]
        options[0]
        #myLabel = tkinter.Label(root, text="You picked "+e.get()+"", bg="white")
        #myLabel.place(x=270, y= 30)
        ui=str(e.get())
        ui=ui.lower()
        if ui.lower()=="q":
            cw=str(cw)
            uw=str(uw)
            draw=str(draw)
            Label1 = tkinter.Label(root, text="Final Score Was: AI-"+cw+"vs User-"+uw+"with"+draw+"draws.")
            Label1.place(x=270, y= 30)
        if ui.lower() in ["rock", "paper", "scissors"]:
            cg = options[rn]
            Label2 = tkinter.Label(root, text="AI Picked: " + cg + "")
            Label2.place(x=250, y= 125)
            if ui.lower() == "rock" and cg == "scissors":
                Label3 = tkinter.Label(root, width=20, fg="red", bg="black", text="You won! Congrats")
                Label3.place(x=225, y= 200)
                uw += 1
            elif ui.lower() == "paper" and cg == "rock":
                Label4 = tkinter.Label(root, width=20, fg="red", bg="black", text="You won! Congrats")
                Label4.place(x=225, y= 200)
                uw += 1
            elif ui.lower() == "scissors" and cg == "paper":
                Label5 = tkinter.Label(root, width=20, fg="red", bg="black", text="You won! Congrats")
                Label5.place(x=225, y= 200)
                uw += 1
            elif ui.lower() == "rock" and cg == "rock":
                Label6 = tkinter.Label(root, width=20, fg="red", bg="black", text="Its a draw!")
                Label6.place(x=225, y= 200)
                draw += 1
            elif ui.lower() == "scissors" and cg == "scissors":
                Label7 = tkinter.Label(root, width=20, fg="red", bg="black", text="Its a draw!")
                Label7.place(x=225, y= 200)
                draw += 1
            elif ui.lower() == "paper" and cg == "paper":
                Label8 = tkinter.Label(root, width=20, fg="red", bg="black", text="Its a draw!")
                Label8.place(x=225, y= 200)
                draw += 1  
            else:
                Label9 = tkinter.Label(root, width=20, fg="red", bg="black", text="You Lost!")
                Label9.place(x=225, y= 200)
                cw += 1         
mb = tkinter.Button(root, text="Start", command=mc)
mb.place(x=375, y= 5)

        
root.mainloop()
