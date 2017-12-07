"""The Main Function

This module is the start of our elevator programm. 
"""

import time
import main_controller
import docu_handling
import help
import improved_controller

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 


def menue():
    """a procedure for printing a menue we assume"""
    
    print("...Welcome to the Menue................")
    print(".......................................")
    print("...Press 1 to open standard Elevator...")
    print("...Press 2 to open improved Elevator...")
    print("...Press 3 to open Help File...........")
    print("...Press 4 to open Documenation........")
    print("...Press 5 to Exit.....................")
    print(".......................................")


def main():
    """Main Procedure
    
    Holds everything in a for loop
    """
    
    while (True):
        menue()
        inp = ""
        inp = input()
        if (inp == "1"):
            main_controller.controller()
        elif (inp == "2"):
            print("Same procedure but improved")
            improved_controller.controller()
        elif (inp == "3"):
            help.helpings()
        elif (inp == "4"):
            docu_handling.run()
        elif (inp == "5"):
            import sys
            sys.exit()
        else:
            print("Invalid Input. Please repeat")


if __name__ == '__main__':
    main()
