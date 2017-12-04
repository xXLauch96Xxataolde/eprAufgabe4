import tkinter as tk
import tkinter.ttk as ttk
import tkinter as tk 

class Controller():
    def __init__(self):
        root = tk.Tk()
        
        self.label = tk.Label(root, text="sdfsd").pack()
        
        root.mainloop()

if __name__ == '__main__':
    c = Controller()
    c.run()
