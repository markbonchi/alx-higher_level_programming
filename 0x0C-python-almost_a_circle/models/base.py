#!/usr/bin/python3
"""
    Base class module
"""
import json


class Base:
    """
    Base class for all other classes in this project

    def __init__(id):
    args:
        id: (int) object id
    """


    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        converts to json string

        args:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None:
            return json.dumps([])

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        converts from json string to data structure

        args:
            json_string: (str)
        """
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file
        """
        filename = "{}.json".format(cls.__name__)
        my_list = [i.to_dictionary() for i in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set

        args:
            **dictionary: key/value pair of attributes to initiate
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return [cls.create(**i) for i in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
