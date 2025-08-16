# def generate_secret_code():


class Board:

    def __init__(self):
        pass

    def display_current_board(self, guess_pegs, feedback_pegs):
        line = "------------------------------------------"
        print(line)
        print("Instructions")
        print(line)


# def validate_player_input():


# def show_feedback():


# def play_mastermind():


colours = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE"]
guess_pegs = [["o", "o", "o", "o"] * 8]
feedback_pegs = [[".", ".", ".", "."] * 8]
board = Board()
board.display_current_board(guess_pegs, feedback_pegs)
