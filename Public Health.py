from tkinter import *
import webbrowser

def open():
    webbrowser.open ("https://dph.georgia.gov/STDs")


root = Tk()

res_btn = Button(root, text= "GA Dept of Public Health",command=open, padx=100, pady=40, fg="yellow", bg="teal")

res_btn.pack()

root.mainloop()