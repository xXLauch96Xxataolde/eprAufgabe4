"""An Elevator Class

If the constructor of this class is called, an elevator object is constructed.
We gave them quite a few attributes and functions as well a pocedures. That
helped us in the development. 

"""

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 


class Elevator (object):
    """"Elevator Class
    
    To built elevators. More details in constructor and functions
    """

    def __init__(self, name, level, direction, spec_list):
        """The Constructor
        
        The constructor gets attributes and produces an elevator object if
        called to do so. Name is the name, sure, level is the current level, 
        on which the elevator elevates in the moment. The spec_list is an 
        individual list with what we call jobs. A job is the push of a button
        which adds a destination for the designated elevator to elevate to. 
        """
        self.name = name
        self.level = level
        self.direction = direction
        self.spec_list = spec_list

    def get_name(self):
        """returns the name of an instance"""
        
        return self.__name

    def get_level(self):
        """returns the level of an instance"""
        
        return self.__level

    def get_direction(self):
        """returns the direction of an instance, like up and down"""
        
        return self.__direction

    def get_spec_list(self):
        """returns the spec_list, as mentioned in the constructor docstring"""
        
        return self.__spec_list

    def set_name(self, value):
        """allows to set a name for an instance. But is protected"""
        
        self.__name = value

    def set_level(self, value):
        """allows to set a level"""
        
        self.__level = value

    def set_direction(self, value):
        """allows to set a direction"""
        
        self.__direction = value

    def set_spec_list(self, value):
        """sets a special list"""
        
        self.__spec_list = value

    def del_name(self):
        """deletes a set name"""
        
        del self.__name

    def del_level(self):
        """destructs the name"""
        
        del self.__level

    def del_direction(self):
        """deletes the direction"""
        
        del self.__direction

    def del_spec_list(self):
        """deletes the special list"""
        
        del self.__spec_list
        
    def elevator_printer(self, tic):
        """Elevator Printer
        
        a handy procedure we wrote to elegantly print all important information 
        about an elevator object
        """
        
        print("Elevator:", self.name, "at level:", self.level, "is going:",
              self.direction, "current Jobs:", self.spec_list[tic:])

    def elevator_fileprinter(self, tic):
        """The elevator file printer
        
        Because we had a method in mind to show a certain way of behaviour
        of two different elevator algorithms we used this function to 
        return relevant information to e.g. another function which writes them 
        to a file
        """
        
        outpur_str = ""
        outpur_str = "Elevator: " + self.name + " at level: " 
        outpur_str += str(self.level) + " is going: " + self.direction 
        outpur_str += " current Jobs: " + str(self.spec_list[tic:])
        return(outpur_str)

    
    name = property(get_name, set_name, del_name, "name's docstring")
    level = property(get_level, set_level, del_level, "level's docstring")
    direction = property(get_direction, set_direction, del_direction,
                         "direction's docstring")
    spec_list = property(get_spec_list, set_spec_list, del_spec_list,
                         "spec_list's docstring")
