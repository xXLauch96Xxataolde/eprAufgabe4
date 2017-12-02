from testing import TestingGui 
from tkinter import *
from tkinter.ttk import *
from elevator_problem import elevator

root = Tk()
my_gui = TestingGui(root)
root.mainloop()

def main():
    print("here")
    view = TestingGui(root)
    view.test("tralala")
        
    
if __name__ == '__main__':
    main()