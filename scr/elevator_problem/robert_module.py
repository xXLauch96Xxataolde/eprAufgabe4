"""I

live here
"""

import elevator_problem.main_controller as main_controller
from elevator_problem.elevator import Elevator
import random
    
def better_floors(a_list):
    new_list = []
    for entry in a_list:
        if (entry[1] == "K"):    
            entry[1].replace("K","-1")
        elif (entry[1] == "E"):
            entry[1].replace("E","0")
        new_list.append(entry)
    print("new_list 2", new_list)
            
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
    
    joblist_a = better_floors(joblist_a)
    print(joblist_a)
    return (joblist_a, joblist_b , job_special)

def dispatcher(my_list, tic, elevator_a, elevator_b):
    set = [1, 2, 3]
        
    random.shuffle(set)
    tics_to_wait = set[0]
    
    joblist_a, joblist_b, job_special = job_sharer(my_list)
    curr_pos_a = elevator_a.get_level()
    curr_pos_b = elevator_b.get_level()
    
    while(True):
        curr_pos_a = elevator_a.get_level()
        curr_pos_b = elevator_b.get_level()
        inp = input()
        print("here")
        for entry in joblist_a:
            if (inp != False):
                if (curr_pos_a < int(entry[1])):
                    elevator_a.set_level(curr_pos_a + 1)
                    print("A", elevator_a.elevator_printer())
                    curr_pos_a = elevator_a.get_level()
                    break
def main():
    tic = 0
    #  my_list = main_controller.input_reader()
    my_list = ['A3', 'AK', 'B4', 'A4', 'AK', 'BE', 'Kh', '4h']
    elevator_a = Elevator("A", 0, "up")
    elevator_b = Elevator("B", 0, "up")
    dispatcher(my_list, tic, elevator_a, elevator_b)
        
