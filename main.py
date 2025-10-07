## loop - straight up looping it


import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Label

root = Tk()
root.maxsize(1080, 1080)
frm = ttk.Frame(root, padding=10)
frm.grid()
text = ttk.Label(root, text="Daniel is approaching . . . Better Run!")
text.pack(pady=20)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

