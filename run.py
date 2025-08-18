import random
import os


def generate_secret_code(colours):
    """
    Returns a list of 4 random choices (allowing for repeats)
    from the list of 6 guessable peg colours.
    """
    return random.choices(colours, k=4)


def display_current_board(secret_code, guess_pegs, guess, feedback_pegs):
    """
    Displays the game instructions and progress on the board,
    including the hidden/revealed code, guessed codes, feedback
    and remaining attempts.
    """
    line = "------------------------------------------"

    print(line)
    print("Instructions".center(42))
    print(line)

    print("Enter numbers to guess the pegs in the 'x x x x' code:")
    print("1 = RED, 2 = ORANGE, 3 = YELLOW, 4 = GREEN, 5 = BLUE, 6 = PURPLE")
    print("|B| = a peg was guessed in the correct colour AND position")
    print("|W| = a peg was guessed in the correct colour, NOT position")

    print(line)
    print()
    print("MASTERMIND".center(42))
    print(line)

    print("      |   ", end="")
    # Lines up secret code pegs horizontally
    for x in secret_code:
        print(x[:3], end="     ")
        # if secret_code in guess_pegs or guess == 8:
        #     print(x[:3], end="     ")
        # else:
        #     print(" x ", end="     ")

    print()

    # Creates 2x2 grid for feedback pegs, first guess at the bottom
    for i in reversed(range(8)):
        print(line)
        print("|", feedback_pegs[i][0], feedback_pegs[i][1], "|")
        print("|", feedback_pegs[i][2], feedback_pegs[i][3], end=" |   ")

        # Lines up guessed codes next to feedback
        for x in guess_pegs[i]:
            print(x[:3], end="     ")
        print()

    print(line)


def validate_player_input(guess_pegs, guess, colours_dict):
    """
    Inside the try, converts strings into a list of integers.
    Raises ValueError if strings cannot be converted into integers.
    Displays error messages if more or less than 4 numbers are entered or
    if any of the numbers are outside the 1-6 range.

    Updates the guess pegs by matching the valid input numbers to their
    corresponding colours in the colours dictionary.
    """
    while True:
        try:
            player_input = [int(x) for x in (input("Enter your guess (colours "
                                                   "may be repeated): "
                                                   ).split())]

            # Checks that 4 separated digits have been inputted
            if len(player_input) != 4:
                print("Please enter exactly 4 numbers, with spaces.")
                continue

            # Checks that inputted numbers are in the valid 1-6 range
            invalid_range = False
            for x in player_input:
                if x < 1 or x > 6:
                    invalid_range = True
                    break
            if invalid_range:
                print("Please only enter numbers between 1 and 6, "
                      "with spaces.")
                continue
            else:
                for i in range(4):
                    guess_pegs[guess][i] = colours_dict[player_input[i]]

            return player_input

        except ValueError:
            # Displays if any inputted values are not numbers
            print("Please enter numbers only, with spaces.")
            continue


def show_feedback(guess_pegs, guess, feedback_pegs, secret_code):
    """
    Checks each player guess against the secret code and updates
    feedback pegs for pegs guessed in the correct colour AND position and
    those guessed in the correct colour only.
    """
    secret_copy = secret_code.copy()  # Preserves secret code throughout game
    running_score = [".", ".", ".", "."]
    marked_secret_pegs = [False] * (len(secret_copy))

    for i in range(len(secret_copy)):
        # Checks for guessed pegs matching the colour AND position
        # of pegs in the secret code
        if guess_pegs[guess][i] == secret_code[i]:
            running_score[i] = "B"
            # Then blocks the peg in that position in the secret code
            # from being included in checks for colour matches
            marked_secret_pegs[i] = True

    for i in range(len(secret_copy)):
        # Checks for any guessed pegs matching a colour of any unmarked pegs
        # remaining (ie weren't in the right position) in the secret code
        if running_score[i] != "B":
            for j in range(len(secret_copy)):
                if (not marked_secret_pegs[j] and
                        guess_pegs[guess][i] == secret_copy[j]):
                    running_score[i] = "W"
                    # Then blocks that secret peg from matching any
                    # subsequent pegs guessed in the same colour
                    marked_secret_pegs[j] = True
                    break

    # Shuffles feedback pegs to reflect original reasoning challenge
    random.shuffle(running_score)
    feedback_pegs[guess] = running_score


def play_mastermind():
    """
    Initiates guess count, secret code, default board and
    runs all functions in the main game loop.
    """
    colours = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE"]
    colours_dict = {1: "RED", 2: "ORANGE", 3: "YELLOW",
                    4: "GREEN", 5: "BLUE", 6: "PURPLE"}
    guess_pegs = [[" o ", " o ", " o ", " o "] for _ in range(8)]
    feedback_pegs = [[".", ".", ".", "."] for _ in range(8)]

    def update_board():
        """
        Clear terminal and display board including
        up-to-date guess and feedback pegs.
        """
        os.system("cls" if os.name == "nt" else "clear")
        display_current_board(secret_code, guess_pegs, guess, feedback_pegs)

    secret_code = generate_secret_code(colours)
    guess = 0

    while guess < 8:
        update_board()
        validate_player_input(guess_pegs, guess, colours_dict)
        show_feedback(guess_pegs, guess, feedback_pegs, secret_code)

        if guess_pegs[guess] == secret_code:  # WIN message
            update_board()
            print("Well done! You cracked the code!")
            break

        guess += 1

        if guess == 8:  # LOSS message
            update_board()
            print("Bad luck! You have run out of guesses.")
            break


def start_game():
    """
    Loops running the game, ending each round by giving the player
    the ability to stop or start again.
    """
    while True:
        play_mastermind()

        play_again = input("Would you like to play again? (Y/N): ").upper()
        while play_again not in ("Y", "N"):
            # Repeats request for valid input
            print("Please enter Y or N.")
            play_again = input("Would you like to play again? (Y/N): ").upper()

        if play_again == "N":  # Ends program
            break

    print("Thanks for playing!")


start = start_game()
