#!/usr/bin/python3
""" Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ My Class """
    def __init__(self, size, x=0, y=0, id=None):
        """ My def init """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ My str """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)
