#!/usr/bin/python3
""" base """


class Base:
    """ This class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is a definition init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
