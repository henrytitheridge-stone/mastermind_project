# MASTERMIND project

MASTERMIND is a Python terminal codebreaker game for children, students and adults alike looking for a classic, strategic problem-solving activity. Users are challenged to crack a hidden code in up to 8 attempts, trying combinations of 4 pegs in 6 possible colours and receiving feedback to refine their guesses. The game runs in the Code Institute mock terminal on Heroku and hopes to offer players a fun logical- and critical thinking exercise in a familiar context.

The program is aimed at lovers of board games and logic puzzles and would appeal to users of any age who might benefit from building resilience and reasoning skills in a single-player, turn-based, untimed environment.

<!-- Screenshot of deployed app -->

## How to play

MASTERMIND is based on the classic board game. You can read more about its origins here: [Wikipedia - Mastermind (board game)](https://en.wikipedia.org/wiki/Mastermind_(board_game))

In this version, when the player runs the program the peg board is displayed under some instructions – these explain the aim of the game and include keys indicating how the pegs are represented.

To evoke the tactile appeal of the physical game, the ‘holes’ for the guess pegs are represented in rows as ‘ o ‘ placeholders and for the feedback pegs in adjacent grids as ‘ . ’ placeholders – a visual reminder of the attempts remaining.

- A randomly generated secret peg code of 4 colours – including possible repeats – is hidden behind ‘x x x x’ at the top of the board.

- The player starts making guesses from the bottom row upwards by entering a series of 4 single-spaced numbers between 1 and 6 which are displayed as the corresponding peg colours (abbreviated).

- For each guess, feedback is given in the form of a randomly positioned black ‘B’ marker for any peg that was guessed in the correct colour and correct position in the secret code and a white ‘W’ marker for any peg that was guessed in the correct colour but wrong position in the secret code.

- The player wins the game if they can deduce and reveal the secret code before running out of guesses.

## Features
### Flowchart
The main game logic is shown here:
<!-- Screenshot of flowchart -->

The program initiates a main game function which sets the guess count to 0 and generates a secret code of colours. This is achieved through the use of 'random.choices()' to return a list of 4 colours (chosen from a list of 6), allowing for repeats. Nested within the main function, the rest of the game's functions are contained in a while loop, limiting the player to 8 guesses:

#### Updating the board
<!-- Screenshot of initial board -->
- Before every guess the update_board function clears the terminal and prints the current mastermind board, including the generated secret code which the player sees only as 'x x x x'.
- The design of the board reflects the original game, displaying 8 rows of 4 peg 'holes' for guesses and adjacent feedback pegs separated by '|' and '-' lines.
- After each guess the update_board function 'adds' the guessed colours and feedback pegs for the player to track their progress

#### Accepting an input
- Presented with the board and 'number:colour' key, the player is now asked to input a guess of 4 numbers with spaces, and reminded that colours may be repeated.
- Each input is run through a try-except validation statement, first raising a ValueError if any non-numeric characters are entered.
    - This is achieved by splitting the entries into indivual strings, converting them to integers and returning them in a list like this:
        ```
        player_input = [int(x) for x in (input("Enter your guess (colours may be repeated): \n").split())]
        ```
- If statements then check for any guesses of more or less than 4 items and any numbers outside the 1-6 range
<!-- Screenshots of error messages -->
- Valid guesses are then matched to their colour dictionary values and made ready to be 'added' as pegs on the board:
    ```
    for i in range(4):
        guess_pegs[guess][i] = colours_dict[player_input[i]]
    ```

#### Marking each guess
- The mechanics of the show_feedback function loops will be detailed further in the bugs and fixes sections below but from the player's point of view:
    - If any of the pegs from their guess code matched the colour AND position as one in the secret code, a 'B' is given as feedback for each perfect match.
    - If any of the remaining, unmatched pegs from their guess match in colour (NOT position) with any remaining, unmatched pegs in the secret code, a 'W' is given as feedback
- The feedback pegs are then made ready to be 'added' to the board after being shuffled so that their position in the grid would not reveal specific matches
<!-- Screenshot of feedback grid -->

#### Win and loss conditions
- To begin the next iteration - ie clear the terminal and update the board - checks occur for the win and loss conditions:
    - If statements check firstly if the players guess and secret code are a perfect match, leading to a success message and breaking the game loop or else adding 1 to the guess count
    - Then if the guess count has reached 8, ie without the code being cracked, a bad luck message is printed and the game loop is stopped
<!-- Screenshots of win/loss messages -->
- Both the win and loss conditions reveal the secret code and last guess feedback in a final board update

### Start/finish
- The main game function is itself called from within a while loop, generating a new secret code and resetting the board for a new round if the player opts to play again:
    - At the end of each round (defined by the win and loss conditions above), the player is asked to enter 'Y' or 'N' to restart or end the program.
    - This input is validated by using the 'upper()' function to accept 'y' or 'n' and repeating the input request after anything other than 'Y' or 'N' is attempted:
    ```
    while True:
        play_mastermind()

        play_again = input("Would you like to play again? (Y/N): \n").upper()
        while play_again not in ("Y", "N"):
            # Repeats request for valid input
            print("Please enter Y or N.")
            play_again = input("Would you like to play again? "
                               "(Y/N): \n").upper()

        if play_again == "N":  # Ends program
            break

    print("Thanks for playing!")
    ```
#### Future features
- Give a multiplayer option by adding functionality for players to input their own secret code
- Make visuals more engaging by adding a colour library to display peg/colour names in matching colours
- Experiment with layout to fit original feedback grids into the terminal

## Testing
I have manually tested the features of this project in the VS Code and deployed Heroku terminals by:
- Using the PEP8-aligned 'Flake8' Python linter extension in VS Code to address problems throughout development
    - FIXED: E501 errors flagged (lines > 79 characters) and continuation lines were added  
- Entering invalid inputs: strings instead of numbers, none or more than 4 numbers, numbers without spaces and numbers out of the 1-6 range to confirm all correct prompts displayed
- Playing through rounds of the game to confirm that:
    - the secret code remains hidden as 'x x x x' until a win/loss condition is triggered
    - the guessed numbers are correctly displayed as the expected colours
    - the terminal is cleared and board updated successfully after each guess
    - the feedback peg positions are randomised (by repeating guesses)
    - the feedback accurately marks the perfect and colour-only matches without double counting
    - the win/loss message and 'play again' input request is displayed after each game and...
        - that invalid inputs here (other than Y, y, N or n) display a prompt to try again
        - that an input of Y leads to a new game, board and secret code being generated
        - and an input of N ends the program with the "Thanks for playing!" message

### Bugs and fixes
#### Feedback
To check the accuracy of the feedback mechanism, the secret code was made visible throughout testing. The following succession of revisions were made to address misleading feedback:
- For a secret code of 'PUR, YEL, GRE, ORA', if a player guessed a colour more than once, eg 'RED, YEL, BLU, YEL' the original solution would generate a 'B' for their first YEL - in the right place - AND a 'W' for their second YEL as the YEL in the secret code was checked for again:
    ```
    for i in range(4):
        if guess_codes[guess][i] == secret_code[i]:
            feedback_pegs[guess][i] = "B"
        elif guess_codes[guess][i] in secret_code:
            feedback_pegs[guess][i] = "W"
    ```
- To stop players from unwittingly believing that 2 of their guesses were present in the secret code instead of just the one, the checks were refactored to include a 'marked' set which was intended to stop any perfectly matched pegs from being used in colour-only checks:
    ```
    marked = set()
    for i in range(4):
        if guess_codes[guess][i] == secret_code[i]:
            feedback_pegs[guess][i] = "B"
            marked.add(guess_codes[guess][i])
            continue
        if guess_codes[guess][i] in secret_code and guess_codes[guess][i] not in marked:
            feedback_pegs[guess][i] = "W"
            marked.add(guess_codes[guess][i])
            continue
    ```
- This led to unmarked guess pegs where matches came after the same colour had already been given a 'B' for a perfect match.
    - For example, a secret code of 'RED, ORA, RED, YEL' and a guess of 'RED, RED, RED, RED' would receive just one 'B' instead of 2.
    - In that example a guess of 'RED, ORA, GRE, RED' would also just receive one 'B' without the extra 'W' it warranted.
- FIXED: a boolean list was introduced in order to register the secret positions (rather than the guessed positions or colours) as marked after every match by:
    - checking for and 'locking in' perfect matches before...
    - iterating through those left of the unmatched secret code AND guess pegs to check for colour-only matches.
    ```
    secret_copy = secret_code.copy()  # Preserves secret code throughout game
    running_score = [".", ".", ".", "."]
    marked_secret_pegs = [False] * (len(secret_copy))

    for i in range(len(secret_copy)):
        if guess_pegs[guess][i] == secret_code[i]:
            running_score[i] = "B"
            marked_secret_pegs[i] = True

    for i in range(len(secret_copy)):
        if running_score[i] != "B":
            for j in range(len(secret_copy)):
                if (not marked_secret_pegs[j] and
                        guess_pegs[guess][i] == secret_copy[j]):
                    running_score[i] = "W"
                    marked_secret_pegs[j] = True
                    break
    ```
    - From the example above (secret='RED, ORA, RED, YEL'), for that guess of 'RED, RED, RED, RED', this solution now correctly provides an output of 'B B . .' and for 'RED, ORA, GRE, RED' an output of '. B W B' where the second RED is still shown as present but in the wrong position.

#### Other fixes
- The original logic to reveal the secret code if the latest guess matched the secret code or the guess count reached 8, threw an index error after an 8th guess as the guess_pegs list of 8 lists is zero indexed:
    ```
    if guess_pegs[guess] == secret_code:
    ```
- FIXED: rearranged the condition to reveal the secret code after an 8th guess if the secret code itself matched ANY of the guess_pegs lists:
    ```
    if secret_code in guess_pegs or guess == 8:
    ```
- The 'os.system("cls if os.name == "nt" else "clear")' command was sufficient to clear the terminal in VS Code but not in the Code Institute Heroku mock terminal where the game board would be partially reprinted above each full reprint.
- FIXED: included line below in clear_terminal function to refresh the mock terminal:
    ```
    print("\033c", end="")
    ```

### Validator testing
- PEP8:
    - No errors were returned from pep8ci.herokuapp.com

## Development & Deployment

- The site was built using Visual Studio Code connected to GitHub via the steps below:
    - Created a local project folder in VS Code
    - Opened the deployment-ready Code Institute template repository on GitHub
    - Selected the ‘Create a new repository' from the ‘Use this template’ dropdown menu
    - Assigned the project name and cloned the repository by:
        - Opening ‘<> Code’ and copying the new repository’s url
        - Running a new terminal in VS Code, entering ‘git clone’, the pasted url and ‘.’
    - This created a local copy and initialised git, connecting the workspace to the repository

- A virtual environment was created and activated via the steps below:
    - Chose ‘Python: Create environment...’ from the VS Code command palette
    - Selected ‘Venv’, ‘Python 3.13.6’ and ‘requirements.txt’ to install dependencies
    - Added ‘.venv’ to the ‘.gitignore’ file to exclude it from version control

- Throughout the project, changes made in VS Code were regularly saved and shared by:
    - Entering 'git add .' into a terminal to stage all changes
    - Entering 'git commit -m' with a succinct summary message to commit the changes
    - Entering 'git push' to push all local changes to the project's remote GitHub repository

- The site has been deployed to Heroku via the steps below:
    - Created a new app with the project name from the Heroku dashboard
    - Opened the Settings tab in the new app
    - Added the following buildpacks in this order: ‘heroku/python’ and ‘heroku/nodejs’.
    - Added a single config var with a key set to ‘PORT’ and value set to ‘8000’.
    - Selected the ‘Connect to GitHub’ deployment method in the Deploy tab
    - Searched for and selected the project repository name to establish the connection
    - Enabled automatic deploys to rebuild the app after each push to GitHub
    - Above the tabs bar an 'Open app' link was provided to the hosted site


<!-- - The live link can be found here:   -->

## Credits

- Methods to clear the terminal from [Geeks for Geeks](https://www.geeksforgeeks.org/python/clear-screen-python/) and [OnlineGDB](https://question.onlinegdb.com/12248/how-do-you-clear-the-output-in-python-3)
- Random choices, centring titles, using 'end=' parameters, copying lists and looping using a list comprehension from [W3Schools](https://www.w3schools.com/python/default.asp) 
- Mastermind board layout, reversed range method and word abbreviation from [AskPython](https://www.askpython.com/python/examples/create-mastermind-game-in-python)
- Inspiration for using a boolean list to exclude matched items between lists from subsequent checks from [studytonight.com](https://www.studytonight.com/post/python-check-if-given-two-lists-have-any-element-in-common#:~:text=Asked%20Questions(FAQs)-,1.,element%20membership%20in%20the%20other.) and [finxter.com](https://blog.finxter.com/5-best-ways-to-return-a-boolean-array-for-string-suffix-matches-in-python/)

- Flowchart created using [draw.io](https://www.drawio.com/)
- Deployment terminal from Code Institute
- Mastermind game details from Wikipedia
