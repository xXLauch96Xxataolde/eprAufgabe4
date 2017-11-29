'''
Created on 27.11.2017

@author: Niels
'''

import time

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


def job_builder(elevator, destination):
'''Builds the List for commands inside the elevator if job is assigned to current list'''
    list = []
    if elevator.level > destination:
         for lev in range(elevator.level, destination - 1, -1):
             list.append(lev)
    elif elevator.level < destination:
        for lev in range(elevator.level, destination + 1):
            list.append(lev)
    return list


def spec_job_assigner(spec_list, job):
'''assigns the converted jobs to specific job list'''

    if spec_list[takt] == 10:
        spec_list.extend(job)

    takt_plus_x = 0;

    for lev in job:
        for spec_lev in spec_list[takt + takt_plus_x:]:  # [takt:] bedeutet schaue dir alle levels nach dem aktuellen takt an


            job_parser


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

        if takt_plus_x == len(spec_list[takt:]) and treffer is True:
            print("append at last char")

    if treffer is True:
        spec_list.extend(job[takt_plus_x - 1:])

direction = ""
match = False
new_takt = -1
def allgemeiner_job_assigner(job_liste, elevator, spec_list):
    for job in job_liste:

        for lev in spec_list[takt:]:
            new_takt += 1
            if job[0] == lev:
                print("elevator passes level")
                match = True

            if match is True:
                if spec_list[takt + new_takt] > spec_list[takt + new_takt + 1]:
                    print("fährt runter")
                    direction = "r"
                elif spec_list[takt + new_takt] < spec_list[takt + new_takt + 1]:
                    print("fährt hoch")
                    direction = "h"

                if direction == job[1] and match is True:
                    print("WE HAVE A MATCH")

                else: continue  #or evtl. break



2r
3h

1234

1
