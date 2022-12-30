import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('rock_paper_scissors')


def get_user_name():
    """
    Get the username from the user and creates a worksheet for each new user.
    Username is validated and cannot be blank or match an existing username.
    """
    global DATA_STR
    DATA_STR = input('Please enter your username: \n')
    if len(DATA_STR.strip()) == 0:
        print("Your username should have at least one character")
        main()
    else:
        try:
            SHEET.add_worksheet(title=DATA_STR, rows=1, cols=2)
        except:
            print("This username is already taken, please pick a different one")
            main()

    print(f"Welcome to Rock Paper Scissors, {DATA_STR}\n")
    print("The rules are as follow:\n")
    print("Rock beats scissors")
    print("Scissors beats paper")
    print("Paper beats rock\n")
    # Set the score to 0 - 0
    score = [0, 0]
    SHEET.worksheet(DATA_STR).append_row(score)


def get_user_answer():
    """
    Ask the user to make a choice and validates it
    """
    global USER
    choice = input('Please choose from rock, paper, or scissors: ')
    choice_strip = choice.strip()
    USER = choice_strip.lower()
    if USER == "rock" or USER == "paper" or USER == "scissors":
        print()
        print(f'You chose {USER}')
    else:
        print()
        print("Your input is incorrect...")
        get_user_answer()


def get_computer_answer():
    """
    Generate random computer choice
    """
    global COMPUTER
    COMPUTER = random.choice(["rock", "paper", "scissors"])
    print(f'Your opponent chose {COMPUTER}')


def play_game(USER, COMPUTER): 
    """
    Compare the user and the computer choices
    """
    if USER == COMPUTER:
        print()
        print("It's a tie")
        print()
        calculate_score(DATA_STR)
        play_again()

    if (USER == 'rock' and COMPUTER == 'scissors') or (USER == 'paper' and COMPUTER == 'rock') or (USER == 'scissors' and COMPUTER == 'paper'):
        print()
        print('You won')
        print()
        increment_user_score(DATA_STR)
        calculate_score(DATA_STR)
        play_again()

    else:
        print()
        print('You lost')
        print()
        increment_computer_score(DATA_STR)
        calculate_score(DATA_STR)
        play_again()


def play_again():
    """
    Allow the user to exit the program or keep playing after each result
    """
    answer = input("Do you want to keep playing? y or n ...\n")
    answer_strip = answer.strip()
    answer_lower = answer_strip.lower()
    if answer_lower == "n":
        print(f'\nThanks for playing "rock paper scissors", {DATA_STR}. \n')
        print("This app was developed as part of the 3rd module of a Full Stack Software Development course")
        print("Find my Github repositories here: https://github.com/roman-gs")
        quit()

    if answer_lower == "y":
        get_user_answer()
        get_computer_answer()
        play_game(USER, COMPUTER)
    
    else:
        print()
        print("Your input is incorrect, please choose Y for yes or N for no")
        play_again()


def increment_user_score(DATA_STR): 
    """
    Increment the user score by 1 and the computer score by 0
    """
    new_score = [1, 0]
    SHEET.worksheet(DATA_STR).append_row(new_score)


def increment_computer_score(data_str): 
    """
    Increment the computer score by 1 and the user score by 0
    """
    new_score = [0, 1]
    SHEET.worksheet(DATA_STR).append_row(new_score)


def calculate_score(DATA_STR):
    """
    Calculate the user and computer scores
    """
    print("Calculating score...")
    current_user_score = SHEET.worksheet(DATA_STR).col_values(1)
    # Convert str in the "current_user_score" list to int 
    # Cred: https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    current_user_score_int = [eval(i) for i in current_user_score]
    user_score = sum(current_user_score_int)

    current_computer_score = SHEET.worksheet(DATA_STR).col_values(2)
    current_computer_score_int = [eval(i) for i in current_computer_score]
    computer_score = sum(current_computer_score_int)

    print(f'Score is: {DATA_STR} {user_score}, computer {computer_score} \n')


def main():
    """
    Call all program functions
    """
    get_user_name()
    get_user_answer()
    get_computer_answer()
    play_game(USER, COMPUTER)


main()
