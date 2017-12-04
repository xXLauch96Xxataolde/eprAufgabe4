"""The Controler Function...

This module is meant for coordination purposes of the program, which is responsible for the normal elevator.
"""

import time
import re
import elevator
import job_feeder
import main

__author__ = "6785468: Robert am Wege, 6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


def non_valid_inp(requests, valid_inputs):
    """Non Valid Input

    We thought we wouldnt organise enough lists, so we added some more. The
    procedure prints all faulty inputs
    """
    non_valid_str = ""
    for entry in requests:
        if (entry not in valid_inputs):
            non_valid_str += entry + " "
            
    if (len(non_valid_str.strip()) == 0):
        return None
    else:
        list_a = non_valid_str.split()
        if (len(list_a) == 1):
            print("Unfortunately [", non_valid_str.strip(), "] is a faulty input.")
        else:
            print("Unfortunately [", non_valid_str.strip(), "] are faulty inputs.")

        print("Do you want to see our help file?")
        print("Type exit to go back to Menue")
        print("Then press 3")


def input_reader():
    """Input Reader
    
    This should interpret, check and parse an input.
    requests is an empty list for storing the split parts of the input string
    pattern_elevator and pattern_floor are the pattern for the regex. The 
    regex searches for matching patterns in a given string. if such a matching 
    string is found, a valid result object (search: matching object) is 
    constructed and the valid input is stored in a valid_inputs list
    """
    inp = input("Where do you want to travel?")

    if inp == "exit":
        print("\n"*2)
        main.main()

    requests = []
    valid_inputs = []
    requests = inp.split(" ")
    pattern_elevator = "[AB][KE1-4]"
    pattern_floor = "[KE1234][hr]"

    for entry in requests:
        result_elevator = re.match(pattern_elevator, entry)
        result_floor = re.match(pattern_floor, entry)
        if result_elevator or result_floor:
            valid_inputs.append(entry)

    valid_inputs = job_feeder.better_floors(valid_inputs)

    valid_inputs = delete_doubles(valid_inputs)

    non_valid_inp(requests, valid_inputs)

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


def tui_interface(elevator_a, elevator_b, tic):
    """TUI Interface

    This procedure writes an elevator object into a text-file.
    """

    list_a = ["K", "E", "1", "2", "3", "4"]
    list_b = ["-1", "0", "1", "2", "3", "4", ]
    list_res_a = []
    list_res_b = []

    for i in range(5, -1, -1):
        if (str(elevator_a.get_level()) == list_b[i]):
            list_res_a.append(str(list_a[i] + " [ x ]"))
        else:
            list_res_a.append(str(list_a[i] + " [   ]"))

        if (str(elevator_b.get_level()) == list_b[i]):
            list_res_b.append(str(list_a[i] + " [ x ]"))
        else:
            list_res_b.append(str(list_a[i] + " [   ]"))

    print("\n", "   A       B")

    i = 0
    for entry in list_res_a:
        print(list_res_a[i], list_res_b[i])
        i += 1
    print("\n")

    status_a = elevator_a.elevator_fileprinter(tic)
    status_b = elevator_b.elevator_fileprinter(tic)

    file = open("elevator_stages.txt", "w")
    file_excel = open("elevator_behaviour.txt", "a")

    file.writelines(status_a + "\n")
    file.writelines(status_b + "\n")

    file_excel.writelines(status_a + "\n")
    file_excel.writelines(status_b + "\n")

    file.close()


def delete_doubles(list):
    new_list = []
    for job in list:
        if job in new_list:
            continue
        else:
            new_list.append(job)
    return new_list


def main_function():
    """ Main Function()

    Dear Niels please insert a exit possiblity which leads the user to the
    main menue built in main.main()
    """
    tic = 0

    remaining_common_jobs = []
    remaining_spec_jobs = []

    elevator_a = elevator.Elevator("A", 0, "none", [10])
    elevator_b = elevator.Elevator("B", 0, "none", [10])

    remaining_jobs = []

    while True:
        print("Tic is:", tic)

        # sets the new attributes for our elevators
        elevator_setter(elevator_a, tic)
        elevator_setter(elevator_b, tic)

        tui_interface(elevator_a, elevator_b, tic)

        inp = input_reader()

        common_jobs, special_jobs = job_list_builder(inp)

        remaining_spec_jobs = delete_doubles(remaining_spec_jobs)
        for job in remaining_spec_jobs:
            special_jobs.extend(job)

        remaining_common_jobs = delete_doubles(remaining_common_jobs)
        common_jobs.extend(remaining_common_jobs)

        print("Common Jobs", common_jobs)
        common_jobs = delete_doubles(common_jobs)

        elevator_a.elevator_printer(tic)
        elevator_b.elevator_printer(tic)

        # special jobs are assigned here
        print(special_jobs)
        remaining_spec_jobs.append(job_feeder.spec_job_assigner(elevator_a, tic, special_jobs))
        remaining_spec_jobs.append(job_feeder.spec_job_assigner(elevator_b, tic, special_jobs))

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
                if inp[0] == "-1":
                    remaining_common_jobs.append("-1h")
                else:
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

        # elevator_a.elevator_printer(tic)
        # elevator_b.elevator_printer(tic)

        if len(elevator_b.spec_list[tic:]) == 1:
            elevator_b.spec_list.extend([10])
        if len(elevator_a.spec_list[tic:]) == 1:
            elevator_a.spec_list.extend([10])

        tic += 1
