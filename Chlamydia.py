# [] create The link to Chlamydia facts

from tkinter import *

import webbrowser

def open():

    webbrowser.open ("https://www.cdc.gov/std/Chlamydia")

root = Tk()

clyamydia_btn = Button(root, text= "CDC Chlamydia Facts",command=open, padx=300, pady=300 fg="gray", bg="blue")

clyamydia_btn.pack()

root.mainloop()
