# [] create The link to HPV facts

from tkinter import *

import webbrowser

def open():

    webbrowser.open ("https://www.cdc.gov/std/treatment-guidelines/hpv.htm")

root = Tk()

res_btn = Button(root, text= "CDC HPV Facts",command=open, padx=30, fg="gray", bg="dark blue")

res_btn.pack()

root.mainloop()