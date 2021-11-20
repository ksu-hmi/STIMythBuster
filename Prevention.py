from tkinter import *
import webbrowser

def open():
    webbrowser.open ("https://www.cdc.gov/std/prevention/default.htm")


root = Tk()

res_btn = Button(root, text= "Prevention",command=open, padx=100, pady=40, fg="Fuchsia", bg="Light Blue")

res_btn.pack()

def resize(e):
    size = e.width / 20
    res_btn.config(font=("Helveltica", int(size)))
  

root.bind('<Configure>', resize)

root.mainloop()