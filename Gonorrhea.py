# [] create The link to Gonorrhea facts


from tkinter import *

import webbrowser



def open():

    webbrowser.open ("https://www.cdc.gov/std/Gonorrhea")




root = Tk()



res_btn = Button(root, text= "CDC Gonorrhea Facts",command=open, padx=30, fg="gray", bg="dark blue")



res_btn.pack()



root.mainloop()
