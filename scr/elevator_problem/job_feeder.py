"""Job Feeder

Nomnomnom jobs
"""

import time
import random
import elevator
import main_controller

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


def better_floors(a_list):
    """Better Floors

    This function translates the K and E floors to -1 and 0 because it is
    more sensible to have them named that way
    """
    new_list = []
    for entry in a_list:
        """the conversion from e.g. Kh to -1h"""
        if (entry[0] == "K" and entry[1] == "r"):
            continue
        elif (entry[0] == "4" and entry[1] == "h"):
            continue
        elif (entry[0] == "K"):
            a = "-1" + entry[1]
            new_list.append(a)
        elif (entry[0] == "E"):
            a = "0" + entry[1]
            new_list.append(a)
        elif (entry[1] == "K"):
            a = entry[0] + "-1"
            new_list.append(a)
        elif (entry[1] == "E"):
            a = entry[0] + "0"
            new_list.append(a)
        else:
            new_list.append(entry)

    return (new_list)


def job_builder(elevator, jobs):
    """Job Builder
    
    Builds the List for commands inside the elevator if job is assigned to 
    current list
    """

    builded_jobs = []

    for job in jobs:
        print("JOB INFO, Len()", job, len(job), elevator.get_name())
        if len(job) != 0:
            if elevator.get_name() == job[0]:

                list = []

                if len(job) < 3:
                    destination = int(job[1])
                else:
                    destination = -1

                if elevator.get_level() > destination:
                    for lev in range(elevator.get_level(), destination - 1, -1):
                        list.append(lev)
                elif elevator.get_level() < destination:
                    for lev in range(elevator.get_level(), destination + 1):
                        list.append(lev)
                elif elevator.get_level() == destination:
                    list.append("same floor")
                    list = [destination]

                list.extend(level_stop(destination))

                builded_jobs.append(list)

                # jobs.remove(job)  # removes the converted jobs

    print("Built", builded_jobs)

    return builded_jobs


def spec_job_assigner(elevator, tic, jobs):
    """ Special Job Assigner
    
    assigns the converted jobs to specific job list
    """

    remaining_spec_jobs = []

    jobs = main_controller.delete_doubles(jobs)

    converted_jobs = job_builder(elevator, jobs)

    for job in converted_jobs:

        main_controller.elevator_setter(elevator, tic)
        elevator.elevator_printer(tic)

        counter = -1
        tic_plus_x = 0
        treffer = False

        job_direction = "none"

        if int(job[-1]) > elevator.get_level():
            job_direction = "up"

        elif int(job[-1]) < elevator.get_level():
            job_direction = "down"

        if elevator.get_direction() == job_direction or elevator.get_direction() == "none":  # only append the jobs that are in the same direction

            if elevator.spec_list[tic] == 10 and len(elevator.spec_list[tic:]) == 1:
                elevator.spec_list.extend(job[1:])
                continue

            for lev in job:
                counter += 1

                if tic_plus_x == len(elevator.spec_list[tic:]) and treffer is True:
                    elevator.spec_list.extend(job[counter:])
                    break

                if treffer is True and elevator.spec_list[tic + tic_plus_x] != lev:
                    for level in job[counter:]:
                        elevator.spec_list.insert(tic + tic_plus_x - 1, level)
                    break

                for spec_lev in elevator.spec_list[
                                tic + tic_plus_x:]:

                    print("Tic Level", spec_lev, tic_plus_x, len(elevator.spec_list[tic:]), treffer)
                    """[tic:] look at all levels after the current tic"""

                    if tic_plus_x - 1 == len(elevator.spec_list[tic:]) and treffer is True:
                        print("!!!", job[counter:])
                        break

                    if job[-1] == spec_lev:
                        try:
                            if job[-1] == elevator.spec_list[tic + tic_plus_x + 1]:
                                print("Job is already assigned.")
                                break
                        except IndexError:
                            print("Not in List")

                    if lev == spec_lev:
                        print("match")
                        treffer = True
                        tic_plus_x += 1
                        continue

                    elif treffer is True:
                        print("no match anymore check new element")
                        break

                    tic_plus_x += 1

                if tic_plus_x - 1 == len(elevator.spec_list[tic:]) and treffer is True:
                    elevator.spec_list.extend(job[counter:])
                    break

                try:
                    if job[-1] == spec_lev and job[-1] == elevator.spec_list[tic + tic_plus_x + 1]:
                        break
                except IndexError:
                    break

        else:
            print("Remaining")
            print(remaining_spec_jobs)
            print(job)

            if job[-1] == -1:
                rema_job = elevator.name + "-1"
            else:
                rema_job = elevator.name + str(job[-1])
            try:
                remaining_spec_jobs.remove(rema_job)
                print("deltet JOB")
            except ValueError:
                print("NOT A REMAINING JOB TO DELETE")
            remaining_spec_jobs.append(rema_job)  # save the remaining jobs

    print("REMIAING SPEC:", remaining_spec_jobs)
    return remaining_spec_jobs


def common_job_assigner(elevator, job, tic):
    """Common Job Assigner
    
    Commands from outside the elevator will be passed to the elevator here
    """
    print("Common Job Assigner", job)
    new_tic = -1
    match_number = 0
    direction = ""
    match = False

    elevator.elevator_printer(tic)
    """print both elevators"""

    infos = ""

    if elevator.spec_list[tic] == 10 and len(elevator.spec_list[tic:]) == 1:  # if no jobs left get people from floors
        if len(job) > 2:
            infos = abs(elevator.get_level() - (-1))
        else:
            infos = abs(elevator.get_level() - int(job[0]))
        return infos

    for lev in elevator.spec_list[tic:]:
        new_tic += 1
        if int(job[0]) == lev:
            print("elevator passes level")
            match = True

        if match is True:
            if elevator.get_level() > elevator.spec_list[tic + new_tic]:
                print("goes down")
                direction = "r"
            elif elevator.get_level() < elevator.spec_list[tic + new_tic]:
                print("goes up")
                direction = "h"

            if direction == job[1] and match is True:
                print("WE HAVE A MATCH")
                match_number += 1

                print(new_tic)
                return new_tic + 1
                # elevator.spec_list.insert(new_tic, level_stop(job[0]))

            else:
                break  # or evtl. break
    return "no match"
    # delete jobs after assigning them!!


def assign_common_stop(destination, elevator, match_tic, tic):
    """Assign a common stop
    
    I have no idea what niels printed here
    """
    list = []
    print("DESINATION:", destination)
    destination = int(destination)

    if elevator.get_level() > destination:
        list.append("r")
        for lev in range(elevator.get_level(), destination - 1, -1):
            list.append(lev)
    elif elevator.get_level() < destination:
        list.append("h")
        for lev in range(elevator.get_level(), destination + 1):
            list.append(lev)
    elif elevator.get_level() == destination:
        list.append("same floor")
        list = [destination]

    for level in level_stop(destination):
        list.insert(-1, level)

    if elevator.spec_list[tic] == 10 and len(elevator.spec_list[tic:]) == 1:
        print("Starts from start position.")
        elevator.spec_list.extend(list[2:])
    else:
        for level in level_stop(destination):
            # print(elevator.spec_list[tic:].index(destination), tic)
            elevator.spec_list.insert(elevator.spec_list[tic:].index(destination) + tic, level)
            # print(elevator.spec_list)


def level_stop(job):
    """Random Tic Generator

    Takes a destination and repeats it times the result of the tics the
    elevator should wait aka the random generator
    """

    waiting_tic = random.randint(1, 3)
    waiting_job_list = []
    for i in range(waiting_tic):
        waiting_job_list.append(job)

    return waiting_job_list
