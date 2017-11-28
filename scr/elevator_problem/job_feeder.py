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



def spec_job_assigner(spec_list, job):
'''assigns the converted jobs to specific job list'''
    for lev in job:
        for spec_lev in spec_list[takt:]:  # [takt:] bedeutet schaue dir alle levels nach dem aktuellen takt an
            if lev == spec_lev:
                print("match")
                break


