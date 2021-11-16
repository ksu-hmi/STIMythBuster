import tkinter as tk

chlamydia_info =    """
    General Facts 
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

    Women
    Vaginal discharge and itching 
    Bleeding between periods 
    Painful sexual intercourse 

    Men
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
    Pelvic inflammatory disease (PID), infertility and ectopic pregnancy in women. 

    """

gonorrhea_info =    """ 
    ENTER TEXT HERE
    """

hpv_info =    """ 
    ENTER TEXT HERE
    """

syphilis_info =    """ 
    ENTER TEXT HERE
    """

trichomoniasis_info =    """ 
    ENTER TEXT HERE
    """

#ACTIONS
def click():
    print("Chlamydia")
    window = tk.Toplevel(main_window)
    window.title("Chlamydia Information")
    info = tk.Label(window, text=chlamydia_info, foreground="black")
    info.config(font=('Georgia', 12))
    info.grid(row=0, column=0, columnspan=3)


def click1():
    print("Gonorrhea")
    window = tk.Toplevel(main_window)
    window.title("Gonorrhea Information")
    info = tk.Label(window, text=gonorrhea_info, foreground="black")
    info.config(font=('Georgia', 12))
    info.grid(row=0, column=0, columnspan=3)

def click2():
    print("HPV")
    window = tk.Toplevel(main_window)
    window.title("HPV Information")
    info = tk.Label(window, text=hpv_info, foreground="black")
    info.config(font=('Georgia', 12))
    info.grid(row=0, column=0, columnspan=3)

def click3():
    print("Syphilis")
    window = tk.Toplevel(main_window)
    window.title("Syphilis Information")
    info = tk.Label(window, text=syphilis_info, foreground="black")
    info.config(font=('Georgia', 12))
    info.grid(row=0, column=0, columnspan=3)

def click4():
    print("Trichomoniasis")
    window = tk.Toplevel(main_window)
    window.title("Trichomoniasis Information")
    info = tk.Label(window, text=trichomoniasis_info, foreground="black")
    info.config(font=('Georgia', 12))
    info.grid(row=0, column=0, columnspan=3)


#SETUP
def click_setup():
    button1 = tk.Button(text='Chlamydia')
    button1.config(command=click) # performs call back of function
    button1.config(height = 5, width = 25)
    button1.config(font=('Georgia', 15, 'bold'))
    button1.config(bg='orange')
    button1.config(fg='white')
    button1.grid(row=0, column=0)
 

def click1_setup():
    button2 = tk.Button(text='Gonorrhea')
    button2.config(command=click1) # performs call back of function
    button2.config(height = 5, width = 25)
    button2.config(font=('Georgia', 15, 'bold'))
    button2.config(bg='#DE1F27')
    button2.config(fg='white')
    button2.grid(row=1, column=0)

def click2_setup():
    button3 = tk.Button(text='Human Papillomavirus')
    button3.config(command=click2) # performs call back of function
    button3.config(height = 5, width = 25)
    button3.config(font=('Georgia', 15, 'bold'))
    button3.config(bg='#B6DE1F')
    button3.config(fg='white')
    button3.grid(row=2, column=0)

def click3_setup():
    button4 = tk.Button(text='Syphilis')
    button4.config(command=click3) # performs call back of function
    button4.config(height = 5, width = 25)
    button4.config(font=('Georgia', 15, 'bold'))
    button4.config(bg='#D4DE1F')
    button4.config(fg='white')
    button4.grid(row=3, column=0)


def click4_setup():
    print("Trichomoniasis")
    button5 = tk.Button(text='Trichomoniasis')
    button5.config(command=click4) # performs call back of function
    button5.config(height = 5, width = 25)
    button5.config(font=('Georgia', 15, 'bold'))
    button5.config(bg='#1FDED6')
    button5.config(fg='white')
    button5.grid(row=4, column=0)


main_window = tk.Tk()
main_window.title("STI Educational Health App")

click_setup()
click1_setup()
click2_setup()
click3_setup()
click4_setup()

main_window.mainloop()