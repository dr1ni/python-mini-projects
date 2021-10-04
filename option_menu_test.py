import tkinter as tk
import tkinter 
import time, random
from tkinter import Entry, OptionMenu, StringVar, Variable, filedialog, Text
import os
from tkinter.constants import Y
from tkinter import Entry, filedialog, Text
from tkinter import *
from tkinter import ttk
from tkinter.constants import W, Y

root = tkinter.Tk()

options = [
    "rock",
    "paper",
    "scissors"
]

variable = StringVar(root)

canvas = tkinter.Canvas(root, height=700, width=700, bg="#808080")
canvas.pack()
def send():
    option = variable.get()
    sendlabel = tk.Label(root, width=20, text="You selected: "+option+"")
    sendlabel.pack()
start = tk.Button(root, text="Send", command=send)
start.pack()



optionmenu = tk.OptionMenu(root, variable, *options)
optionmenu.pack()

root.mainloop()