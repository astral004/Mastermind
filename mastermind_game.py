"""
   Kash Tare
   CS5001
   Spring 2021
   Project: Main file that runs the Mastermind game
"""
import turtle
from random import randint
from Game import *
from Button import *
from Marble import *
from Point import Point
from Display import *
from Leaderboard import *
import time


def count_bulls_and_cows(secret_code, guess):
    """
    function -- count_bulls_and_cows
        takes the secret code and the player's guess as input and checks if the player's guess matches the secrete code.
        For every guess that matches, increments bulls by 1. For every guess that is in the code but not at the right
        location, increments cows by 1.
    :param secret_code: (List) list of colors in the form the secret code
    :param guess: (List) list of colors in the player's guess
    :return: (Tuple) a tuple that holds the bulls, and the cows
    """
    if len(guess) == len(secret_code):
        bulls = 0
        cows = 0
        checked = [False, False, False, False]
        for i in range(len(guess)):
            if guess[i] == secret_code[i]:
                checked[i] = True
        for i in range(4):
            if guess[i] == secret_code[i]:
                bulls += 1
                checked[i] = True
            else:
                for j in range(4):
                    if i != j and guess[i] == secret_code[j] and checked[j] is False:
                        cows += 1
                        checked[j] = True
                        break
        return bulls, cows


