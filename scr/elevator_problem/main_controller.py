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
    
    elevator_a.set_level(3)
    elevator_a.elevator_printer()
    