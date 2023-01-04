# ROCK PAPER SCISSORS

Rock Paper Scissors is a Python terminal game that runs on Heroku.

The user plays against the computer by choosing between rock, paper and scissors. Their choice is then compared against the computer's random choice, and the result is shown. The score is uploaded to an external Google sheet and then printed to the terminal. 

[Here](https://rock-paper-scissors.herokuapp.com/) is the live version of the "rock paper scissors" app.

![amIresponsive-image](/assets/readme-images/amiresponsive.png)

## HOW TO PLAY

Rock Paper Scissors is based on the classic Rock Paper Scissors game. You can learn more about it on [this Wikipedia page.](https://en.wikipedia.org/wiki/Rock_paper_scissors)

The rules are the following:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock

The user is first asked to pick a unique username. They then have to make their choice between rock, paper or scissors by typing the word rock, paper or scissors. The program compares their answer with the computer's randomly generated choice and returns whether it's a tie, a win or a loss. 

A tie awards no points, a win awards 1 point to the user and a loss awards 1 point to the computer. The score is then displayed to the user.

The user is asked if they want to play again and can communicate their decision to the program by typing "y" or "n" in terminal. 

## FEATURES

### Chart: 

![chart-image](/assets/readme-images/chart.png)

### Playing the game:

- The program asks the user for a unique username.
- Then, welcomes the new user and displays the rules.
- Then, asks the user to pick one of the three options.

![username-image](/assets/readme-images/username.png)

- Once the user has made their choice:
    - The program generates the computer's choice, compares it to the user's choice and returns the result of this round.
    - The program calculates, updates and prints the score to the terminal.
    - The program asks the user if they wish to play another round. 

![results-image](/assets/readme-images/results.png)

- If the user picks "y", a new round begins
- If the user picks "n", a thank you message is displayed and the program is exited

![exit-image](/assets/readme-images/exit.png)

### User input validation:

- The user cannot input an empty username.

![blank-image](/assets/readme-images/blank.png)

- The user cannot input an existing username.
- If they do, they are prompted to choose another username.

![taken-image](/assets/readme-images/taken.png)

- The user cannot input a choice other than "rock", "paper" or "scissors"
- Any space is removed before and after the user's input
- User's input is automatically converted to lowercase

![incorrect-input-image](/assets/readme-images/input.png)

## DATA MODEL

The "rock paper scissors" app integrates with Google sheets. 
The score is uploaded to a new worksheet of the connected spreadsheet every time the user or the computer scores a point.
The score for each player is then read in the worksheet, summed and printed in terminal after each round.

## TESTING

 - I have manually tested this project by doing the following:
    - Passed the code through a PEP8 linter and confirmed there were no problems
    - Given invalid inputs, including blank inputs or existing usernames 
    - Tested in my local terminal as well as in Heroku's terminal

### Bugs:

- ### Solved bugs:  

    - Entering a blank username was crashing the program since a worksheet couldn't be created. I was able to fix it by adding extra validation preventing the user from submitting a blank username or a username composed only of spaces.

    - Entering an existing username was crashing the program since two worksheets cannot have the same name in Google sheets. I was able to fix it by adding an exception handler prompting the user to pick a different username. 

- ### Remaining bugs:  

    - No remaining bugs.

- ### Validator testing:

    - PEP8:
        - No errors were returned on the [CI Python Linter](https://pep8ci.herokuapp.com/):
    
    ![linter-image](/assets/readme-images/linter.png)

## DEPLOYMENT

This project was deployed using Heroku.

- Fork or Clone the Repository:
    - To Fork the Repository:
        - Log into GitHub and locate the repository
        - Click on "Fork" in the top right corner
        - Select "Create Fork"

    - To create a local Clone:
        - Log into GitHub and locate the repository
        - Open the "Code" drop-down menu in the top right corner
        - Copy the URL from under the HTTPS tab
        - In your IED, open Terminal
        - Change the current working directory to the location where you want the cloned directory
        - Type git clone, and then paste the URL you copied earlier
        - Press "Enter" to create your local clone

- To deploy on Heroku:
    - Create a new Heroku app
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on "Deploy"

## CREDITS

- [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/)