import tkinter
from tkinter import Entry, filedialog, Text
import os
import tkinter
from tkinter.constants import Y

root = tkinter.Tk()


canvas = tkinter.Canvas(root, height=700, width=700, bg="#808080")
canvas.pack()
frame = tkinter.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
title= tkinter.Label(frame, text="Rock, Paper, Scissors!")


e = Entry(frame)
e.pack()
e.get()

def mc():
    myLabel = tkinter.Label(frame, text="You picked "+e.get()+"", bg="white")
    myLabel.pack()
    ui = str(e.get())
    print(ui)

mb = tkinter.Button(frame, text="Enter here", command=mc)
mb.pack()



root.mainloop()