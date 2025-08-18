# MASTERMIND project

MASTERMIND is a Python terminal codebreaker game for children, students and adults alike looking for a classic, strategic problem-solving activity. Users are challenged to crack a hidden code in up to 8 attempts, trying combinations of 4 pegs in 6 possible colours and receiving feedback to refine their guesses. The game runs in the Code Institute mock terminal on Heroku and hopes to offer players a fun logical- and critical thinking exercise in a familiar context.

The program is aimed at lovers of board games and logic puzzles and would appeal to users of any age who might benefit from building resilience as well as strategic planning and reasoning skills in a single-player, turn-based, untimed environment.

<!-- Screenshot of deployed app -->

## How to play

MASTERMIND is based on the classic board game. You can read more about its origins here:

In this version, when the player runs the program the peg board is displayed under some instructions – these explain the aim of the game and include keys indicating how the pegs are represented.

To evoke the tactile appeal of the physical game, the ‘holes’ for the guess pegs are represented in rows as ‘ o ‘ placeholders and for the feedback pegs in adjacent grids as ‘ . ’ placeholders – a visual reminder of the attempts remaining.

- A randomly generated secret peg code of 4 colours – including possible repeats – is hidden behind ‘x x x x’ at the top of the board.

- The player starts making guesses from the bottom row upwards by entering a series of 4 single-spaced numbers between 1 and 6 which are displayed as the corresponding peg colours (abbreviated).

- For each guess, feedback is given in the form of a randomly positioned black ‘B’ marker for any peg that was guessed in the correct colour and correct position in the secret code and a white ‘W’ marker for any peg that was guessed in the correct colour but wrong position in the secret code.

- The player wins the game if they can deduce and reveal the secret code before running out of guesses.

## Features
### Flowchart
<!-- Screenshot of flowchart -->

## Testing
### Bugs

## Development & Deployment

- The site was built using Visual Studio Code connected to GitHub via the steps below:
    - Created a local project folder in VS Code
    - Opened the Code Institute template repository on GitHub
        - Used to support deployment of a web-hosted version of the project with essential front end components
    - Selected the ‘Create a new repository' from the ‘Use this template’ dropdown menu
    - After assigning the project name, cloned the repository by:
        - Opening ‘<> Code’ and copying the new repository’s url
        - Opening a new terminal in VS Code, entering ‘git clone’, the pasted url and ‘.’
    - This created a local copy of the project and initialised git, connecting the workspace to the remote repository

- A virtual environment (to run in its own space with the right tools/packages unable to interfere with any other projects) was created and activated via the steps below:
    - Chose ‘Python: Create environment...’ from the VS Code command palette
    - Selected ‘Venv’, ‘Python 3.13.6’ and confirmed selection of ‘requirements.txt’ to install dependencies
    -  Added ‘.venv’ to the ‘.gitignore’ file to exclude the virtual environment folder from version control, preventing large or unnecessary files from being uploaded to GitHub

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


<!-- - The live link can be found here:   -->

## Credits


