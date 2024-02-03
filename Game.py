"""
   Kash Tare
   CS5001
   Spring 2021
   Project: A class to maintain game logic
"""
from random import randint


class Game:
    """
    A class to create and maintain the game logic.
    Holds information crucial to saving the leaderboard, updating the secret code, the player's guess, the colors
    which never change but are used to randomize the secrete code, the counter which is a list of [round, marble]
    and keeps track of the round number and which marble to color next, and whether the game is still running.
    """
    def __init__(self):
        """
        method -- __init__
            initializes an instance of the game
        """
        self.player_name = ""
        self.leader_list = []
        self.secret_code = []
        self.player_code = []
        self.colors = ["blue", "red", "green", "yellow", "purple", "black"]
        self.counter = [0, 0]
        self.running = True

    def generate_code(self):
        """
        method -- generate_code
            Generates the secret code and returns it
        :return: (str) The secret code
        """
        code = []
        for i in range(4):
            """
            ALLOWS FOR MULTIPLE OF THE SAME COLOR!
            """
            random_number = randint(0, 5)
            code.append(self.colors[random_number])
        # game is significantly easier with line 41 uncommented. Used for testing purposes
        # print(code)
        return code

    def read_leaders_file(self, controller, file_name):
        """
        method -- read_leaders_file
            reads the leaders file if it exists and returns a list that contatins lists of a score and username.
            If it doesn't exist, writes an empty file and returns an empty list.
        :param file_name: (str) name of file from which to read
        :param controller: (Controller) instance of the Controller object
        :return: Either a list of scores, and users or an empty list if a leaders file does not exist.
        """
        leaders_list = []
        try:
            with open(file_name, mode="r") as file:
                for line in file:
                    leaders_list.append(line.split())
                return leaders_list
        except FileNotFoundError:
            print("File not found! Creating leaders file now.")
            self.write_leaders_file([], controller, file_name)
            return []

    def write_leaders_file(self, leaders_list, controller, file_name):
        """
        method -- write_leaders_file
            Writes the leaders list to a file if it exists.
            If it doesn't exist, catches an error and triggers a method that will update the display.
        :param file_name: (str) name of file to write
        :param leaders_list: (List) list of winners
        :param controller: (Controller) instance of the Controller class used to trigger the display_error method
        :return: (void)
        """
        temp_list = []
        leaders_list.sort()
        if len(leaders_list) > 5:
            leaders_list = leaders_list[:5]
        try:
            with open(file_name, mode="w") as file:
                if len(leaders_list) > 0:
                    for leader in leaders_list:
                        temp_list.append(" ".join(leader))
                    file.write("\n".join(temp_list))
        except FileNotFoundError:
            controller.display_error("leaderboard_error.gif")

    def take_input(self, color):
        """
        method -- take_input
            takes a color as input and updates the model if there are less than 4 colors in the player's guess
        :param color: (str) the color that was clicked
        :return: (void)
        """
        if len(self.player_code) < 4:
            self.player_code.append(color)

    def count_bulls_and_cows(self, secret_code, guess):
        """
        method -- count_bulls_and_cows
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
            """
            FOR THE SAKE OF HAVING MULTIPLE COLORS IN THE SECRET CODE:
            needed to maintain a list of which colors in the secret code were already checked to prevent getting
            multiple cows for the same color. I.e. if there was only one red in the answer, there should be only
            one bull or one cow even if the player guesses 4 reds.
            """
            checked = [False, False, False, False]
            for i in range(len(guess)):  # first set all bulls to checked
                if guess[i] == secret_code[i]:
                    checked[i] = True
            for i in range(4):  # now go through the guess and count which are bulls vs which are cows
                if guess[i] == secret_code[i]:
                    bulls += 1
                else:  # if not a bull
                    for j in range(4):  # iterate through all the OTHER colors in the secre t code
                        """
                        if not the same index, but current guess matches a different answer that has not been checked
                        increment cow and stopping searching
                        """
                        if i != j and guess[i] == secret_code[j] and checked[j] is False:
                            cows += 1
                            checked[j] = True
                            break
            return bulls, cows
