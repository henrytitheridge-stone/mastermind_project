# def generate_secret_code():


class Board:

    def __init__(self):
        pass

    def display_current_board(self, guess_pegs, feedback_pegs):
        line = "------------------------------------------"
        print(line)
        print("Instructions")
        print(line)
        print("Enter these numbers to guess the secret code:")
        print("1 = RED, 2 = ORANGE, 3 = YELLOW, 4 = GREEN, 5 = BLUE, 6 = PURPLE")
        print("W = a peg was guessed in the correct colour")
        print("B = a peg was guessed in the correct colour AND position")
        print(line)
        print("MASTERMIND")
        print(line)

        for i in range(8):
            print(line)
            print(feedback_pegs[i][0], feedback_pegs[i][1])
            print(feedback_pegs[i][2], feedback_pegs[i][3], end="     ")

            for x in guess_pegs[i]:
                print(x, end="     ")
            print()

        print(line)


# def validate_player_input():


# def show_feedback():


# def play_mastermind():


colours = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE"]
guess_pegs = [["o", "o", "o", "o"] for _ in range(8)]
feedback_pegs = [[".", ".", ".", "."] for _ in range(8)]
board = Board()
board.display_current_board(guess_pegs, feedback_pegs)
