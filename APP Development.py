
#import the library
import tkinter as Tk
from tkinter import *


#create a window object
root = Tk()


#setup the window size
frame = Tk.Frame(root, width=600, height=600)
#put the sizing  into our window (pack is the simplest method)
frame.pack()

#setup canvas size and color
canvas = Canvas(root, width=700, height=700, bg="blue")
canvas.pack()

#Create a label
label = Label(frame, text='Welcome to STIMythBusters')
label.pack()

#Add a button to frame
def create.frames(self):
    self.left_frame = Tk.Frame(width=140, height=140, background='red')
    self.left_frame.grid(row=0, column=0)

#Add a button to root
runApps = Button(root, text="Click Here", padx=10, pady=5, fg="white", bg="red") 
runApps.pack()



#title the overall window
root.title("STIMythBuster")

#show the window - windows run in a loop listening for the window close button to break the loop
root.mainloop()

