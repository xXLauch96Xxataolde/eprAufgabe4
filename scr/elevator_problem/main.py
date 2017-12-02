"""The Main Function

This function initializes the start of the program
"""

import time
import gui_levitation as gui_levitation
import main_controller

__author__ = "123456: Ada Lovelace, 654321: Alan Turing"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"

def menue():
    
    print("...Welcome to the Menue................")
    print(".......................................")
    print("...Press 1 to open standard Elevator...")
    print("...Press 2 to open improved Elevator...")
    print("...Press 3 for Help File...............")
    print("...Press 4 to Exit.....................")
    print(".......................................")

def main():
    gui_levitation.test1()
    
    while (True):
        menue()
        inp = input()
        if (inp == "1"):
            main_controller.main_function()  # maybe rename these modules
        elif (inp == "2"):
            print("Same procedure but imporved")
        elif (inp == "3"):
            print("Help File")
        elif (inp == "4"):
            break
        else:
            print("Invalid Input. Please reoeat")

if __name__ == '__main__':
    main()
