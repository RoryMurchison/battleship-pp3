# Battleships

This game of battleship takes inspiration from the classic boardgame and puts its own spin on it. This version of battleship is played within a Python terminal, which runs in the Code Institute mock terminal on Heroku. Designed as a single player game, the user must find all the computers randomly placed ships (2-5 in length), within their given amount of turns.

## How To Play

The user will be presented with a grid consisting of ".".
The "." is used to represent an area of the grid which is unknown.
Enemy ships have been placed randomly on this board but are hidden to the user.
The user will then proceed to be prompted to guess a set of coordinates on the grid.
Assuming the guess is valid, the game will then reveal if you have hit or miss an enemy ship.
A "#" will be used to represent a missed attempt.
A "X" will be used to represent a hit.
A running counter will show how many more ships are left to sink and how many turns remain.
If all ships are sunk before you run out of turns, then you win!

## Features

### Existing Features

    - Randomised board generated
  
         - Ships of random length are placed randomly onto the grid.
         - The ships positioning is hidden to the user so as not to ruin the game.

    - Legend 

        - A legend printed before the grid informs the user what the symbols mean.

![image displaying welcome text and initial game grid](/assets/images/battle-1.png) 

    - Accepts user input

    - Input validation and error checking

        - You can't enter coordinates outside the grid.
        - You can't enter coordinates unless in proper format (eg. letter then number, f6).
        - You can't enter coordinates you have already guessed.

![image displaying input validation](/assets/images/battle-2.png) 

    - Dynamic scoring

        - Text is available that details turns remaining and how many ships need to be sunk to win.
        - This text automatically updates with each turn.

    - Grid reprints

        - After each turn the grid reprints with the updated information for the user.

![image displaying up to date grid and dynamic scoring](/assets/images/battle-3.png)

### Future Features

    - Allow player to determine variables such as grid size, number of ships to be guessed and turns available.

## Data Model

Within this code, I primarily relied on the use of global variables and functions.
A main function ran the game code, calling other functions when necessary.
Once the game was set up, a while loop was used to repeat the functions needed for the turns until the game was finished.

## Testing

I have manually tested this project by:

    - Running and playing the game in the local terminal.
    - Given inputs expected to fail so as to ensure correct error messages show.
    - Run the code through a Python Linter which confirmed no problems with the code.

### Validator Testing

    - No errors were found using a PEP8 Python validator.

![image displaying the code in the validator showing no errors](/assets/images/python-v.png)

## Bugs

### Solved Bugs

    - The terminal got stuck in an infinite loop printing the grid due to the print grid function being the only code in a True while statement which was resolved by commenting out the statement during development.
    - Fired missiles didn't update the grid as == was used as opposed to = in the code that updated the grid.
    - The code wasn't generating random ship placement everytime it was run and so the random was linked to time to help this.

### Unsolved Bugs

    - No bugs remaining.

## Deployment

This project was deployed using Code Institutes mock terminal for Heroku.
   
    - Deployment steps

        - Create a new Heroku app
        - Add config var with key: PORT and value: 8000
        - Add buildpacks Python and NodeJS in that order
        - Link the Heroku app to the repository
        - Deploy

## Credits

    - Code Institute for the deployment terminal
