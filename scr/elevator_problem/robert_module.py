"""I

live here
"""

import elevator_problem.main_controller as main_controller
from elevator_problem.elevator import Elevator
import random
    

def job_sharer(my_list):
    """ Job Sharer.
    
    Takes all jobs, dispatches them to the elevator job lists and a special
    job list
    """
    joblist_a = []
    joblist_b = []
    job_special = []
    
    for entry in my_list:
        if (entry[0] == 'A'):
            joblist_a.append(entry)
        elif (entry[0] == 'B'):
            joblist_b.append(entry)
        else:    
            job_special.append(entry)
    
    print("list a:", joblist_a)
    print("list b:", joblist_b)
    print("list spec:", job_special)
    
    return (joblist_a, joblist_b , job_special)

def dispatcher(my_list, tic, elevator_a, elevator_b):
    set = [1, 2, 3]
        
    random.shuffle(set)
    tics_to_wait = set[0]
    
    joblist_a, joblist_b, job_special = job_sharer(my_list)
    curr_pos_a = elevator_a.level
    curr_pos_b = elevator_b.level
    
    
def main():
    tic = 0
    #  my_list = main_controller.input_reader()
    my_list = ['A3', 'AK', 'B4', 'A4', 'AK', 'BE', 'Kh', '4h']
    elevator_a = Elevator("A", 0, "up")
    elevator_b = Elevator("B", 0, "up")
    dispatcher(my_list, tic, elevator_a, elevator_b)
        