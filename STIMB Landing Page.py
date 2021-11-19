#import libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


#beginning of code
root = tk.Tk()
root.title("STIMythBusters Interactive Application")

canvas = tk.Canvas(root, bg="purple", width=600, height=400)
canvas.grid(columnspan=4, rowspan=4)

canvas2 = tk.Canvas2(root, bg="purple", width=600, height=400)
canvas2.grid(columnspan=4, rowspan=4)

frame = tk.Canvas2(root, bg="blue", width=600, height=400)
frame.grid(x=20, y=20)

#Open logo
load = Image.open("logo.png")
render = ImageTk.PhotoImage(load)
#Then associate it with the label:
img = tk.Label(canvas, image=render)
img.image = render
img.place(x=20, y=20)


#instrutions - Landing Page
instructions = tk.Label(root, text="Welcome to STIMythBusters", font="Raleway", bg="brown", fg="white")
instructions.grid(columnspan=4, column=0, row=0)


def open_file():
    browser_text.set("loading....")
    canvas2 = tk.Canvas(root, bg="purple", width=600, height=400)
    canvas2.grid(columnspan=4, rowspan=4) 

#button = tk.Button(canvas2, text="new window",command=lambda:open_file(), bg='black', fg='#469A00', )
#button.grid(column=1, row=2)
    
#create button that will be placed on canvas2
browser_text2 = tk.StringVar()
browse_btn= tk.Button(canvas2, textvariable=browser_text2, command=lambda:open_file(), font="Raleway", bg="green", fg="white", height=2, width=15)
browser_text2.set("LEARN MORE")
browse_btn.grid(column=1, row=2)
    

#browser button 1
browser_text = tk.StringVar()
browse_btn= tk.Button(root, textvariable=browser_text, command=lambda:open_file(), font="Raleway", bg="green", fg="white", height=2, width=15)
browser_text.set("SearchbySTI")
browse_btn.grid(column=1, row=2)

def open_button():
    browse_text.set("loading....")
    canvas2 = tk.Canvas(root, bg="purple", width=600, height=400)
    canvas2.grid(columnspan=4, rowspan=4) 

#browse button 2
browse_text = tk.StringVar()
browse_btn= tk.Button(root, textvariable=browse_text, command=lambda:open_button(), font="Raleway", bg="green", fg="white", height=2, width=15)
browse_text.set("SearchbySymptoms")
browse_btn.grid(column=2, row=2)




#ending of code
root.mainloop()


