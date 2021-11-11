from tkinter import *
import webbrowser

def open():
    webbrowser.open ("https://www.cdc.gov/std/treatment/resources.htm")


root = Tk()

res_btn = Button(root, text= "Resources",command=open, padx=30, fg="fuchsia", bg="dark blue")

res_btn.pack()

root.mainloop()



