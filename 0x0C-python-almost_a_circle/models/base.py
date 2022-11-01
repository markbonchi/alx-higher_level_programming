#!/usr/bin/python3
"""
    Base class module
"""
import json
import csv
import turtle



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

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
