#!/usr/bin/python3
"""
    Square class module
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    class Square defining parameters of a square

    __init__(size, x, y, id):
    """

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__,
                self.id, self.x,
                self.y, self.width))
