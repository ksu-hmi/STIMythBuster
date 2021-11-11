#import libraries
import tkinter as tk
from PILLOW import Image

#beginning of code
root = tk.Tk()

canvas = tk.Canvas(root, bg="purple", width=600, height=400)
canvas.grid(columnspan=4, rowspan=4)

#logo
logo = Image.open("logo.png")
logo = tk.Image.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo 
logo_label.grid(column=1, row=0)


#instrutions - Landing Page
instructions = tk.Label(root, text="Welcome to STIMythBusters", font="Raleway", bg="purple")
instructions.grid(columnspan=4, column=0, row=1)

def open_file():
    browser_text.set("loading....")

#browser button 1
browser_text = tk.StringVar()
browse_btn= tk.Button(root, textvariable=browser_text, command=lambda:open_file(), font="Raleway", bg="green", fg="white", height=2, width=15)
browser_text.set("SearchbySTI")
browse_btn.grid(column=1, row=2)

def open_file():
    browse_text.set("loading....")

#browse button 2
browse_text = tk.StringVar()
browse_btn= tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="green", fg="white", height=2, width=15)
browse_text.set("SearchbySymptoms")
browse_btn.grid(column=2, row=2)


#ending of code
root.mainloop()


