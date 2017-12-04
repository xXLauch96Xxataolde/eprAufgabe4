import tkinter as tk
import tkinter.ttk as ttk
import elevator
import main
import time


class Model():

    def __init__(self):
        print("")
        
    def get_pos(self):
        self.elevator
        

class View():

    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.progress_bar = ttk.Progressbar(orient=tk.VERTICAL,
                                                mode='indeterminate',
                                                takefocus=True)
        self.progress_bar.pack()


class Controller():

    def __init__(self):        
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        
    def run(self):        
        self.root.title("Elevator Problem")
        self.root.mainloop()
