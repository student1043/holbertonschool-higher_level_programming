#!/usr/bin/python3
class Node:
    """This is a class"""
    def __init__(self, data, next_node=None):
        """This is a definition"""
        self.__data = data
        self.__next_node = next_node
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) or next_node != None
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """This is a definition"""
        return self.__data

    @data.setter
    def data(self, value):
        """This is a definition"""
        self.__data = value
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    
