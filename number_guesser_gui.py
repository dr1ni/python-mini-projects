import tkinter as tk
from tkinter import Entry, filedialog, Text
import os
import tkinter
from tkinter.constants import W, Y

root = tk.Tk()


canvas = tk.Canvas(root, height=400, width=600, bg="#808080")
canvas.grid(row=1, column=1, sticky=W)
title= tk.Label(root, text="Rock, Paper, Scissors!")
title.place

#rock paper scissors button

def okcmd():
    rps = entry1.get()
    print(rps)
    return None
entry1 = tkinter.Entry(root, width=35, bg="Black", fg="White",)
text = "Type Rock/Paper/Scissors or Q to quit:"
entry1.insert(0, text)
entry1.place(x=200, y=25)


ok=tk.Button(root, text="Start", command=okcmd, bg="Black", fg="White")
ok.place(x=250, y=22)


root.mainloop()