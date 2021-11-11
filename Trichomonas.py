# [] create The link to Trichomoniasis facts

import os
cmd ="curl https://www.cdc.gov/std/trichomonas -o mean_temp.txt"
os.system(cmd)


def click3():
    print("Trichomonas")

button4 = Button(window, text='Trichomonas')
button4.config(command=click3) # performs call back of function
button4.config(font=('Georgia', 50, 'bold'))
button4.config(bg='#D4DE1F')
button4.config(fg='white')
button4.grid(row=3, column=0)