"""The XXX Function

This function is for testing purposes 
"""

import time

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 

import tkinter as Tkinter
import tkinter.ttk as ttk
import time


def test():

    root = Tkinter.Tk()
    
    ft = ttk.Frame()
    fb = ttk.Frame()
    
    ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
    fb.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
    
    elevator_bar = ttk.Progressbar(fb, orient='vertical', mode='indeterminate')
   
    elevator_bar.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.LEFT)

    elevator_bar.start(50)
    time.sleep(2)
    elevator_bar.step(40)
    time.sleep(2)
    elevator_bar.step(10)
    time.sleep(2)
    elevator_bar.step(10)

    root.mainloop()


if __name__ == '__main__':
    main()
