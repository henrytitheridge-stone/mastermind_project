import random
import os


def generate_secret_code(colours):
    """
    Returns a list of 4 random choices (allowing for repeats)
    from the list of 6 guessable peg colours.
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
        # Line up secret code pegs horizontally
        for x in secret_code:
            print(x, end="     ")
        print()

        # Create 2x2 grid for feedback pegs, first guess at the bottom
        for i in reversed(range(8)):
            print(line)
            print("|", feedback_pegs[i][0], feedback_pegs[i][1], "|")
            print("|", feedback_pegs[i][2], feedback_pegs[i][3], end=" |   ")

            # Line up guessed codes next to feedback
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
            # Split numbers (at spaces) into individual strings,
            # convert each to an integer and return in a list
            player_input = list(map(int, input("Enter your guess (colours may be repeated): ").split()))

            # Check that 4 separated digits have been inputted
            if len(player_input) != 4:
                print("Please enter exactly 4 numbers, with spaces.")
                continue

            # Check that inputted numbers are in the valid 1-6 range
            invalid_range = False
            for x in player_input:
                if x < 1 or x > 6:
                    invalid_range = True
                    break
            if invalid_range:
                print("Please only enter numbers between 1 and 6, with spaces.")
                continue
            else:
                # Replace each default guess peg with the colour
                # corresponding to the inputted number for the current guess
                for i in range(4):
                    guess_pegs[guess][i] = colours_dict[player_input[i]]

            return player_input

        except ValueError:
            # Displays if any inputted values are not numbers
            print("Please enter numbers only, with spaces.")
            continue


def show_feedback(guess_pegs, feedback_pegs, secret_code):
    """
    Check each player guess and update feedback pegs for pegs guessed
    in the correct colour AND position and those guessed in the
    correct colour only.
    """
    for i in range(4):
        if guess_pegs[guess][i] == secret_code[i]:
            feedback_pegs[guess][i] = "B"
        elif guess_pegs[guess][i] in secret_code:
            feedback_pegs[guess][i] = "W"
        else:
            continue


# def play_mastermind():


colours = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE"]
colours_dict = {1: "RED", 2: "ORANGE", 3: "YELLOW", 4: "GREEN", 5: "BLUE", 6: "PURPLE"}
guess_pegs = [[" o ", " o ", " o ", " o "] for _ in range(8)]
feedback_pegs = [[".", ".", ".", "."] for _ in range(8)]

guess = 0
secret_code = generate_secret_code(colours)

while guess < 8:
    board = Board()
    board.display_current_board(secret_code, guess_pegs, feedback_pegs)
    validate_player_input(guess_pegs, guess, colours_dict)
    show_feedback(guess_pegs, feedback_pegs, secret_code)
    os.system("cls")

    if guess_pegs[guess] == secret_code:  # WIN message
        os.system("cls")
        board.display_current_board(secret_code, guess_pegs, feedback_pegs)
        print("Well done! You cracked the code!")
        break

    guess += 1

    if guess == 8:  # LOSS message
        os.system("cls")
        board.display_current_board(secret_code, guess_pegs, feedback_pegs)
        print("Bad luck! You have run out of guesses.")
        break
