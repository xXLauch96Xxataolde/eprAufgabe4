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

def main_function():
    elevator_a= Elevator("A", 0, "up")
    elevator_b =Elevator("B", 0, "up")
    elevator_a.elevator_printer()
    elevator_b.elevator_printer()
    
    
    inp = int(input("Where the fuck do you want to travel?"))  # dangerous

    for i in range(inp):
        time.sleep(1)
        elevator_a.set_level(elevator_a.get_level()+1)  # i is teh greatest (faggot)
        elevator_a.elevator_printer()
    