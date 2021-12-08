from tkinter import *
import webbrowser

def open():
    webbrowser.open ("https://dph.georgia.gov/STDs")


root = Tk()

res_btn = Button(root, text= "GA Dept of Public Health",command=open, padx=100, pady=50, fg="yellow", bg="teal")

res_btn.pack()


def resize(e):
    size = e.width / 30
    res_btn.config(font=("Helveltica", int(size)))
  

root.bind('<Configure>', resize)

root.mainloop()

