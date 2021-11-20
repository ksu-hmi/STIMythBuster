from tkinter import *
import webbrowser

def open():
    webbrowser.open ("https://www.cdc.gov/std/treatment/resources.htm")


root = Tk()

res_btn = Button(root, text= "Resources",command=open, padx=100, pady=40, fg="fuchsia", bg="dark blue")

res_btn.pack()


def resize(e):
    size = e.width / 20
    res_btn.config(font=("Helveltica", int(size)))
  

root.bind('<Configure>', resize)

root.mainloop()