class Controller:
    """
    A class to create and maintain the game controller.
    Allows the user to interact with the game and let's them know if an error occurred.
    """

    def __init__(self):
        """
        method -- __init__
            initializes an instance of Controller
        """
        self.pen = turtle.Turtle()
        self.pen.color("black")
        self.pen.width(10)
        self.pen.hideturtle()
        self.pen.speed(0)
        self.marble_button_x = -230
        self.marble_button_y = -285
        self.game = Game()
        self.marbles = [Marble(Point(self.marble_button_x, self.marble_button_y), "blue"),
                        Marble(Point(self.marble_button_x + 40, self.marble_button_y), "red"),
                        Marble(Point(self.marble_button_x + 80, self.marble_button_y), "green"),
                        Marble(Point(self.marble_button_x + 120, self.marble_button_y), "yellow"),
                        Marble(Point(self.marble_button_x + 160, self.marble_button_y), "purple"),
                        Marble(Point(self.marble_button_x + 200, self.marble_button_y), "black")]
        self.check_button = Button(Point(25, self.marble_button_y+15), "checkbutton.gif")
        self.x_button = Button(Point(90, self.marble_button_y+15), "xbutton.gif")
        self.quit_button = Button(Point(200, self.marble_button_y+15), "quit.gif")
        self.display = Display()
        self.leaderboard = Leaderboard()

    def draw(self):
        """
        method -- draw
            draws the controller
        :return: (void)
        """
        turtle.Screen().setup(width=650, height=670)
        self.pen.up()
        self.pen.goto(-300, -220)
        self.pen.down()
        self.pen.goto(300, -220)
        self.pen.goto(300, -320)
        self.pen.goto(-300, -320)
        self.pen.goto(-300, -220)
        for marble in self.marbles:
            marble.draw()
        self.check_button.draw()
        self.x_button.draw()
        self.quit_button.draw()
        self.display.draw()
        self.leaderboard.draw()

    def click_marble(self, x, y):
        """
        method -- click_marble
            called whenever a click is made on screen to check which marble was clicked
        :param x: x coordinate of marble passed by turtle
        :param y: y coordinate of marble passed by turtle
        :return: (void) updates the model via the take_input function call
        """
        if len(self.game.player_code) < 4 and self.game.running:
            for marble in self.marbles:
                if marble.clicked_in_region(x, y):
                    marble.draw_empty()
                    marble.draw()  # COMES BACK TO ALLOW MULTIPLE GUESSES OF THE SAME COLOR!
                    self.game.take_input(marble.color)
                    if (0 < len(self.game.player_code) < 4) or (self.game.counter[1] < 4):
                        self.display.rows[self.game.counter[0]].color_marble(self.game.player_code[-1],
                                                                             self.game.counter[1])
                        self.game.counter[1] += 1

    def click_check(self, x, y):
        """
        method -- click_check
            handles clicks on the check button. calls the count bulls and cows function, tells the display
            how many bulls/cows to show, tells the model to update the round Counter, displays lose gif, displays
            win gif, calls functions to update leaderboard.txt and to update the leaderboard view
        :param x: (float) x coordinate from screen
        :param y: (float) y coordinate from screen
        :return: (void)
        """
        # only go through the following if there are four guess and four colored marbles and the game is still running
        if len(self.game.player_code) == 4 and self.game.counter[1] == 4 and self.game.running:
            # animation to confirm click was registered and so the player knows something happened
            self.check_button.pen.hideturtle()
            self.check_button.pen.showturtle()
            bulls, cows = self.game.count_bulls_and_cows(self.game.secret_code, self.game.player_code)
            if bulls != 4:  # if they have not won
                self.game.counter[1] = 0  # reset the second value in counter so we can color the pegs
                for i in range(bulls):  # color bulls
                    self.display.rows[self.game.counter[0]].color_peg("black", self.game.counter[1])
                    self.game.counter[1] += 1
                for i in range(cows):  # color cows
                    self.display.rows[self.game.counter[0]].color_peg("red", self.game.counter[1])
                    self.game.counter[1] += 1
                self.game.counter[0], self.game.counter[1] = self.game.counter[0] + 1, 0  # increment the round
                if self.game.counter[0] < 10:  # if 10 rounds have not been played, move the counter down 1
                    x, y = self.display.counter.position()
                    self.display.counter.goto(x, y - 50)
                    self.game.player_code = []
                else:  # else, the player has lost. Rub it in their face with a gif
                    self.pen.up()
                    self.pen.goto(0, 0)
                    turtle.Screen().addshape("Lose.gif")
                    self.pen.shape("Lose.gif")
                    self.pen.showturtle()
                    self.game.running = False  # game over... :(
                    turtle.textinput("Secret Code", self.game.secret_code)
            else:  # in case bulls equal four, they won! :) Rub it in their face with a gif
                self.game.leader_list.append([str(self.game.counter[0] + 1), self.game.player_name])
                self.leaderboard.write_leaders(self.game.leader_list)
                self.game.write_leaders_file(self.game.leader_list, self, "leaderboard.txt")
                self.pen.up()
                self.pen.goto(0, 0)
                turtle.Screen().addshape("winner.gif")
                self.pen.shape("winner.gif")
                self.pen.showturtle()
                self.game.running = False  # game won! :)

    def click_x(self, x, y):
        """
        method -- click_x
            clears the selection the player has made so far and resets the second value in the game.counter to 0
        :param x:(float) x coordinate from screen
        :param y:(float) y coordinate from screen
        :return:(void)
        """
        if self.game.running and self.game.counter[0] < 10:
            self.x_button.pen.hideturtle()
            self.x_button.pen.showturtle()
            number_to_clear = self.game.counter[1]
            self.game.counter[1] = 0  # resets the counter of how many marbles have been colored
            for i in range(number_to_clear):  # reset all marbles to white
                self.display.rows[self.game.counter[0]].color_marble("white", self.game.counter[1])
                self.game.counter[1] += 1
            self.game.counter[1] = 0
            self.game.player_code = []  # clear the player's guesses

    def click_quit(self, x, y):
        """
        method -- click_quit
            Creates a quit popup and disables the game functionality
        :param x: (float) x coordinate from screen
        :param y: (float) y coordinate from screen
        :return: (void)
        """
        if self.game.running:  # They quit. Rub it in their face with a gif
            self.quit_button.pen.hideturtle()
            self.quit_button.pen.showturtle()
            self.pen.up()
            self.pen.goto(0, 0)
            turtle.Screen().addshape("quitmsg.gif")
            self.pen.shape("quitmsg.gif")
            self.pen.showturtle()
            self.game.counter = [10, 0]  # pushes the round counter up to 10 to prevent checks
            self.game.player_code = ["white", "white", "white", "white"]  # fills the guesses to prevent marble clicks
            self.game.running = False  # game over... :(

    def display_error(self, error_gif):
        """
        method -- display_error
            creates and shows the player an error gif for 2 seconds and disappears
        :param error_gif:(str) name of the gif to show
        :return:(void)
        """
        # something went wrong with the leaderboard.. I swear it was working a minute ago.. rub it in their face
        self.pen.up()
        self.pen.goto(0, 0)
        turtle.Screen().addshape(error_gif)
        self.pen.shape(error_gif)
        self.game.running = False
        turtle.exitonclick()

    def take_name(self):
        """
        method -- take_name
            pops up a dialog box that is taking information to be stored as a string
        :return: (str) returns the input
        """
        return turtle.textinput("Username", "Please enter your Username: ")

    def run_controller(self):
        """
        method -- run_controller
            responsible for starting the game. generates the secret_code, takes the player's name, reads
            the leaderboard file, and writes the existing leaders to the leaderboard
        :return: (void)
        """
        self.game.secret_code = self.game.generate_code()
        self.game.player_name = self.take_name()
        self.game.leader_list = self.game.read_leaders_file(self, "leaderboard.txt")
        self.leaderboard.write_leaders(self.game.leader_list)

        turtle.listen()

        turtle.Screen().onclick(self.click_marble)
        self.check_button.pen.onclick(self.click_check)
        self.x_button.pen.onclick(self.click_x)
        self.quit_button.pen.onclick(self.click_quit)

        turtle.mainloop()


# def main():
if __name__ == '__main__':

    control = Controller()
    control.draw()
    control.run_controller()


# main()
