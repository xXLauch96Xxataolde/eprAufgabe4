"""Job Feeder

Nomnomnom jobs
"""

import time
import random
import elevator
import improved_controller

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

    Takes a job and and builds a list with numbers in range from current level to destination of
    job.
    Return the list.
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


    return builded_jobs


def spec_job_assigner(elevator, tic, jobs):
    """ Specific Job Assigner

    This function takes the specific jobs and assigns them to their elevator. If a job is not
    in the direction of the elevator it remains and is later on reassigned to the specific-jobs.
    At the beginning we take our jobs, which we received from the main_controller, and build a
    list with the range of numbers from the current level to our destination.
    Then we run every list through our "function", which either assigns it to the elevator or
    appends it to the remaining job list, which is later on returned. (In the function we take
    the first element of our job and the first element of the current job list of the elevator
    and compare them. If they are not identical we the next level of the current job list of the
    elevator. If we have a match the next level from the elevator is compared. If those are
    identical we go on. If not we take the next level from the job and start over until one of
    the cases is reached (1. Compared every element 2. Had a match and now not anymore 3. List
    only consist of one job 4. No current elevator jobs).
    The return value of this function is always the remaining job list.
    """

    remaining_spec_jobs = []

    jobs = improved_controller.delete_doubles(jobs)

    converted_jobs = job_builder(elevator, jobs)

    for job in converted_jobs:

        improved_controller.elevator_setter(elevator, tic)
        elevator.elevator_printer(tic)

        if job == elevator.name + "c":
            print("Doors closing --- Caution!")
            continue

        counter = -1
        tic_plus_x = 0
        treffer = False

        # we determine the job direction
        job_direction = "none"
        if int(job[-1]) > elevator.get_level():
            job_direction = "up"
        elif int(job[-1]) < elevator.get_level():
            job_direction = "down"

        if elevator.get_direction() == job_direction or elevator.get_direction() == "none":
            # only append the jobs that are in the same direction

            if elevator.spec_list[tic] == 10 and len(elevator.spec_list[tic:]) == 1:  # 4.
                elevator.spec_list.extend(job[1:])
                continue

            for lev in job:
                counter += 1

                if tic_plus_x == len(elevator.spec_list[tic:]) and treffer is True:  # 1.
                    elevator.spec_list.extend(job[counter:])
                    break

                if treffer is True and elevator.spec_list[tic + tic_plus_x] != lev:  # 2.
                    for level in job[counter:]:
                        elevator.spec_list.insert(tic + tic_plus_x - 1, level)
                    break

                for spec_lev in elevator.spec_list[
                                tic + tic_plus_x:]:
                    # [tic:] means look at all levels after the current tic

                    if tic_plus_x - 1 == len(elevator.spec_list[tic:]) and treffer is True:  # 2.
                        print("!!!", job[counter:])
                        break

                    if job[-1] == spec_lev:  # 3.
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

                if tic_plus_x - 1 == len(elevator.spec_list[tic:]) and treffer is True:  # 1.
                    elevator.spec_list.extend(job[counter:])
                    break

                try:
                    if job[-1] == spec_lev and job[-1] == elevator.spec_list[tic + tic_plus_x + 1]:
                        break
                except IndexError:
                    break

        # if a job can not be assigned, because it is not in the same direction it is appended
        # to the remaining_job_list
        else:
            if job[-1] == -1:
                rema_job = elevator.name + "-1"
            else:
                rema_job = elevator.name + str(job[-1])
            try:
                remaining_spec_jobs.remove(rema_job)
            except ValueError:
                None
            remaining_spec_jobs.append(rema_job)  # save the remaining jobs

    return remaining_spec_jobs


def common_job_comparer(elevator, job, tic):
    """Common Job Assigner

    The common jobs from outside the elevator are passed to this function. It takes the job
    and checks if it is possible to assign it to an elevator. It return values which are then
    compared by the main controller.
    """
    print("Common Job Assigner", job)
    new_tic = -1
    match_number = 0
    direction = ""
    match = False
    infos = ""

    # if no jobs left get people from floors
    if elevator.spec_list[tic] == 10 and len(elevator.spec_list[tic:]) == 1:
        if len(job) > 2:
            infos = abs(elevator.get_level() - (-1))
        else:
            infos = abs(elevator.get_level() - int(job[0]))
        return infos

    # check if elevator passes level and check if direction of elevator is equal to job direction
    for lev in elevator.spec_list[tic:]:
        new_tic += 1

        if int(job[0]) == lev:
            match = True

        if match is True:
            if elevator.get_level() > elevator.spec_list[tic + new_tic]:
                direction = "r"
            elif elevator.get_level() < elevator.spec_list[tic + new_tic]:
                direction = "h"
            if direction == job[1] and match is True:
                match_number += 1
                return new_tic + 1

            else:
                break

    return "no match"


def assign_common_stop(destination, elevator, match_tic, tic):
    """Assign a common stop

    This procedure is called from the main controller for an elevator after the comparision, for
    which elevator the job should be assigned to. Then the job is built as a list in range from
    level to destination. This list is then appended to the list of levels which the elevator
    passes.
    """
    list = []
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
            elevator.spec_list.insert(elevator.spec_list[tic:].index(destination) + tic, level)


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
