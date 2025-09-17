import tkinter as tk
from tkinter import *
from tkinter import ttk

# win=tk.Tk() # this creates a "top level widget" which is used to create a main window for an application
# specifically the .Tk() is what creates the top level widget
# win.geometry('750x750') # this sets the height and width of the window. Measurements in what?
# win.title('Listless') # sets the title for the window that appears

# win.mainloop()

root=Tk()
frm=ttk.Frame(root, padding=10) # creates a window frame with some padding
frm.grid() # initializes a grid for us to customize

userInput=StringVar()

ttk.Label(frm, text='Hello World').grid(column=0, row=0) # creates a label
ttk.Button(frm, text='Quit', command=root.destroy).grid(column=1, row=0) # creates a button
ttk.Entry(frm, textvariable=userInput, width=20).grid(column=0, row=1)
root.mainloop()

# this program currently opens 2 windows, one with nothing in it called 
# "Listless", the other that says 'Hello World' with a button to self destruct