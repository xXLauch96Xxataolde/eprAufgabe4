'''
Created on 27.11.2017

@author: Niels
'''

import time
import random
from elevator_problem.elevator import Elevator

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"

job_liste = ['1h', '3r']


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


def spec_job_assigner(elevator, takt, jobs):
    '''assigns the converted jobs to specific job list'''

    converted_jobs = job_builder(elevator, jobs)

    for job in converted_jobs:

        counter = 0
        takt_plus_x = 0;
        treffer = False

        if elevator.spec_list[takt] == 10:
            elevator.spec_list.extend(job)



        for lev in job[1:]:

            counter += 1

            if treffer is True and  elevator.spec_list[takt + takt_plus_x] != lev:
                if elevator.get_direction() == job[0]
                print("have to insert here", elevator.spec_list, job[counter:])

                elevator.spec_list.insert(takt_plus_x, job[counter:])

            for spec_lev in elevator.spec_list[takt + takt_plus_x:]:  # [takt:] bedeutet schaue dir alle levels nach dem aktuellen takt an

                if takt_plus_x == len(elevator.spec_list[takt:]) and treffer is True:
                    elevator.spec_list.extend(job[counter:])
                    break

                if lev == spec_lev:

                    print("match")
                    treffer = True
                    takt_plus_x += 1
                    continue

                elif treffer is True:
                    print("no match anymore check new element")

                    break

                else: print("first new element")

                takt_plus_x += 1

            # if takt_plus_x == len(elevator.spec_list[takt:]) and treffer is True:
            #     print("append at last char")

        if treffer is True:
            elevator.spec_list.extend(job[takt_plus_x - 1:])







def allgemeiner_job_assigner(elevator, job_liste, takt):
    '''commands from outside the elevator will be passed to the elevator here'''
    new_takt = -1
    match_number = 0
    direction = ""
    match = False

    for job in job_liste:

        for lev in elevator.spec_list[takt:]:
            new_takt += 1
            if job[0] == lev:
                print("elevator passes level")
                match = True

            if match is True:
                if elevator.spec_list[takt + new_takt] > elevator.spec_list[takt + new_takt + 1]:
                    print("goes down")
                    direction = "r"
                elif elevator.spec_list[takt + new_takt] < elevator.spec_list[takt + new_takt + 1]:
                    print("goes up")
                    direction = "h"

                if direction == job[1] and match is True:
                    print("WE HAVE A MATCH")
                    match_number += 1

                    return new_takt
                    # elevator.spec_list.insert(new_takt, level_stop(job[0]))

                else: continue  # or evtl. break


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
