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


def get_user_name(): #Get the username from the user and creates a worksheet for each new user
    global data_str
    data_str = input('Please enter your username: \n')
    print(f"Welcome to Rock Paper Scissors, {data_str}")
    worksheet = SHEET.add_worksheet(title=data_str, rows=1, cols=2)
    score = [0 ,0] #Set the score to 0 - 0
    SHEET.worksheet(data_str).append_row(score) 

get_user_name()


def get_user_answer(): # Ask for the user choice
    global user
    choice = input('Please choose from rock, paper, or scissors: ')
    choice_strip = choice.strip()
    user = choice_strip.lower()
    if user == "rock" or user == "paper" or user == "scissors": # Validate the user choice
        print()
        print(f'You chose {user}')
    else:
        print()
        print("Your input is incorrect...")
        get_user_answer()
        
def get_computer_answer(): # Generate random computer choice
    global computer
    computer = random.choice(["rock", "paper", "scissors"])
    print(f'Your opponent chose {computer}')

def play_game(user, computer): # Compare the user and the computer choices
    if user == computer:
        print()
        print("It's a tie")
        print()
        calculate_user_score(data_str)
        play_again()

    if (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        print()
        print('You won')
        print()
        increment_user_score(data_str)
        calculate_user_score(data_str)
        play_again()

    else:
        print()
        print('You lost')
        print()
        increment_computer_score(data_str)
        calculate_user_score(data_str)
        play_again()

def play_again(): # Allow the user to exit the program or keep playing after each result
    answer = input("Do you want to keep playing? y or n ...\n")
    answer_strip = answer.strip()
    answer_lower = answer_strip.lower()
    if answer_lower == "n":
        quit()

    if answer_lower == "y":
        get_user_answer()
        get_computer_answer()
        play_game(user, computer)
    
    else:
        print()
        print("Your input is incorrect, please choose Y for yes or N for no")
        play_again()

def increment_user_score(data_str): # Increment the user score by 1
    new_score = [1, 0]
    update_score = SHEET.worksheet(data_str).append_row(new_score)

def increment_computer_score(data_str): # Increment the computer score by 1
    new_score = [0, 1]
    update_score = SHEET.worksheet(data_str).append_row(new_score)

def calculate_user_score(data_str):
    current_score = SHEET.worksheet(data_str).col_values(1)
    current_score_int = [eval(i) for i in current_score] # Convert str in the "current_score" list to int
    user_score = sum(current_score_int)
    print(fuser_score)

get_user_answer()
get_computer_answer()
play_game(user, computer)


    


