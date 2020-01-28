#!/usr/bin/python3
""" base """
import json


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

    def to_json_string(list_dictionaries):
        """ Json String """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
