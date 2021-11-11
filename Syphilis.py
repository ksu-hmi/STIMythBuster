# [] create The link to Syphilis facts

from tkinter import *

import webbrowser

def open():

    webbrowser.open ("https://www.cdc.gov/std/Syphilis")

root = Tk()

res_btn = Button(root, text= "CDC Syphilis Facts",command=open, padx=30, fg="gray", bg="dark blue")

res_btn.pack()

root.mainloop()