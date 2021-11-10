# [] create The Weather
# [] copy and paste in edX assignment page

import os
cmd ="curl https://www.cdc.gov/std/Gonorrhea -o mean_temp.txt"
os.system(cmd)



button2 = Button(window, text='Gonorrhea')
button2.config(command=click1) # performs call back of function
button2.config(font=('Georgia', 50, 'bold'))
button2.config(bg='#DE1F27')
button2.config(fg='white')
button2.grid(row=1, column=0)



