import tkinter as tk

window = tk.Tk()
window.title('STIMythBuster')
window.geometry('400x400')
 
l = tk.Label(window, width=20, text='Select all symptoms that apply:')
l.pack()
 
var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Bleeding', onvalue=1, offvalue=0)
c1.pack()
c2 = tk.Checkbutton(window, text='Burning sensation when urinating', onvalue=1, offvalue=0)
c2.pack()
c3 = tk.Checkbutton(window, text='Painful bowel movements', onvalue=1, offvalue=0)
c3.pack() 
c4 = tk.Checkbutton(window, text='Soreness', onvalue=1, offvalue=0)
c4.pack() 
c5 = tk.Checkbutton(window, text='Single or Multiple sores', onvalue=1, offvalue=0)
c5.pack() 
c6 = tk.Checkbutton(window, text='Skin rash', onvalue=1, offvalue=0)
c6.pack() 
c7 = tk.Checkbutton(window, text='Mucous membrane lesions', onvalue=1, offvalue=0)
c7.pack() 
c8 = tk.Checkbutton(window, text='Itching or irritation', onvalue=1, offvalue=0)
c8.pack() 

window.mainloop()

def click_me():
    print(i.get())
 
b = Button(root,text="Click here",command=click_me)
b.pack()


