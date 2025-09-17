import tkinter as tk
from tkinter import *
from tkinter import ttk

# alright, I wanna do something

win=tk.Tk()
frm=ttk.Frame(win, padding=20)
# frm.grid()
# first value is width, second is height
win.geometry('1200x600')
win.title('Listless')
print(win.configure())

prompt=StringVar()

def yesResponse():
    # some code
    prompt.set('Prompt works')

def noResponse():
    prompt.set('Prompt is not working lol')

Label(win, textvariable=prompt, width=40, font=('Courier', 40)).place(relx=.5, rely=.3, anchor=CENTER)
Button(win, text='YES', font=('Ubuntu', 25), command=yesResponse, bg='light green').place(relx=.4, rely=.5, anchor=CENTER)
Button(win, text='NO', font=('Ubuntu', 25), command=noResponse, bg='red').place(relx=.6, rely=.5, anchor=CENTER)

win.mainloop()