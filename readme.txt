Overall Design:
    - Intended to run from mastermind_game.py as required
    - Instantiates Controller which houses the colored marbles, check, x, and quit buttons that allow for input.
    - Controller contains instances of Display, Leaderboard and Game and allows for the controller to talk to the
        the components that form the view and the Game which holds all the backend logic for the Model.
    - Draw creates and renders the visual components
    - Run_controller tells the Model to update at the start of the game and also tells turtle to listen for input
Model(Game logic) Design:
    - ALLOWS FOR MULTIPLES OF THE SAME COLOR IN THE SECRET CODE, THE GUESSES, AND IN COUNT_BULLS_AND_COWS
    - Multiples of the same color were received by calling a random integer from 0 - 5 and using it as an index
        to select a color from the colors list
    - Stores player name, a list of leaders, the secret code, the player's guess, the list of colors used in the game,
        a counter to represent the round and marble via a list like so: [round, marble], and whether the game is still
        being played
    - Allows creating, retrieving, and updating of a file that stores information on leaders.
    - Updates the list of guesses so long as it does not already have 4 guesses in it
    - Houses a duplicate of count bulls and cows to meet separation of concerns criteria. There is a function of the
        same name in the mastermind_game.py file to allow for the required testing hooks.
    - Game class was created to prevent test_mastermind_game.py from triggering a build of the entire game with
        display, controller, and logic.
View Design:
    - The display and leaderboard are instructed to instantiate and render themselves by the controller at startup as
        well as on any change that is registered.
    - The display is comprised of 10 Row instances which hold 4 marbles and 4 pegs each. Pegs are just smaller instances
        of the Marble class.
    -  The leaderboard is comprised of a turtle that draws the frame, a turtle that writes the title, and a turtle that
        writes the leaders when called. For the leaders to be displayed a list of lists of score, and username are
        required.
    - Displays the round via a black and red turtle which moves as the round increments
Controller:
    - Starts by telling the display and leaderboard to render themselves as well as telling the game to initiate itself
    - When run_controller is called, the controller starts listening to the user and relays input to the display and
        the model so the display is in sync with the game logic
    - Let's the player know a button has been clicked by flashing the button. THE COLORED BUTTONS DON'T TURN OFF TO
        ALLOW FOR MULTIPLE GUESSES OF THE SAME COLOR.
    -  When the game is won, lost, or quit, disables all of the buttons, and presents a popup, but allows the player to
        continue viewing the screen.
    - ***NOTE*** Due to the nature of how coloring the display is processed, the player cannot click the buttons very fast.
        Doing so will register the click in the model, but there won't be enough time for the display to render it
        before attempting to render the next color on the next marble.
Testing:
    - the test_leaders_file.txt is required for testing the file read/write logic. This is not the file used to create,
        retrieve, and update info on the leaderboard. That is under the name of "leaderboard.txt" as stated in the
        project requirements and will be created on initial boot up of the game.
