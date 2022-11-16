from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]#The grid which maps the ship locations
GUESS_BOARD = [[' '] * 8 for x in range(8)]#The grid which marks the player's previous guesses

TURNS = 20
letters_to_numbers = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}


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

def guess_location():
    """
    Prompts the player to input a row number.
    Then prompts the player to input a column heading, converts to uppercase.
    Repeats the request if the input is not in the expected range.
    function returns the input as a tuple of (row,column)
    """
    row = input(f'Please enter a row from 1 to 8: \n')
    while str(row) not in '12345678':
        print('Please enter a valid row')
        row = input(f'Please enter a row from 1 to 8: \n')
    
    column = input(f'Please enter a column from A to H: \n').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input(f'Please enter a column from A to H: \n').upper()

    return (row,column)

def check_guess(row,column):
    """
    Checks to see if the passed arguments are already marked on the GUESS_BOARD
        if so, the player is asked to select another location
        turns is NOT incremented
    Otherwise, the HIDDEN_BOARD is checked for a ship
        if present, the GUESS_BOARD is marked with 'x' to show a hit.
        if absent, the GUESS_BOARD is marked with a '-' to show a miss.
        hit or miss, turns is incremented 
    row number starts at 1, and so is reduced by one in function to match zero indexing.
    *A dictionary 'letters_to_numbers' is used to convert column letters to index numbers
    """
    try:
        if GUESS_BOARD[int(row) - 1][letters_to_numbers[column]] == '-' or GUESS_BOARD[int(row) - 1][letters_to_numbers[column]] == 'x':
            print('\n You cannot target the same location more than once.\n please choose again.')
            guess_location()

        elif HIDDEN_BOARD[int(row) - 1][letters_to_numbers[column]] == 'x':
            print('\n Hit! You sunk a battleship!')
            GUESS_BOARD[int(row) - 1][letters_to_numbers[column]] = 'x'
            increment_turns()
            print_board(GUESS_BOARD)

        else:
            print(f'\n Miss. There is no battleship at this location.{row}{column}')
            GUESS_BOARD[int(row) - 1][letters_to_numbers[column]] = '-'
            increment_turns()
            print_board(GUESS_BOARD)
    except ValueError:
        print('Please add a valid target location')
        guess_location()
    except KeyError:
        print('Please add both a valid row AND column')
        guess_location()
    except IndexError:
        print('Please select a row between 1 and 8')
        guess_location()
def increment_turns():
    """
    Reduces global variable turns by 1 each time it is called
    prints turns remaining before game over.
    """
    global TURNS
    TURNS -= 1
    print(f'Turns remaining: {TURNS}')

def count_hit_ships(board):
    """
    Counts the number of 'x' marks on the argument board.
    Checks each cell, of each row individually using nested for loops.
    returns the total number of 'x'.
    Is the victory condition for the player.
    """
    count = 0
    for row in board:
        for cell in row:
            if cell == 'x':
                count += 1
    return count

def new_game():
    """
    Restarts the game without exiting the program
    """
    replay = input('Would you like to play again? (y/n): \n')
    if replay.upper() == 'Y':
        global HIDDEN_BOARD 
        HIDDEN_BOARD = [[' '] * 8 for x in range(8)]#The grid which maps the ship locations
        global GUESS_BOARD 
        GUESS_BOARD = [[' '] * 8 for x in range(8)]#The grid which marks the player's previous guesses
        global TURNS
        TURNS = 20
        main()
    elif replay.upper() == 'N':
        exit()
    else:
        new_game()

def main():
    """
    Runs all primary functions
    While loop repeatedly runs guess_location > check_guess
        the while loop is broken when turns is equal to zero,
        or if the number of 'x' marks on GUESS_BOARD is 5 or greater.
    game ends when the loop is broken.
    """
    print('\nWelcome to battleships')
    print(f'You have {TURNS} to sink all 5 ships.')
    create_ships(HIDDEN_BOARD)
    print_board(GUESS_BOARD)
    while TURNS > 0:
        guess_row,guess_column = guess_location()
        check_guess(guess_row,guess_column)
        if count_hit_ships(GUESS_BOARD) >= 5:
            print ('\nYou hit all battleships. You win!')
            break
        elif TURNS == 0:
            print('\nGame Over, you ran out of turns')
            print('Ship Locations')
            print_board(HIDDEN_BOARD)
            break
        
    new_game()
main()