# [] create The link to HPV facts

import os
cmd ="curl https://www.cdc.gov/std/treatment-guidelines/hpv-cancer.htm -o mean_temp.txt"
os.system(cmd)


def click2():
    print("Human Papillomavirus!")
button3 = Button(window, text='Human Papillomavirus')
button3.config(command=click2) # performs call back of function
button3.config(font=('Georgia', 40, 'bold'))
button3.config(bg='#B6DE1F')
button3.config(fg='white')
button3.grid(row=2, column=0)