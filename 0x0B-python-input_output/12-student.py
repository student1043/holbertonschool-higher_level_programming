#!/usr/bin/python3
"""
    a class Student that defines a student
"""


class Student:
    """
        a class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
            Function init
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Class to JSON
        """
        if attrs is not None:
            dic = {}
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return dic
        else:
            return(self.__dict__)
