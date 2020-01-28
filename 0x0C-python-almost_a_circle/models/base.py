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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Json String """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ save to file """
        with open(cls.__name__ + ".json", "w") as file:
            if list_objs is None:
                file.write("[]")
