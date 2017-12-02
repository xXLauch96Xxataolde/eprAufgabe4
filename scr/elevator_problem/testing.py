from tkinter import *
from tkinter.ttk import *
from elevator_problem import elevator


class TestingGui:

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Lets see!")
        self.label.pack()
        
        self.elevator_a = Progressbar(master, orient=VERTICAL, length=100, mode='indeterminate')
        self.elevator_a.pack(side="left", fill="x", expand=False, padx=8, pady=4)

        self.greet_button = Button(master, text="Next Tic", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Exit", command=master.quit)
        self.close_button.pack()

    def test(self, a):
        print(a)

    def greet(self):
        print("Hallo!")
        self.master.update_idletasks()
        self.elevator_a['value'] += -20 
        
        
        

