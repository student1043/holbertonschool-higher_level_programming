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

    @property
    def size(self):
        """ size property """
        return self.width

    @size.setter
    def size(self, value):
        """ size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update args, kwargs """
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
        for ind, val in kwargs.items():
            if hasattr(self, ind) is True:
                setattr(self, ind, val)

    def to_dictionary(self):
        """ My Dict """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
