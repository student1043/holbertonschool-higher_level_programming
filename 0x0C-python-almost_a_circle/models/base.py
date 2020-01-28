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

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        list = []
        if list_objs is not None:
            for i in list_objs:
                list.append(i.to_dictionary())
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """ from json string """
        list = []
        if json_string is None or not json_string:
            return list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create """
        if cls.__name__ == "Square":
            tip = cls(10)
        elif cls.__name__ == "Rectangle":
            tip = cls(10, 10)
        tip.update(**dictionary)
        return tip

    @classmethod
    def load_from_file(cls):
        """ load from file """
        try:
            with open(cls.__name__ + ".json", "r") as file:
                pr = cls.from_json_string(file.read())
                list = []
                for i in pr:
                    list.append(cls.create(**i))
                return list
        except:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to file csv """
        list = []
        if list_objs is not None:
            for i in list_objs:
                list.append(i.to_dictionary())
        with open(cls.__name__ + ".csv", "w") as file:
            file.write(cls.to_json_string(list))

    @classmethod
    def load_from_file_csv(cls):
        """ load from file """
        try:
            with open(cls.__name__ + ".csv", "r") as file:
                pr = cls.from_json_string(file.read())
                list = []
                for i in pr:
                    list.append(cls.create(**i))
                return list
        except:
            return []