"""An Elevator Class

If the constructor of this class is called, an elevator object is constructed.
We gave them quite a few attributes and functions as well a pocedures. That
helped us in the development. 
"""

import os
if (os.name == "nt"):
    import elevator_problem
import main
import main_controller
import elevator
import job_feeder
import improved_controller
import improved_job_feeder

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 


def run():
    """Run
    
    print all help file for documentation purposes. One may notice,
    that there is a if statement in line 34. This is due to different
    os versions we are developing on. Windows and eclipse allows to import 
    the package for printing information but unix/macOS seems to have problems
    So we figuered, we want to run our program smoothly on most platforms we
    chose to work this problem this way. 
    """
    
    if (os.name == "nt"):
        print(help(elevator_problem))
    print(help(main))
    print(help(main_controller))
    print(help(improved_controller))
    print(help(elevator))
    print(help(job_feeder))
    print(help(improved_job_feeder))
    print("\n")
