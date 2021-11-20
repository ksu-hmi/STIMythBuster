from tkinter import *
import webbrowser

def open():
    webbrowser.open ("https://www.cdc.gov/std/prevention/default.htm")


root = Tk()

res_btn = Button(root, text= "Prevention",command=open, padx=100, pady=40, fg="Fuchsia", bg="dark blue")

res_btn.pack()

root.mainloop()