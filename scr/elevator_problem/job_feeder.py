"""
Created on 27.11.2017

@author: Niels Heissel
"""

import time
import random
import elevator
import main_controller

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"

job_liste = ['1h', '3r']
remaining_spec_jobs = []


def better_floors(a_list):
    # print("Teh list", a_list)
    """Better Floors

    This function translates the K and E floors to -1 and 0 because it is
    more sensible to have them named that way
    """
    new_list = []
    for entry in a_list:
        """the conversion from e.g. Kh to -1h"""
        if (entry[0] == "K"):
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

    # print("here", new_list)
    return (new_list)


def job_builder(elevator, jobs):
    # '''Builds the List for commands inside the elevator if job is assigned to current list'''

    builded_jobs = []

    for job in jobs:
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

    # print(builded_jobs)

    return builded_jobs


def spec_job_assigner(elevator, tic, jobs):
    """assigns the converted jobs to specific job list"""
    jobs.extend(remaining_spec_jobs)
    print("#####", jobs)
    converted_jobs = job_builder(elevator, jobs)

    print("------", converted_jobs)

    for job in converted_jobs:

        main_controller.elevator_setter(elevator, tic)
        elevator.elevator_printer(tic)

        counter = -1
        tic_plus_x = 0;
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

            for lev in job[1:]:
                counter += 1

                if tic_plus_x == len(elevator.spec_list[tic:]) and treffer is True:
                    elevator.spec_list.extend(job[counter:])
                    break

                if treffer is True and elevator.spec_list[tic + tic_plus_x] != lev:
                    for level in job[counter:]:
                        elevator.spec_list.insert(tic + tic_plus_x - 1, level)
                    break

                for spec_lev in elevator.spec_list[
                                tic + tic_plus_x:]:  # [tic:] bedeutet schaue dir alle levels nach dem aktuellen tic an



                    if job[-1] == spec_lev:
                        if job[-1] == elevator.spec_list[tic + tic_plus_x + 1]:
                            print("Job is already assigned.")
                            break

                    if tic_plus_x == len(elevator.spec_list[tic:]) and treffer is True:
                        print("!!!", job[counter:])
                        elevator.spec_list.extend(job[counter:])
                        break

                    if lev == spec_lev:
                        print("match")
                        treffer = True
                        tic_plus_x += 1
                        continue

                    elif treffer is True:
                        print("no match anymore check new element")
                        break

                    tic_plus_x += 1

            if job[-1] == spec_lev and job[-1] == elevator.spec_list[tic + tic_plus_x + 1]:
                break

            if tic_plus_x == len(elevator.spec_list[tic:]) and treffer is True:
                break

                # if treffer is True:
                # elevator.spec_list.extend(job[tic_plus_x - 1:])

        else:
            print("Remaining")
            if job[-1] == -1:
                rema_job = elevator.name + "-1"
            else:
                rema_job = elevator.name + str(job[-1])
            remaining_spec_jobs.append(rema_job)  # save the remaining jobs
    print(remaining_spec_jobs)


def common_job_assigner(elevator, job, tic):
    '''commands from outside the elevator will be passed to the elevator here'''
    print("Common Job Assigner", job)
    new_tic = -1
    match_number = 0
    direction = ""
    match = False

    # for both elevators ...

    infos = ""

    if elevator.spec_list[tic] == 10 and len(elevator.spec_list[tic:]) == 1:  # if no jobs left get people from floors
        infos = abs(elevator.get_level() - int(job[0]))
        return infos

    for lev in elevator.spec_list[tic:]:
        new_tic += 1
        if int(job[0]) == lev:
            print("elevator passes level")
            match = True

        if match is True:
            print("Liste von Außen", elevator.spec_list, "Tic:", tic, "New_tic:", new_tic)
            if elevator.spec_list[tic + new_tic - 1] > elevator.spec_list[tic + new_tic]:
                print("goes down")
                direction = "r"
            elif elevator.spec_list[tic + new_tic] < elevator.spec_list[tic + new_tic + 1]:
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
    list = []
    destination = int(destination)

    print(elevator.get_level())

    if elevator.get_level() > destination:
        list.append("r")
        for lev in range(elevator.get_level(), destination - 1, -1):
            list.append(lev)
    elif elevator.get_level() < destination:
        list.append("h")
        for lev in range(elevator.get_level(), destination + 1):
            print(lev)
            list.append(lev)
    elif elevator.get_level() == destination:
        list.append("same floor")
        list = [destination]

    for level in level_stop(destination):
        list.insert(-1, level)

    print(list)

    if elevator.spec_list[tic] == 10 and len(elevator.spec_list[tic:]) == 1:
        print("Starts from start position.")
        elevator.spec_list.extend(list[2:])
    else:
        for level in list[2:]:
            print("----- ", level)
            print(match_tic)
            elevator.spec_list.insert(tic + match_tic, level)


def level_stop(job):
    '''Random Tic Generator

    Takes a destination and repeats it times the result of the tics the
    elevator should wait aka the random generator
    '''

    waiting_tic = random.randint(1, 3)
    waiting_job_list = []
    for i in range(waiting_tic):
        waiting_job_list.append(job)

    return waiting_job_list
