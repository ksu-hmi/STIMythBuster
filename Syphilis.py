# [] create The link to Syphilis facts

from tkinter import *

import webbrowser

def open():

    webbrowser.open ("https://www.cdc.gov/std/Syphilis")

root = Tk()

syphilis_btn = Button(root, text= "CDC Syphilis Facts",command=open, padx=300, pady=300, fg="gray", bg="blue")

syphilis_btn.pack()

root.mainloop()
