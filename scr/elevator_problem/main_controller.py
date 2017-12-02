"""The Controler Function...

This module is meant for coordination purposes of the whole program. 
"""

import time
import re
from elevator import Elevator
import job_feeder

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


def prio_list():
    """Maybe we can implement a priolist here"""


def input_reader():
    """This should interpret, check and parse an input.
    
    requests is an empty list for storing the split parts of the input string
    pattern_elevator and pattern_floor are the pattern for the regex. The 
    regex searches for matching patterns in a given string. if such a matching 
    string is found, a valid result object (search: matching object) is 
    constructed and the valid input is stored in a valid_inputs list
    """
    inp = input("Where do you want to travel?")

    requests = []
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

    valid_inputs = job_feeder.better_floors(valid_inputs)

    return valid_inputs


def elevator_setter(elevator, tic):
    
    if elevator.spec_list[tic] != 10:
        elevator.set_level(elevator.spec_list[tic])
        try:
            if elevator.get_level() > elevator.spec_list[-1]:
                elevator.set_direction("down")
            elif elevator.spec_list[-1] > elevator.get_level():
                elevator.set_direction("up")
            else:
                elevator.set_direction("none")
        except IndexError:
            elevator.set_direction("none")
    elif elevator.spec_list[tic] == 10 and len(elevator.spec_list[tic:]) > 1:
        if elevator.get_level() > elevator.spec_list[-1]:
            elevator.set_direction("down")
        elif elevator.spec_list[-1] > elevator.get_level():
            elevator.set_direction("up")
        else:
            elevator.set_direction("none")
    else:
        elevator.set_direction("none")


def job_list_builder(inp):
    common_list = []
    special_list = []
    for job in inp:
        if job[0].isdigit():
            print("Found a common job.")
            common_list.append(job)
        else:
            special_list.append(job)
    return common_list, special_list


def main_function():
    """ Main Function()
    
    Dear Niels please insert a exit possiblity which leads the user to the
    main menue built in main.main()
    """
    tic = 0

    elevator_a = Elevator("A", 0, "none", [10])
    elevator_b = Elevator("B", 0, "none", [10])

    remaining_jobs = []

    while True:
        """
        Maybe you can here check the input. 
        inp = input()
        if (inp = "exit"):
            break;
        else:
            continue with your main function
        
        Thx
        """
        inp = input_reader()

        # sets the new attributes for our elevators
        elevator_setter(elevator_a, tic)
        elevator_setter(elevator_b, tic)

        common_jobs, special_jobs = job_list_builder(inp)

        elevator_a.elevator_printer(tic)
        elevator_b.elevator_printer(tic)

        # special jobs are assigned here
        print(special_jobs)
        job_feeder.spec_job_assigner(elevator_a, tic, special_jobs)
        job_feeder.spec_job_assigner(elevator_b, tic, special_jobs)

        # common jobs are assigned here
        for inp in common_jobs:
            distance_a = job_feeder.common_job_assigner(elevator_a, inp, tic)
            print("Distance: ", distance_a)
            print("---!!--")
            distance_b = job_feeder.common_job_assigner(elevator_b, inp, tic)
            print("Distance: ", distance_b)

            if distance_b == "no match" and distance_a == "no match":
                continue

            if distance_a == "no match":
                distance_a = 1000
            if distance_b == "no match":
                distance_b = 1000

            if len(elevator_b.spec_list[tic:]) > 1 and len(elevator_a.spec_list[tic:]) > 1:
                if distance_a > distance_b:
                    job_feeder.assign_common_stop(inp[0], elevator_b, distance_b, tic)
                    print("assigned to b", distance_b)
                else:
                    job_feeder.assign_common_stop(inp[0], elevator_a, distance_a, tic)
                    print("assigned to a", distance_a)

            elif elevator_a.spec_list[tic] == 10 and len(elevator_a.spec_list[tic:]) == 1:
                print("assssssssssssss to a ")
                job_feeder.assign_common_stop(inp[0], elevator_a, distance_a, tic)

            elif elevator_b.spec_list[tic] == 10 and len(elevator_b.spec_list[tic:]) == 1:
                print("assssssss to b")
                job_feeder.assign_common_stop(inp[0], elevator_b, distance_b, tic)

        elevator_a.elevator_printer(tic)
        elevator_b.elevator_printer(tic)

        if len(elevator_b.spec_list[tic:]) == 1:
            elevator_b.spec_list.extend([10])
        if len(elevator_a.spec_list[tic:]) == 1:
            elevator_a.spec_list.extend([10])
        # after every tic or return, we want to assign the jobs!

        tic += 1
