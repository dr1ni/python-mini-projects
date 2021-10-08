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
    "Up",
    "Down",
    "Right",
    "Left"
]
variable = StringVar(root)
variable.set(menuoptions[0])
menu = tk.OptionMenu(root, variable, *menuoptions)
menu.place(x=200, y= 8)
def close():
    quit()
def mc():
    menuoptions = [
    "up",
    "down",
    "right",
    "left"
    ]
    clearlabel1 = tk.Label(root, width=50, bg="#808080")
    clearlabel1.place(x=220, y= 125)
    clearlabel2 = tk.Label(root, width=50, bg="#808080")
    clearlabel2.place(x=220, y= 125)
    clearlabel3 = tk.Label(root, width=50, bg="#808080")
    clearlabel3.place(x=220, y= 200)
    rn=random.randint(0,3)
    # up: 0, down: 1, left: 2, right: 3
    e = variable.get().lower()
    if 1 != 1:
        print("")
    else:
        options = ["up", "down", "right", "left"]
        options[0]
        ui=str(e)
        ui=ui.lower()
        if ui.lower() in ["up", "down", "right", "left"]:
            cg = options[rn]
            Label2 = tkinter.Label(root, width=20,  bg="#808080", fg="black", text="AI Picked: " + cg.capitalize() + "")
            Label2.place(x=220, y= 125)  
            blanklabel1 = tk.Label(root, width=100, bg="#808080", text="")
            if ui.lower() == "up" and cg == "up":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label3 = tkinter.Label(root, width=22, fg="black", bg="lime", text="You won! Congrats")
                blanklabel1.place(x=220, y= 200)
                Label3.place(x=225, y= 200)
            elif ui.lower() == "left" and cg == "left":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label4 = tkinter.Label(root, width=22, fg="black", bg="lime", text="You won! Congrats")
                blanklabel1.place(x=220, y= 200)
                Label4.place(x=225, y= 200)
            elif ui.lower() == "down" and cg == "down":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label5 = tkinter.Label(root, width=22, fg="black", bg="lime", text="You won! Congrats")
                blanklabel1.place(x=220, y= 200)
                Label5.place(x=225, y= 200)
            elif ui.lower() == "right" and cg == "right":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label5 = tkinter.Label(root, width=22, fg="black", bg="lime", text="You won! Congrats")
                blanklabel1.place(x=220, y= 200)
                Label5.place(x=225, y= 200)
            elif ui.lower() == "right" and cg == "left":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label7 = tkinter.Label(root, width=22, bg="red", fg="black", text="You lost!")
                blanklabel1.place(x=220, y= 200)
                Label7.place(x=225, y= 200)
            elif ui.lower() == "left" and cg == "right":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label7 = tkinter.Label(root, width=22, bg="red", fg="black", text="You lost!")
                blanklabel1.place(x=220, y= 200)
                Label7.place(x=225, y= 200)
            elif ui.lower() == "up" and cg == "down":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label7 = tkinter.Label(root, width=22, bg="red", fg="black", text="You lost!")
                blanklabel1.place(x=220, y= 200)
                Label7.place(x=225, y= 200)
            elif ui.lower() == "down" and cg == "up":
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label7 = tkinter.Label(root, width=22, bg="red", fg="black", text="You lost!")
                blanklabel1.place(x=220, y= 200)
                Label7.place(x=225, y= 200)
            else:
                blanklabel = tk.Label(root, width=100, bg="#808080", text="")
                blanklabel.place(x=100, y=50)
                Label7 = tkinter.Label(root, width=22, bg="orange", fg="black", text="Its a draw!")
                blanklabel1.place(x=220, y= 200)
                Label7.place(x=225, y= 200)

mb = tkinter.Button(root, text="Start", command=mc)
mb.place(x=350, y= 10)
cb = tkinter.Button(root, bg="red", text="Exit", command=close)
cb.place(x=550, y= 350)
root.mainloop()