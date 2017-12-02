from tkinter import *
from tkinter.ttk import *
import time

tk = Tk()
elevator_a = Progressbar(tk, orient=VERTICAL, length=100, mode='indeterminate')
elevator_a.pack(side="left", fill="both", expand=False, padx=4, pady=4)
elevator_b = Progressbar(tk, orient=VERTICAL, length=100, mode='indeterminate')
elevator_b.pack(side="left", fill='both', expand=False, padx=8, pady=4)
# help

def bar():
    for i in range(5):
        time.sleep(1)
        elevator_a_label.configure(text="Elevator A:" + str(i))
        tk.update_idletasks()
    tk.update_idletasks()
    elevator_a['value'] = 20
    tk.update_idletasks()
    time.sleep(1)
    elevator_a['value'] = 50
    tk.update_idletasks()
    time.sleep(1)
    elevator_a['value'] = 80
    tk.update_idletasks()
    time.sleep(1)
    elevator_a['value'] = 100


elevator_a_label = Label(tk, text="yddas")
elevator_a_label.pack()
image_left = PhotoImage(file='house_left.gif')

Button(tk, text="Start", command=bar).pack(side="bottom", fill='both', expand=False, padx=4, pady=2)

mainloop()
