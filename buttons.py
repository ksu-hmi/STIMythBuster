from tkinter import *

def click():
    print("""General Facts 

A common sexually transmitted infection caused by the bacteria Chlamydia trachomatis.  

The infection is transmitted through vaginal, oral, and anal unprotected sex. 

It can be passed on from an infected mother to the child during childbirth. 

Chlamydia eye infection can occur through genital contact with the eyes. 

Risk Factors 

Having multiple partners. 

Unprotected sex. 

History of STI. 

Symptoms 

Usually, no symptoms during the initial stages of infection. 

Women: 

Vaginal discharge and itching 

Bleeding between periods 

Painful sexual intercourse 

Men: 

Pain and swelling in testicles 

Discharge from penis 

Diagnosis 

Urine culture for men. 

Swab test of cervix for women. 
Treatment 

Antibiotics to kill bacteria such as Azithromycin or Doxycycline. 

Specialist to consult 

OB GYN 

Urologist 

If left untreated: 

Pelvic inflammatory disease (PID), infertility and ectopic pregnancy in women.""")

 
 
 
 



 

window = Tk()
button1 = Button(window, text='Chlamydia')
button1.config(command=click) # performs call back of function
button1.config(height=2, width=15)
button1.config(font=('Comic Sans', 30, 'bold'))
button1.config(bg='#DE1F37')
button1.config(fg='white')
button1.grid(row=0, column=0)

def click1():
    print("""Gonorrhea 

A sexually transmitted bacterial infection caused by the bacteria Neisseria gonorrhea. It often affects the urethra, rectum, or throat. 

Symptoms: 

Men: 

Frequent urination 

Puss-like discharge from the penis 

Swelling or pain in the testicle 

Persistent sore throat 

Women: 

Discharge from the vagina 

Pain or burning sensation while urinating 

Heavier periods or spotting 

Pain during sexual intercourse 

Sharp pain in the lower abdomen 

Sore throat, fever 

Causes: 

It is caused by the bacterium Neisseria gonorrhea. 

Affects the mouth, throat, eyes, rectum and female reproductive tract. 

It spreads through unprotected sex. 

Can be passed from an infected mother to her baby during delivery. 

Prevention: 

Stay away from unprotected sex  

Always use a condom 

Get tested if suspicious of infection 

Complications: 

Pelvic inflammatory disease in women (PID) 

Blockage or scarring of fallopian tubes 

Scarring in the urethra in men 

Ectopic pregnancy 

Painful abscess may develop in the interior of the penis. 

Diagnosis: 

Swab test: a sample is collected either from the genitals or mouth and tested for the presence of bacteria. 

Treatment: 
Antibiotics to kill the bacteria such as Ceftriaxone and Azithromycin 

Self-care Strategies: 

Avoid sexual intercourse during the treatment period. 

Specialist to Consult: 

Gynecologist 

Urologist 

""")

button2 = Button(window, text='Gonorrhea')
button2.config(command=click1) # performs call back of function
button2.config(height=2, width=15)
button2.config(font=('Comic Sans', 30, 'bold'))
button2.config(bg='#1FDEC6')
button2.config(fg='white')
button2.grid(row=1, column=0)


def click2():
    print("Hello World!")
button3 = Button(window, text='HPV')
button3.config(command=click2) # performs call back of function
button3.config(height=2, width=15)
button3.config(font=('Comic Sans', 30, 'bold'))
button3.config(bg='#DE1F37')
button3.config(fg='white')
button3.grid(row=2, column=0)

def click3():
    print("Syphilis")

button4 = Button(window, text='Syphilis')
button4.config(command=click3) # performs call back of function
button4.config(height=2, width=15)
button4.config(font=('Comic Sans', 30, 'bold'))
button4.config(bg='#1FDEC6')
button4.config(fg='white')
button4.grid(row=3, column=0)

def click4():
    print("trichomoniasis")



button5 = Button(window, text='Trichomoniasis')
button5.config(command=click4) # performs call back of function
button5.config(height=2, width=15)
button5.config(font=('Comic Sans', 30, 'bold'))
button5.config(bg='#DE1F37')
button5.config(fg='white')
button5.grid(row=4, column=0)


window.mainloop()



