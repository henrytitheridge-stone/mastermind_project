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

    def display_current_board(self, guess_pegs, feedback_pegs):
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


# def validate_player_input():


# def show_feedback():


# def play_mastermind():


colours = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE"]
guess_pegs = [[" o ", " o ", " o ", " o "] for _ in range(8)]
feedback_pegs = [[".", ".", ".", "."] for _ in range(8)]
secret_code = generate_secret_code(colours)
print(secret_code)
board = Board()
board.display_current_board(guess_pegs, feedback_pegs)
