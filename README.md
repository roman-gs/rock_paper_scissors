# ROCK PAPER SCISSORS

Rock Paper Scissors is a Python terminal game, which runs in ...

The user plays again the computer by choosing between rock, paper and scissors. Their choice is then compared against the computer's random choice and the result is shown. The score is uploaded to an external Google sheet and then printed to terminal. 

Here is the live version.

## HOW TO PLAY

Rock Paper Scissors is based on the classic Rock Paper Scissors game. You can learn more about it on [this wikipedia page.](https://en.wikipedia.org/wiki/Rock_paper_scissors)

The rules are the following:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock

The user is first asked to pick a unique username. They then have to make their choice between rock, paper or scissors by typing the world rock, paper or scissors. The program compares their answer with the computer's randomly generated choice and return whether it's a tie, a win or a loss. 

A tie awards no points, a win awards 1 point to the user and a loss awards 1 point to the computer. The score is then displayed to the user.

The user is asked if they want to play again and can communicate their decision to the program by typing "y" or "n" in terminal. 

## FEATURES

### Playing the game:

- The program asks the user for a unique username.

![username-image](/assets/readme-images/username.png)

- The program welcomes the new user, displays the rules and ask the user to pick one of the three options.

![options-image](/assets/readme-images/options.png)

- The program generates the computer's choice, compares it to the user's choice and return the result of the game.
- The program calculates, updates and prints the score to terminal
- The program ask the user if they wish to play again 

![results-image](/assets/readme-images/results.png)

### User input validation:

- The user cannot input an empty username.

![empty-image](/assets/readme-images/empty.png)

- The user cannot input an existing username.
- If they do, they are prompted to choose another username.

![taken-image](/assets/readme-images/taken.png)

- The user cannot input a choice other than "rock", "paper" or "scissors"
- Any space is removed before and after the user's choice
- User's input is automatically converted to lowercase

![results-image](/assets/readme-images/results.jpg)

## DATA MODEL

## TESTING

### Bugs:

- ### Solved bugs:  

    - Entering a blank username was crashing the program since a worksheet couldn't be created. I was able to fix it by adding extra validation preventing the user from submitting a blank username or a username composed only by spaces.

    - Entering an existing username was crashing the program since two worksheets cannot have the same name in Google sheets. I was able to fix it by adding an exception handler prompting the user to pick a different username. 

- ### Remaining bugs:  

    - No remaining bugs

- ### Validator testing:

    - PEP8
        - No errors were returned on https://www.pythonchecker.com/ 

## DEPLOYMENT

This project was deployed using ...

    - Steps for deployment:

## CREDITS

    - 