# [] create The link to Trichomonas facts

from tkinter import *

import webbrowser

def open():

    webbrowser.open ("https://www.cdc.gov/std/Trichomonas")

root = Tk()

trichomonas_btn = Button(root, text= "CDC Trichomonas Facts",command=open, padx=300, pady=300, fg="gray", bg="blue")

trichomonas_btn.pack()

root.mainloop()
