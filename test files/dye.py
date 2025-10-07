## loop - straight up looping it


import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Label

root = Tk()
root.maxsize(1080, 1080)
frm = ttk.Frame(root, padding=10)
frm.grid()
text = ttk.Label(frm, text="Daniel is approaching . . . Better Run!")

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()


while True:
    root = Tk()
    root.maxsize(1080, 1080)
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Daniel is approaching . . . Better Run!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()


