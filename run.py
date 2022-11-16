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

def create_ships(board):
    """
    Creates random locations for 5 single-cell battleships.
    While loop confirms if the space is unavailable/occupied.
        if true: another random location is selected.
        if false: the value 'X' is assigned to the co-ordinate in the hidden board
    repeats the for loop until all 5 ships are assigned unique locations.
    """
    for ship in range(5):
        ship_row = randint(0,7)
        ship_column = randint(0,7)
        while board[ship_row][ship_column] == 'x':
            ship_row,ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'x'


create_ships(HIDDEN_BOARD)

print('Hidden board')
print_board(HIDDEN_BOARD)
print('')
print('Guess board')
print_board(GUESS_BOARD)