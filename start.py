import tkinter as tk
from tkinter import *
from tkinter import ttk

win=tk.Tk() # this creates a "top level widget" which is used to create a main window for an application
win.geometry('750x750') # this sets the height and width of the window
win.title('Listless')

# win.mainloop()

root=Tk()
frm=ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text='Hello World').grid(column=0, row=0)
ttk.Button(frm, text='Quit', command=root.destroy).grid(column=1, row=0)
root.mainloop()