"""The Controler Function

This module is meant for coordination purposes of the whole program. 
"""

import time
import elevator_problem.gui_levitation as gui_levitation
import re
from elevator_problem.elevator import Elevator

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 


def prio_list():
    """Maybe we can implement a priolist here"""

def input_reader():
    """This should interpret, check and parse an input"""
    inp = input("Where do you want to travel?")
    
    requests = []  # this should store all inputs.
    valid_inputs = [] 
    requests = inp.split(" ")
    pattern_elevator = "[AB][KE1-4]"
    pattern_floor = "[KE1234][hr]"
    
    #  A3 AK AZ A78 A778 V5 B4 b2 A5 A4 Ae AK BE Be bE K1 kh 3R Kh 4h 6H k6 h$ for convenience 
    
    for entry in requests:        
        result_elevator = re.match(pattern_elevator, entry)
        result_floor = re.match(pattern_floor, entry)
        if result_elevator or result_floor:
            valid_inputs.append(entry)
    
    print(valid_inputs)
    return inp

def main_function():
    tic = 0
    elevator_a = Elevator("A", 0, "up")
    elevator_b = Elevator("B", 0, "up")
    elevator_a.elevator_printer()
    elevator_b.elevator_printer()
    
    
    inp = input_reader()
        
