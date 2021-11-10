# [] create The link to Chlamydia facts


import os
cmd ="curl https://www.cdc.gov/std/Chlamydia -o mean_temp.txt"
os.system(cmd)


button1 = Button(window, text='Chlamydia')
button1.config(command=click) # performs call back of function
button1.config(font=('Georgia', 50, 'bold'))
button1.config(bg='orange')
button1.config(fg='white')
button1.grid(row=0, column=0)

def click1():
    print("Chlamydia")