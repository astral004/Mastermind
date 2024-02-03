"""
   Kash Tare
   CS5001
   Spring 2021
   Project: A class that will create an maintain an individual Row in the Display
"""
from Marble import *
from Point import Point


class Row:
    """
    A row of 4 Marble instances called marbles and 4 small Marble instances called pegs.
    10 of these such rows form the Display.
    """
    def __init__(self, marble_position, peg_position):
        """
        method -- __init__
            initializes a Row instance with marbles and pegs
        :param marble_position: (Point) a starting location for the current row of marbles
        :param peg_position: (Point) a starting location for the current row's pegs
        """
        self.marbles = [Marble(marble_position, "white"),
                        Marble(Point(marble_position.x + 40, marble_position.y), "white"),
                        Marble(Point(marble_position.x + 80, marble_position.y), "white"),
                        Marble(Point(marble_position.x + 120, marble_position.y), "white")]

        self.pegs = [Marble(peg_position, "white", 5),
                     Marble(Point(peg_position.x+15, peg_position.y), "white", 5),
                     Marble(Point(peg_position.x, peg_position.y-15), "white", 5),
                     Marble(Point(peg_position.x+15, peg_position.y-15), "white", 5)]
        self.marble_position = marble_position
        self.peg_position = peg_position

    def color_marble(self, color, index):
        """
        method -- color_marble
            colors the marble based on the color and the index passed
        :param color: (str) the color with which to fill the marble
        :param index: (int) the index, from 0-3, of the marble to color
        :return: (void)
        """
        self.marbles[index].set_color(color)
        self.marbles[index].draw()

    def color_peg(self, color, index):
        """
        method -- color_peg
            colors the peg based on the color and the index passed
        :param color: (str) the color with which to fill the peg -- either black, or red
        :param index: (int) the index, from 0-3, of the peg to color. Pegs are color top left, top right, bottom left,
        bottom right
        :return: (void)
        """
        self.pegs[index].set_color(color)
        self.pegs[index].draw()

    def draw(self):
        """
        method -- draw
            visualizes the row of marbles and pegs on startup
        :return: (void)
        """
        for marble in self.marbles:
            marble.draw()
        for peg in self.pegs:
            peg.draw()
