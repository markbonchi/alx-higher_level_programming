#!/usr/bin/python3
"""student module"""


class Student:
    """
    Class Student

    __init__ args:
        first_name: (str)
        last_name: (str)
        age: (int)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json

        args:
            attrs: (list)
        """
        my_dict = self.__dict__.copy()
        if attrs is None:
            return my_dict
        else:
            my_list = [i for i in my_dict.keys()]
            for item in my_list:
                if item not in attrs:
                    del my_dict[item]
            return my_dict

    def reload_from_json(self, json):
        """replaces attributes of the student instance"""
        for attr in json:
            self.__dict__[attr] = json[attr]
