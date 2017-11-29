'''
Created on 27.11.2017

@author: Robert
'''


class Elevator (object):
    '''
    classdocs
    '''

    def __init__(self, name, level, direction, spec_list):
        '''
        Constructor
        '''
        self.name = name
        self.level = level
        self.direction = direction
        self.spec_list = spec_list

    def get_name(self):
        return self.__name


    def get_level(self):
        return self.__level


    def get_direction(self):
        return self.__direction


    def set_name(self, value):
        self.__name = value


    def set_level(self, value):
        self.__level = value


    def set_direction(self, value):
        self.__direction = value


    def del_name(self):
        del self.__name


    def del_level(self):
        del self.__level


    def del_direction(self):
        del self.__direction
        
    def elevator_printer(self):
        print("Elevator:", self.name, "at level:", self.level, "is going:", self.direction)

    name = property(get_name, set_name, del_name, "name's docstring")
    level = property(get_level, set_level, del_level, "level's docstring")
    direction = property(get_direction, set_direction, del_direction, "direction's docstring")
        
