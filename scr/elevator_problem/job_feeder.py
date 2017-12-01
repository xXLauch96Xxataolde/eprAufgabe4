'''
Created on 27.11.2017

@author: Niels
'''

import time
import random
import elevator

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"

job_liste = ['1h', '3r']


def better_floors(a_list):
    """Better Floors

    This function translates the K and E floors to -1 and 0 because it is
    more sensible to have them named that way
    """
    new_list = []
    for entry in a_list:
        if (entry[1] == "K"):
            a = entry[0] + "-1"
            new_list.append(a)
        elif (entry[1] == "E"):
            entry[1].replace("E", "0")
            a = entry[0] + "0"
            new_list.append(a)
        else:
            new_list.append(entry)

    return (new_list)


def job_builder(elevator, jobs):
    # '''Builds the List for commands inside the elevator if job is assigned to current list'''

    builded_jobs = []

    for job in jobs:
        if elevator == job[0]:

            list = []
            destination = job[1]

            if elevator.get_level() > destination:
                list.append("r")
                for lev in range(elevator.get_level, destination - 1, -1):
                    list.append(lev)
            elif elevator.get_level() < destination:
                list.append("h")
                for lev in range(elevator.get_level, destination + 1):
                    list.append(lev)
            elif elevator.get_level() == destination:
                list.append("same floor")
                list = [destination]

            list.append(level_stop(destination))

            builded_jobs.append(list)

            jobs.remove(job)  # removes the converted jobs

    return builded_jobs


def spec_job_assigner(elevator, tic, jobs):
    '''assigns the converted jobs to specific job list'''

    converted_jobs = job_builder(elevator, jobs)

    for job in converted_jobs:

        counter = 0
        tic_plus_x = 0;
        treffer = False

        if elevator.get_direction() == job[0]:  # only append the jobs that are in the same direction

            if elevator.spec_list[tic] == 10:
                elevator.spec_list.extend(job)
                # converted_jobs.remove(job)
                continue

            for lev in job[1:]:
                counter += 1

            if treffer is True and elevator.spec_list[tic + tic_plus_x] != lev:
                if elevator.get_direction() == job[0]:
                    print("have to insert here", elevator.spec_list, job[counter:])

                    elevator.spec_list.insert(tic_plus_x, job[counter:])

            for spec_lev in elevator.spec_list[
                            tic + tic_plus_x:]:  # [tic:] bedeutet schaue dir alle levels nach dem aktuellen tic an

                if tic_plus_x == len(elevator.spec_list[tic:]) and treffer is True:
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

                else:
                    print("first new element")

                tic_plus_x += 1

                # if tic_plus_x == len(elevator.spec_list[tic:]) and treffer is True:
                #     print("append at last char")

            if treffer is True:
                elevator.spec_list.extend(job[tic_plus_x - 1:])


def common_job_assigner(elevator, job, tic):
    '''commands from outside the elevator will be passed to the elevator here'''
    #print("----common job assigner---", job)
    new_tic = -1
    match_number = 0
    direction = ""
    match = False

    # for both elevators ...

    infos = ""

    if elevator.spec_list[tic] == 10:  # if no jobs left get people from floors
        infos = abs(elevator.get_level() - int(job[0]))
        return infos

    for lev in elevator.spec_list[tic:]:
        new_tic += 1
        if int(job[0]) == lev:
            print("elevator passes level")
            match = True

        if match is True:
            if elevator.spec_list[tic + new_tic] > elevator.spec_list[tic + new_tic + 1]:
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
                continue  # or evtl. break
    return "no match"
    # delete jobs after assigning them!!


def assign_common_stop(destination, elevator, match_tic, tic):
    list = []
    destination = int(destination)
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

    if elevator.spec_list[tic] == 10:
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
