"""
   Kash Tare
   CS5001
   Spring 2021
   Project: A class to test the logic behind the model of the Mastermind game.
"""
import unittest
from Game import *

GAME = None


def get_game():
    global GAME
    if GAME is None:
        GAME = Game()
        return GAME
    else:
        return GAME


class TestGame(unittest.TestCase):
    """
    A class to test the model logic of the game
    """
    def test_init(self):
        get_game()
        self.assertEqual(type(GAME), Game)

    def test_generate_code(self):
        code = get_game().generate_code()
        self.assertEqual(len(code), 4)

    def test_read_leaders_file(self):
        temp_list = get_game().read_leaders_file("controller", "test_leaders_file.txt")
        self.assertEqual(len(temp_list), 1)
        self.assertEqual(len(temp_list[0]), 2)

    def test_write_leaders_file(self):
        temp_list = [["8", "Kash"]]
        get_game().write_leaders_file(temp_list, "controller", "test_leaders_file.txt")
        new_list = get_game().read_leaders_file("controller", "test_leaders_file.txt")
        self.assertEqual(new_list, temp_list)

    def test_take_input(self):
        get_game().player_code = ["red", "blue", "green"]
        get_game().take_input("black")
        self.assertEqual(len(get_game().player_code), 4)
        self.assertEqual(get_game().player_code, ["red", "blue", "green", "black"])

    def test_bulls_and_cows(self):
        bulls, cows = 0, 0
        secret_code = ["red", "blue", "green", "black"]
        guess = ["red", "blue", "green", "black"]
        bulls, cows = get_game().count_bulls_and_cows(secret_code, guess)
        self.assertEqual(bulls, 4)

        guess = ["red", "blue", "black", "green"]
        bulls, cows = get_game().count_bulls_and_cows(secret_code, guess)
        self.assertEqual(bulls, 2)
        self.assertEqual(cows, 2)

        guess = ["purple", "purple", "purple", "purple"]
        bulls, cows = get_game().count_bulls_and_cows(secret_code, guess)
        self.assertEqual(bulls, 0)
        self.assertEqual(cows, 0)


# def main():
if __name__ == '__main__':
    unittest.main(verbosity=3)


# main()
