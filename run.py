import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('battleships_sheet')

player = SHEET.worksheet('Player')
player_data = player.get_all_values()
cp = SHEET.worksheet('COM') #cp is short for Computer Player
cp_data = cp.get_all_values()
player_guess = SHEET.worksheet('Player_guess') #The player's previous guesses
player_guess_data = player_guess.get_all_values()

def display_board():
    """
    Display the current state of the game board.
    Keeps computer ship locations hidden.
    """
    print("Player's Board")
    [print(rows) for rows in player_data]
    print("\n COM's Board")
    [print(rows) for rows in player_guess_data]
    print('\nLegend: "-" = blank, "O" = Occupied tile, "X" = Miss, "H" = Hit\n')

display_board()