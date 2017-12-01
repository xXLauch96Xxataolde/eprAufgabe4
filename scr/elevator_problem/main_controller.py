"""The Controler Function...

This module is meant for coordination purposes of the whole program. 
"""

import time
import gui_levitation
import re
import robert_module
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

    # print(valid_inputs)
    return valid_inputs


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
    tic = 0

    elevator_a = Elevator("A", 0, "none", [10])
    elevator_b = Elevator("B", 0, "none", [10])

    while True:
        inp = input_reader()

        # sets the new attributes for our elevators
        if elevator_a.spec_list[tic] != 10:
            elevator_a.set_level(elevator_a.spec_list[tic])
            try:
                if elevator_a.spec_list[tic] > elevator_a.spec_list[tic + 1]:
                    elevator_a.set_direction("down")
                elif elevator_a.spec_list[tic + 1] > elevator_a.spec_list[tic]:
                    elevator_a.set_direction("up")
                else:
                    elevator_a.set_direction("none")
            except IndexError:
                elevator_a.set_direction("none")

        if elevator_b.spec_list[tic] != 10:
            elevator_b.set_level(elevator_b.spec_list[tic])
            try:
                if elevator_b.get_level() > elevator_b.spec_list[tic + 1]:
                    elevator_b.set_direction("down")
                elif elevator_b.spec_list[tic + 1] > elevator_b.get_level():
                    elevator_b.set_direction("up")
                else:
                    elevator_b.set_direction("none")
            except IndexError:
                elevator_b.set_direction("none")

        common_jobs, special_jobs = job_list_builder(inp)

        # elevator_a.elevator_printer(tic)
        # elevator_b.elevator_printer(tic)

        # common jobs are assigned here
        for inp in common_jobs:
            distance_a = job_feeder.common_job_assigner(elevator_a, inp, tic)
            print("-----")
            distance_b = job_feeder.common_job_assigner(elevator_b, inp, tic)

            if distance_b == "no match" and distance_a == "no match":
                continue

            if distance_a == "no match":
                distance_a = 1000
            if distance_b == "no match":
                distance_b = 1000

            if elevator_b.spec_list[tic] != 10 and elevator_a.spec_list[tic] != 10:
                if distance_a > distance_b:
                    job_feeder.assign_common_stop(inp[0], elevator_b, distance_b, tic)
                    print("assigned to b", distance_b)
                else:
                    job_feeder.assign_common_stop(inp[0], elevator_a, distance_a, tic)
                    print("assigned to a", distance_a)

            elif elevator_a.spec_list[tic] == 10 and len(elevator_a.spec_list[tic:]) == 1:
                job_feeder.assign_common_stop(inp[0], elevator_a, distance_a, tic)

            elif elevator_b.spec_list[tic] == 10 and len(elevator_b.spec_list[tic:]) == 1:
                job_feeder.assign_common_stop(inp[0], elevator_b, distance_b, tic)

        # special jobs are assigned here
        print(special_jobs)
        job_feeder.spec_job_assigner(elevator_a, tic, special_jobs)
        job_feeder.spec_job_assigner(elevator_b, tic, special_jobs)


        elevator_a.elevator_printer(tic)
        elevator_b.elevator_printer(tic)

        if len(elevator_b.spec_list[tic:]) == 1:
            elevator_b.spec_list.extend([10])
        if len(elevator_a.spec_list[tic:]) == 1:
            elevator_a.spec_list.extend([10])
        # after every tic or return, we want to assign the jobs!

        tic += 1
