"""The Controler Function...

This module is meant for coordination purposes of the program, which is responsible for the normal elevator.
"""

import time
import re
from elevator import Elevator
import job_feeder
import main
from gui_levitation import Controller

__author__ = "6785468: Robert am Wege, 6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"

remaining_common_jobs = []


def input_reader():
    """This should interpret, check and parse an input.
    
    requests is an empty list for storing the split parts of the input string
    pattern_elevator and pattern_floor are the pattern for the regex. The 
    regex searches for matching patterns in a given string. if such a matching 
    string is found, a valid result object (search: matching object) is 
    constructed and the valid input is stored in a valid_inputs list

    To do: Wrong-input message. 
    """
    inp = input("Where do you want to travel?")

    if inp == "exit":
        main.main()

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

    valid_inputs = list(set(valid_inputs))

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
        elif job[0] == "-":
            print("Found a common job.")
            common_list.append(job)
        else:
            special_list.append(job)
    return common_list, special_list


def gui_interface(elevator_a, elevator_b,  tic):
    """GUI Interface

    This procedure writes an elevator object into a text-file.
    """
    status_a = elevator_a.elevator_fileprinter(tic)
    status_b = elevator_b.elevator_fileprinter(tic)
    
    file = open("elevator_stages.txt", "w")
    file_excel = open("elevator_behaviour.txt", "a")

    file.writelines(status_a + "\n")
    file.writelines(status_b + "\n")
    
    file_excel.writelines(status_a + "\n")
    file_excel.writelines(status_b + "\n")


    file.close()


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
        print("Tic is:", tic)

        gui_interface(elevator_a, elevator_b, tic)

        # mongo function

        inp = input_reader()

        # sets the new attributes for our elevators
        elevator_setter(elevator_a, tic)
        elevator_setter(elevator_b, tic)

        common_jobs, special_jobs = job_list_builder(inp)

        common_jobs.extend(remaining_common_jobs)

        print(common_jobs)
        common_jobs = list(set(common_jobs))

        elevator_a.elevator_printer(tic)
        elevator_b.elevator_printer(tic)

        # special jobs are assigned here
        print(special_jobs)
        job_feeder.spec_job_assigner(elevator_a, tic, special_jobs)
        job_feeder.spec_job_assigner(elevator_b, tic, special_jobs)

        print("REMAINING COMMON JOBS", remaining_common_jobs)
        print("Common", common_jobs)

        # common jobs are assigned here
        for inp in common_jobs:
            if len(inp) > 2:
                inp = [inp[0:2], inp[2]]

            print("Input:", inp)

            distance_a = job_feeder.common_job_assigner(elevator_a, inp, tic)
            print("Distance: ", distance_a)
            print("---!!--")
            distance_b = job_feeder.common_job_assigner(elevator_b, inp, tic)
            print("Distance: ", distance_b)

            if distance_b == "no match" and distance_a == "no match":
                remaining_common_jobs.append(inp)
                continue

            if distance_a == "no match":
                distance_a = 1000
            if distance_b == "no match":
                distance_b = 1000

            if len(elevator_b.spec_list[tic:]) > 1 and len(elevator_a.spec_list[tic:]) > 1:
                if distance_a > distance_b:
                    job_feeder.assign_common_stop(inp[0], elevator_b, distance_b, tic)
                    print("assigned to b", distance_b)
                    try:
                        remaining_common_jobs.remove(inp)
                    except ValueError:
                        continue
                else:
                    job_feeder.assign_common_stop(inp[0], elevator_a, distance_a, tic)
                    print("assigned to a", distance_a)
                    try:
                        remaining_common_jobs.remove(inp)
                    except ValueError:
                        continue

            elif elevator_a.spec_list[tic] == 10 and len(elevator_a.spec_list[tic:]) == 1:
                print("assssssssssssss to a ")
                job_feeder.assign_common_stop(inp[0], elevator_a, distance_a, tic)
                try:
                    remaining_common_jobs.remove(inp)
                except ValueError:
                    continue

            elif elevator_b.spec_list[tic] == 10 and len(elevator_b.spec_list[tic:]) == 1:
                print("assssssss to b")
                job_feeder.assign_common_stop(inp[0], elevator_b, distance_b, tic)
                try:
                    remaining_common_jobs.remove(inp)
                except ValueError:
                    continue

        elevator_a.elevator_printer(tic)
        elevator_b.elevator_printer(tic)

        if len(elevator_b.spec_list[tic:]) == 1:
            elevator_b.spec_list.extend([10])
        if len(elevator_a.spec_list[tic:]) == 1:
            elevator_a.spec_list.extend([10])

        tic += 1
