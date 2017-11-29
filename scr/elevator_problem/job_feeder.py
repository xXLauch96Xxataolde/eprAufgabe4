'''
Created on 27.11.2017

@author: Niels
'''

import time

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


job_liste = []

def job_builder(elevator, destination):
#'''Builds the List for commands inside the elevator if job is assigned to current list'''
    list = []
    if elevator.get_level() > destination:
         for lev in range(elevator.get_level, destination - 1, -1):
             list.append(lev)
    elif elevator.get_level() < destination:
        for lev in range(elevator.get_level, destination + 1):
            list.append(lev)
    elif elevator.get_level() == destination:
        list = [destination]
    return list


def spec_job_assigner(elevator, job, takt):
#'''assigns the converted jobs to specific job list'''

    if elevator.spec_list[takt] == 10:
        elevator.spec_list.extend(job)

    takt_plus_x = 0;

    for lev in job:
        for spec_lev in elevator.spec_list[takt + takt_plus_x:]:  # [takt:] bedeutet schaue dir alle levels nach dem aktuellen takt an

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

        if takt_plus_x == len(elevator.spec_list[takt:]) and treffer is True:
            print("append at last char")

    if treffer is True:
        elevator.spec_list.extend(job[takt_plus_x - 1:])




match_number = 0
direction = ""
match = False
new_takt = -1
def allgemeiner_job_assigner(elevator, job_liste):
'''commands from outside the elevator will be passed to the elevator here'''
    for job in job_liste:

        for lev in elevator.spec_list[takt:]:
            new_takt += 1
            if job[0] == lev:
                print("elevator passes level")
                match = True

            if match is True:
                if elevator.spec_list[takt + new_takt] > elevator.spec_list[takt + new_takt + 1]:
                    print("fährt runter")
                    direction = "r"
                elif elevator.spec_list[takt + new_takt] < elevator.spec_list[takt + new_takt + 1]:
                    print("fährt hoch")
                    direction = "h"

                if direction == job[1] and match is True:
                    print("WE HAVE A MATCH")
                    match_number += 1

                    elevator.spec_list.insert(new_takt, level_stop(job[0]))

                else: continue  #or evtl. break


 '''what if posible for both elevators??????'''

def level_stop():
'''1. nimmt stockwerk zwischen -1 und 4 an und gibt liste mit eins bis drei elementen zurück
   2. K wird als -1 und E als 0 übergeben. Jobs kommen als liste ['0r', 'A-1']
'''
    random.int()
    list = []
    list.append  # random amount between 1 and 3
