
#import the library
import tkinter as Tk
from tkinter import *

#create a window object
root = Tk()

#setup canvas size and color
canvas = Canvas(root, width=700, height=6700, bg="blue")
canvas.pack()

#setup the window size
frame = Frame(root, bg="white")
#put the sizing  into our window (pack is the simplest method)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


#Create a label
label = Label(frame, text='Welcome to STIMythBusters')
label.pack()

#Add a button to frame
Button = Button(frame, text="SearchbySTI")
Button.pack()

#Add a button to root
runApps = Button(root, text="Click Here", padx=10, pady=5, fg="white", bg="red") 
runApps.pack()


#title the overall window
root.title("STIMythBuster")

#show the window - windows run in a loop listening for the window close button to break the loop
root.mainloop()

