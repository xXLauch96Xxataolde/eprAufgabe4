"""The Controler Function

This module is meant for coordination purposes of the whole program. 
"""

import time
import elevator_problem.gui_levitation as gui_levitation
from elevator_problem.elevator import Elevator

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 


def prio_list():
    """Maybe we can implement a priolist here"""

def input_reader():
    """This retarded piece of retardness should interpret, check and parse an input"""
    inp = input("Where the fuck do you want to travel?")
    
    requests = []  # this should store all inputs. 
    requests.append(inp.split(" "))
    for i in requests:  # here the length of the input parts is tested
        if (len(i) != 2):
            print("ERROR")  # here an ERROR Code should be returned
        
    return inp

def main_function():
    tic = 0
    elevator_a = Elevator("A", 0, "up")
    elevator_b = Elevator("B", 0, "up")
    elevator_a.elevator_printer()
    elevator_b.elevator_printer()
    
    
    inp = input_reader()
    
    while(True):
        print("Tic:", tic)
        for i in range(inp):
            time.sleep(1)
            elevator_a.set_level(elevator_a.get_level() + 1)
            elevator_a.elevator_printer()
        tic += 1 
    