"""The Main Function

This module is the start of our elevator programm. 
"""

import time
import main_controller

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
    print("...Press 3 for Help File...............")
    print("...Press 4 to Exit.....................")
    print(".......................................")

def main():
    """Main Procedure
    
    Holds everything in a for loop
    """
    
    while (True):
        menue()
        inp = input()
        if (inp == "1"):
            main_controller.main_function()
        elif (inp == "2"):
            print("Same procedure but improved")
        elif (inp == "3"):
            print("Help File")
            print(help(main_controller))
        elif (inp == "4"):
            break
        else:
            print("Invalid Input. Please reoeat")

if __name__ == '__main__':
    main()
