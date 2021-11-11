# [] create The link to HPV facts

from tkinter import *

import webbrowser

def open():

    webbrowser.open ("https://www.cdc.gov/std/treatment-guidelines/hpv.htm")

root = Tk()

hpv_btn = Button(root, text= "CDC HPV Facts",command=open, padx=30, fg="gray", bg="dark blue")

hpv_btn.pack()

root.mainloop()
