"""The Test Function

This function is for testing purposes 
important video: https://www.youtube.com/watch?v=h3Yrhv33Zb8
"""

import time

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 

import tkinter as Tkinter
import tkinter.ttk as ttk
import time


def ele_move(step, elevator_bar):
    for i in range(20):
        time.sleep(0.1)
        elevator_bar.step(step)
        elevator_bar.update()


def lvl(level):
    dict = {-1: "Basement",
            0: "Ground Floor",
            1 : "1",
            2 : "2",
            3 : "3",
            4 : "4",
            }
    print("Elevator Level:", dict.get(level))


def test1():
    level = 0
    root = Tkinter.Tk()
    
    ft = ttk.Frame()
    fb = ttk.Frame()
    
    ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
    fb.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
    
    elevator_bar = ttk.Progressbar(fb, orient='vertical', mode='indeterminate', value=100)
   
    elevator_bar.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.LEFT)

    elevator_bar.update()
    
    while(True):
        # elevator_bar.step(0)
        # elevator_bar.update()
        inp = input()
        if(inp == "up"):
            ele_move(1, elevator_bar)
            level += 1
            lvl(level)
        elif(inp == "down"):
            ele_move(-1, elevator_bar)
            level -= 1
            lvl(level)

    root.mainloop()


if __name__ == '__main__':
    main()
