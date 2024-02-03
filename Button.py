"""
   Kash Tare
   CS5001
   Spring 2021
   Project: A class to create the check, x, and quit buttons
"""
import turtle
from Point import Point


class Button:
    """
    A button that takes a Point instance for position and a string that is the name
    of the gif that will become the shape of the button.
    """
    def __init__(self, position, name):
        """
        method -- __init__
            Initializes an instance of Button
        :param position: (Point) takes a location in the form of a point
        :param name: (str) the name of the .gif file to use for the shape
        """
        self.pen = turtle.Turtle()
        self.position = position
        self.pen.hideturtle()
        self.pen.speed(0)
        turtle.Screen().addshape(name)
        self.pen.shape(name)

    def draw(self):
        """
        method -- draw
            visualizes the button instance
        :return: (void)
        """
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.st()

