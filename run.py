from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]#The grid which maps the ship locations
GUESS_BOARD = [[' '] * 8 for x in range(8)]#The grid which marks the player's previous guesses
turns = 20

def print_board(board):
    """
    Displays the guess board in the terminal
    Adds headings and row numbers
    """
    print('  A B C D E F G H') #initial empty spaces in string are to allow letters and columns align
    print(' ==================') #divider for headers/cells. Purely aesthetic.
    row_number = 1
    for row in board:
        print(f'{row_number}|'+'|'.join(row)+'|')
        row_number += 1

print('Hidden board')
print_board(HIDDEN_BOARD)

print('Guess board')
print_board(GUESS_BOARD)