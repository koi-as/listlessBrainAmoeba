import tkinter as tk
from tkinter import *
from tkinter import ttk

# alright, I wanna do something

win=tk.Tk()
frm=ttk.Frame(win, padding=20)
frm.grid()
# first value is width, second is height
win.geometry('1200x600')
win.title('Listless')
print(win.configure())

Button(win, text='DIE, loser', command=win.destroy).place(relx=.5, rely=.5, anchor=CENTER)

win.mainloop()