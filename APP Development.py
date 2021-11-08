
#import the library
import tkinter as Tk
from tkinter import *
from tkinter import filedialog, Text
#create a window object
root = Tk()


#Define a function
def addApp():
    filename= filedialog.askopenfilename(initialdir="/", title="Select File",)
    filetypes=(()))


#setup the window size
frame = Tk.Frame(root, width=600, height=600)
#put the sizing  into our window (pack is the simplest method)
frame.pack()

#setup canvas size and color
canvas = Canvas(root, width=600, height=900, bg="blue")
canvas.pack()

#Add a button to root
openFile = Button(root, text="Open File", padx=10, pady=5, fg="white", 
                            bg="red" command=addAPP) 
openFile.pack()

runApps = Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="red") 
runApps.pack()


#title the overall window
root.title("STIMythBuster")
#show the window - windows run in a loop listening for the window close button to break the loop
root.mainloop()

