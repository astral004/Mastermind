"""
   Kash Tare
   CS5001
   Spring 2021
   Project: A class responsible for creating and maintaining the Display
"""
from Row import *


class Display:
    """
    The display where players can see their guesses being recorded,
    can see their guesses being checked, and can see the round number.
    Built off of 10 Row instances.
    """
    def __init__(self):
        """
        method -- __init__
            initializes an instance of Display which holds rows of the marbles and the pegs that will be colored
            as well as a turtle to point to the current round
        """
        self.counter = turtle.Turtle()
        self.counter.hideturtle()
        self.counter.color("black", "red")
        self.counter.up()
        self.counter.goto(-265, 285)
        self.counter.shapesize(2, 2, 2)

        self.pen = turtle.Turtle()
        self.pen.color("black")
        self.pen.width(10)
        self.pen.hideturtle()
        self.pen.speed(0)

        self.marble_x = -230
        self.marble_y = 270
        self.peg_x = -50
        self.peg_y = 288
        self.rows = [Row(Point(self.marble_x, self.marble_y), Point(self.peg_x, self.peg_y)),
                     Row(Point(self.marble_x, self.marble_y-50), Point(self.peg_x, self.peg_y-50)),
                     Row(Point(self.marble_x, self.marble_y-100), Point(self.peg_x, self.peg_y-100)),
                     Row(Point(self.marble_x, self.marble_y-150), Point(self.peg_x, self.peg_y-150)),
                     Row(Point(self.marble_x, self.marble_y-200), Point(self.peg_x, self.peg_y-200)),
                     Row(Point(self.marble_x, self.marble_y-250), Point(self.peg_x, self.peg_y-250)),
                     Row(Point(self.marble_x, self.marble_y-300), Point(self.peg_x, self.peg_y-300)),
                     Row(Point(self.marble_x, self.marble_y-350), Point(self.peg_x, self.peg_y-350)),
                     Row(Point(self.marble_x, self.marble_y-400), Point(self.peg_x, self.peg_y-400)),
                     Row(Point(self.marble_x, self.marble_y-450), Point(self.peg_x, self.peg_y-450))]

    def draw(self):
        """
        method -- draw
            visualizes the display with marbles, and pegs
        :return:
        """
        self.counter.showturtle()
        self.pen.up()
        self.pen.goto(-300, 320)
        self.pen.down()
        self.pen.goto(5, 320)
        self.pen.goto(5, -200)
        self.pen.goto(-300, -200)
        self.pen.goto(-300, 320)
        for row in self.rows:
            row.draw()
