import tkinter as tk
import tkinter.ttk as ttk
import time

class Gui:
    def fun(self, a):
        for i in range(500):
            time.sleep(1)
            f = open("elevator_stages.txt", "r")
            print(f.read())
            print(a)
            a = 40
            self.progress.after(500, self.fun(a))
    
    def callback(self):          
        a = 0
        self.fun(a)
        
        
    def __init__(self):
        root = tk.Tk()        
        self.label = tk.Label(root, text="Elevator")
        self.label.pack()
        self.button = tk.Button(root, text="", command=self.callback)
        self.button.pack()
        self.progress = ttk.Progressbar(root, orient="vertical",
                                        length=100, mode="indeterminate")
        self.progress.pack()
        root.mainloop()
    

if __name__ == '__main__':
    c = Gui()
    
