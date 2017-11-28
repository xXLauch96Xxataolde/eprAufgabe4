"""I

live here
"""

import elevator_problem.main_controller as main_controller
from elevator_problem.elevator import Elevator
import random
    
def dispatcher(my_list):
    #  dasdasd
    set = [1, 2, 3]
    random.shuffle(set)
    tics_to_wait = set[0]
    print("hallo")
    
def main():
    #  my_list = main_controller.input_reader()
    my_list = ['A3', 'AK', 'B4', 'A4', 'AK', 'BE', 'Kh', '4h']
    elevator_a = Elevator("A", 0, "up")
    elevator_b = Elevator("B", 0, "up")
    dispatcher(my_list)
        