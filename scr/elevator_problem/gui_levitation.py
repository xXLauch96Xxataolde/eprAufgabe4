"""Gui Levitation

This function provides the wanted visualization of the elevators. 
A little poorly executed but maybe we get there
"""
from tkinter import *
from tkinter.ttk import *
import time

tk = Tk()
image_left = PhotoImage(file='abc.gif')
image_right = PhotoImage(file='cba.gif')
label_house = Label(tk, image=image_left)
label_house.pack(side="left", fill="x", expand="True")
label_house2 = Label(tk, image=image_right)
label_house2.pack(side="right", fill="x", expand="True")
elevator_a = Progressbar(tk, orient=VERTICAL, length=100, mode='indeterminate')
elevator_a.pack(side="left", fill="x", expand=False, padx=8, pady=4)
elevator_b = Progressbar(tk, orient=VERTICAL, length=100, mode='indeterminate')
elevator_b.pack(side="left", fill='x', expand=False, padx=8, pady=4)
# help


def bar():
    for i in range(5):
        time.sleep(1)
        elevator_a_label.configure(text="Elevator A:" + str(i))
        tk.update_idletasks()
    
    tk.update_idletasks()
    elevator_a['value'] = 20  
    time.sleep(1) 

elevator_a_label = Label(tk, text="yddas")
elevator_a_label.pack()

Button(tk, text="Start", command=bar).pack(side="bottom", fill='both', expand=False, padx=4, pady=2)

mainloop()
