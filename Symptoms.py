import tkinter as tk

def click_me():
    print(var1.get())
    print(var2.get())
    print(var3.get())
    print(var4.get())
    print(var5.get())
    print(var6.get())
    print(var7.get())
    print(var8.get())
 
window = tk.Tk()
window.title('STIMythBuster')
window.geometry('400x400')
 
l = tk.Label(window, width=60, text='Select all symptoms that apply:')
l.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Bleeding', variable=var1, onvalue=1, offvalue=0)
c1.pack()
c2 = tk.Checkbutton(window, text='Burning sensation when urinating', variable=var2, onvalue=1, offvalue=0)
c2.pack()
c3 = tk.Checkbutton(window, text='Painful bowel movements', variable=var3, onvalue=1, offvalue=0)
c3.pack() 
c4 = tk.Checkbutton(window, text='Soreness', variable=var4, onvalue=1, offvalue=0)
c4.pack() 
c5 = tk.Checkbutton(window, text='Single or Multiple sores', variable=var5, onvalue=1, offvalue=0)
c5.pack() 
c6 = tk.Checkbutton(window, text='Skin rash', variable=var6, onvalue=1, offvalue=0)
c6.pack() 
c7 = tk.Checkbutton(window, text='Mucous membrane lesions', variable=var7, onvalue=1, offvalue=0)
c7.pack() 
c8 = tk.Checkbutton(window, text='Itching or irritation', variable=var8, onvalue=1, offvalue=0)
c8.pack() 

b = tk.Button(window,text="Click here",command=click_me)
b.pack()

window.mainloop()



