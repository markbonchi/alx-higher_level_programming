#!/usr/bin/python3
'''
Class Square that defines a square
'''


class Square:
    '''
    __init__ method for parameters of square
    args:
        param1 (int): size
    '''
    def __init__(self, size=0, position=(0,0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) and type(position[1]) is not int
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def position(self):
        '''Return (tuple): position'''
        return self.__position
    @property
    def size(self):
        '''
        Return(int): size
        '''
        return self.__size

    @position.setter
    def position(self, value):
        ''''''
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) and type(position[1]) is not int
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        '''
        Set value for private attribute size

        args:
            param1 (int): size
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''
        Return(int): area of square
        '''
        x = int(self.__size)**2
        return int(x)

    def my_print(self):
        '''
        prints square in stdout with character #
        '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
