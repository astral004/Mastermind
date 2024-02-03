"""
   Kash Tare
   CS5001
   Spring 2021
   Project: A class to create and maintain marbles. Modified so the clickable range of the x axis of a marble is only
   1.16 times the size.
"""
import turtle
from Point import Point

MARBLE_RADIUS = 15


class Marble:
    """
    A Marble which can be colored, erased, emptied, and knows whether it was clicked on.
    """
    def __init__(self, position, color, size=MARBLE_RADIUS):
        """
        method -- __init__
            initializes an instance of Marble
        :param position: (Point) the location of the marble passed as an instance of Point
        :param color: (str) the initial color of the marble
        :param size: (int) the initial radius of the marble -- defaults to 15
        """
        self.pen = self.new_pen()
        self.color = color
        self.position = position
        self.visible = False
        self.is_empty = True
        self.pen.hideturtle()
        self.size = size
        self.pen.speed(0)  # set to fastest drawing

    def new_pen(self):
        """
        method -- new_pen
            instantiates a new turtle
        :return: (Turtle) an instance of Turtle
        """
        return turtle.Turtle()

    def set_color(self, color):
        """
        method -- set_color
            sets the color of the marble
        :param color: (str) the desired color
        :return: (void)
        """
        self.color = color
        self.is_empty = False

    def get_color(self):
        """
        method -- get_color
            returns the current color of the marble
        :return: (str) current color
        """
        return self.color

    def draw(self):
        """
        method -- draw
            visualizes the marble
        :return: (void)
        """
        # if self.visible and not self.is_empty:
        # return
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        """
        method -- draw_empty
            visualizes the marble without a color
        :return: (void)
        """
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)

    def erase(self):
        """
        method -- erase
            turns off the visibility of the marble and clears it from the screen
        :return: (void)
        """
        self.visible = False
        self.pen.clear()

    def clicked_in_region(self, x, y):
        """
        method -- clicked_in_region
            checks if the passed in coordinates are within the marble's allocated area for clicks
        :param x: (float) x coordinate of the clicked location
        :param y: (float) y coordinate of the clicked location
        :return: (bool) if the point falls within the marble's allocated area, returns true; otherwise, returns false
        """
        if abs(x - self.position.x) <= self.size * 1.16 and \
                abs(y - self.position.y) <= self.size * 2:
            return True
        return False


def main():
    marble = Marble(Point(100, 100), "blue")
    marble.draw_empty()
    k = input("enter something here and I'll fill the marble > ")
    marble.draw()
    k = input("enter something here and I'll erase the marble > ")
    marble.erase()


if __name__ == "__main__":
    main()
