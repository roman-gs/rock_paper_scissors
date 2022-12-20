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
        print(f'You chose {user}')
    else:
        print("Your input is incorrect...")
        get_user_answer()
        
def get_computer_answer():
    global computer
    computer = random.choice(["rock", "paper", "scissors"])
    print(f'Your opponent chose {computer}')

def play_game(user, computer):
    if user == computer:
        print('Its a tie')

    if (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        print('You won')

    else:
        print('You lost')

get_user_answer()
get_computer_answer()
play_game(user, computer)

    


