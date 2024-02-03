"""
   Kash Tare
   CS5001
   Spring 2021
   Project: A class to create and maintain the Leaderboard
"""
import turtle


class Leaderboard:
    """
    A leaderboard which displays the top 5 scores.
    """
    def __init__(self):
        """
        method -- __init__
            initializes an instance of leaderboard with a turtle for the frame, a turtle for the pen, and
            a turtle for the title
        """
        self.frame = turtle.Turtle()
        self.frame.color("blue", "blue")
        self.frame.width(10)
        self.frame.hideturtle()
        self.frame.speed(0)

        self.pen = turtle.Turtle()
        self.pen.color("blue", "blue")
        self.pen.width(10)
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.up()

        self.title = turtle.Turtle()
        self.title.color("blue", "blue")
        self.title.width(10)
        self.title.hideturtle()
        self.title.speed(0)
        self.title.up()

    def draw(self):
        """
        method -- draw
            Visualizes the frame and writes the title
        :return: (void)
        """
        self.frame.up()
        self.frame.goto(20, 320)
        self.frame.down()
        self.frame.goto(300, 320)
        self.frame.goto(300, -200)
        self.frame.goto(20, -200)
        self.frame.goto(20, 320)
        self.frame.up()
        self.title.goto(55, 270)
        self.title.write("Leaders:", font=("Arial", 25, "normal"))

    def write_leaders(self, leaders_list):
        """
        method -- write_leaders
            clears any currently displayed leaders in case there has been an update, sorts the list of leaders for
            number of wins, slices the list so it only has up to five leaders, and finally writes score: leader-name
            tuples for each in the leader list
        :param leaders_list: (List) A list which contatins lists that hold a score as the first element and the name of
            the leader as the second element. E.g. [["0", "Python"]].
        :return: (void)
        """
        self.pen.clear()
        x = 55
        y = 235
        font = ("Arial", 20, "normal")
        leaders_list.sort()
        if len(leaders_list) > 5:
            leaders_list = leaders_list[:5]
        if len(leaders_list) > 0:
            for i in range(len(leaders_list)):
                self.pen.goto(x, y - (i * 30))
                self.pen.write("{0}: {1}".format(leaders_list[i][0], leaders_list[i][1]), font=font)
