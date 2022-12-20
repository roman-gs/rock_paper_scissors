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

#def get_user_name():
    #"""
    #Get the username from the user and creates a worksheet for each new user
    #"""
    #data_str = input('Please enter your username: \n')
    #print(f"Welcome to Rock Paper Scissors, {data_str}")
    #worksheet = SHEET.add_worksheet(title=data_str, rows=100, cols=20)

#get_user_name()

def get_user_answer():
    global user
    choice = input('Please choose from rock, paper, or scissors: ')
    choice_strip = choice.strip()
    user = choice_strip.lower()
    if user == "rock" or user == "paper" or user == "scissors":
        print()
        print(f'You chose {user}')
    else:
        print()
        print("Your input is incorrect...")
        get_user_answer()
        
def get_computer_answer():
    global computer
    computer = random.choice(["rock", "paper", "scissors"])
    print(f'Your opponent chose {computer}')

def play_game(user, computer):
    if user == computer:
        print()
        print('Its a tie')
        print()
        play_again()

    if (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        print()
        print('You won')
        print()
        play_again()

    else:
        print()
        print('You lost')
        print()
        play_again()

def play_again():
    answer = input("Do you want to keep playing? Y or N...\n")
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

get_user_answer()
get_computer_answer()
play_game(user, computer)


    


