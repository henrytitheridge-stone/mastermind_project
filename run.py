import random


def generate_secret_code(colours):
    """
    Returns a list of 4 random choices (allowing for repeats)
    from the list of 6 guessable colours.
    """
    return random.choices(colours, k=4)


class Board:
    """
    A class to represent the mastermind board state.
    """

    def __init__(self):
        pass

    def display_current_board(self, secret_code, guess_pegs, feedback_pegs):
        """
        Display the game instructions and progress on the board,
        including the hidden/revealed code, guessed codes, feedback
        and remaining attempts.
        """

        line = "------------------------------------------"
        instructions_title = "Instructions"
        game_title = "MASTERMIND"

        print(line)
        print(instructions_title.center(42))
        print(line)

        print("Enter these numbers to guess the secret code:")
        print("1 = RED, 2 = ORANGE, 3 = YELLOW, 4 = GREEN, 5 = BLUE, 6 = PURPLE")
        print("W = a peg was guessed in the correct colour")
        print("B = a peg was guessed in the correct colour AND position")

        print(line)
        print()
        print(game_title.center(42))
        print(line)

        print("      |   ", end="")
        for x in secret_code:
            print(x, end="     ")

        print()

        for i in range(8):
            print(line)
            print("|", feedback_pegs[i][0], feedback_pegs[i][1], "|")
            print("|", feedback_pegs[i][2], feedback_pegs[i][3], end=" |   ")

            for x in guess_pegs[i]:
                print(x, end="     ")
            print()

        print(line)


def validate_player_input(guess_pegs, guess, colours_dict):
    """
    Asks the player to enter a guess and if the input is 4 numbers
    between 1 and 6 (with spaces), updates the guess pegs by matching
    the inputted numbers to their corresponding colours in the
    colours dictionary.
    """
    while True:
        try:
            player_input = list(map(int, input("Enter your guess (duplicates permitted): ").split()))

            if len(player_input) != 4:
                print("Please enter 4 numbers between 1 and 6, with spaces (duplicates permitted).")
                continue
            else:
                for i in range(4):
                    guess_pegs[guess][i] = colours_dict[player_input[i]]

            return player_input

        except ValueError:
            print("Please enter 4 numbers between 1 and 6, with spaces (duplicates permitted).")
            continue


# def show_feedback():


# def play_mastermind():


colours = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE"]
colours_dict = {1: "RED", 2: "ORANGE", 3: "YELLOW", 4: "GREEN", 5: "BLUE", 6: "PURPLE"}
guess_pegs = [[" o ", " o ", " o ", " o "] for _ in range(8)]
feedback_pegs = [[".", ".", ".", "."] for _ in range(8)]
guess = 0
secret_code = generate_secret_code(colours)
print(secret_code)
board = Board()
board.display_current_board(secret_code, guess_pegs, feedback_pegs)
validate_player_input(guess_pegs, guess, colours_dict)
board.display_current_board(secret_code, guess_pegs, feedback_pegs)
