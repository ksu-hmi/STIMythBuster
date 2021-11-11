# [] create The link to Chlamydia facts

from tkinter import *

import webbrowser

def open():

    webbrowser.open ("https://www.cdc.gov/std/Chlamydia")

root = Tk()

res_btn = Button(root, text= "CDC Chlaymydia Facts",command=open, padx=30, fg="gray", bg="dark blue")

res_btn.pack()

root.mainloop()