import random

# Global variables
grid = [[]]
size_of_grid = 10
ships_in_game = 8
ship_positions = [[]]
ships_sunk = 0
turns_left = 50
game_finished = False
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def attempt_placing_ship(start_r, end_r, start_c, end_c):
    """ Places a ship on the board, but only 
        if another ship is not occupying the space needed """
    global grid
    global ship_positions

# Checks space required for ship is all empty
    place_ship_here = True
    for r in range(start_r, end_r):
        for c in range(start_c, end_c):
            if grid[r][c] != ".":
                place_ship_here = False
                break

# Places a ship if space is available
    if place_ship_here:
        ship_positions.append([start_r, end_r, start_c, end_c])
        for r in range(start_r, end_r):
            for c in range(start_c, end_c):
                grid[r][c] = "O"
    return place_ship_here    


def check_ship_fits(row, column, direction, size):
    """ Check that the ship infomation generated fits onto the game grid """
    global size_of_grid

    start_r, end_r, start_c, end_c = row, row + 1, column, column + 1

    if direction == "up":
        if row - size < 0:
            return False
        start_r = row - size + 1

    elif direction == "down":
        if row + size >= size_of_grid:
            return False
        end_r = row + size

    elif direction == "left":
        if column - size < 0:
            return False
        start_c = column - size + 1

    elif direction == "right":
        if column + size >= size_of_grid:
            return False
        end_c = column + size

    return attempt_placing_ship(start_r, end_r, start_c, end_c)


def create_starting_grid():
    """ Creates a 10 x 10 grid for the game to be played on """ 
    global size_of_grid
    global grid
    global ship_positions
    global ships_in_game

# Creating the grid itself
    rows, columns = (size_of_grid, size_of_grid)

    grid = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(".")
        grid.append(row)

# Generates random positioning for the ships until all are placed
    ships_placed = 0
    ship_positions = []

    while ships_placed != ships_in_game:
        ran_row = random.randint(0, rows - 1)
        ran_column = random.randint(0, columns - 1)
        ran_direction = random.choice(["up", "down", "left", "right"])
        ran_size = random.randint(2, 5)

# Sends randomized ship infomation to be validated
        if check_ship_fits(ran_row, ran_column, ran_direction, ran_size):
            ships_placed += 1


def print_grid():
    """ Will print the 10 x 10 game grid with rows (A-J) and columns (0-9) """
    global grid
    global alphabet

# Enables ships to be seen to test they are correctly placed
    grid_testing = False

# Slices alphabet string to the required length
    alphabet = alphabet[0: len(grid) + 1]

# Adds letters down the left side of grid
    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for column in range(len(grid[row])):
            if grid[row][column] == "O":
                if grid_testing:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][column], end=" ")
        print("")

# Adds numbers along the bottom edge of the grid
    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def valid_missile_choice():
    """ Returns a valid set of co-ordinates to fire upon """
    global grid
    global alphabet
    global size_of_grid

    valid_choice = False
    row = -1
    column = -1

    while valid_choice is False:
        placement_choice = input("Enter row (A-J) and column (0-9) such as F6: \n")
        placement_choice = placement_choice.upper()
# Ensures input is the correct length        
        if len(placement_choice) <= 1 or len(placement_choice) > 2:
            print("Error: Please enter 1 row (A-J) and 1 column (0-9)")
            continue
# Ensures a letter and number are entered in the input
        row = placement_choice[0]
        column = placement_choice[1]
        if not row.isalpha() or not column.isnumeric():
            print("Error: Please enter a letter (A-J) and a number (0-9)")
            continue
# Ensures letter entered is within grid size
        row = alphabet.find(row)
        if not (-1 < row < size_of_grid):
            print("Error: Please enter a letter (A-J) and a number (0-9)")
            continue
# Ensures number entered is within grid size
        column = int(column)
        if not (-1 < column < size_of_grid):
            print("Error: Please enter a letter (A-J) and a number (0-9)")
            continue
# Ensures input hasn't already been chosen by user
        if grid[row][column] == "X" or grid[row][column] == "#":
            print("You have already sent a missile here, please pick again")
            continue
# Confirms valid input 
        if grid[row][column] == "." or grid[row][column] == "O":
            valid_choice = True

    return row, column


def fire_missile():
    """ Fires missile at selected spot on grid and updates accordingly """
    global grid
    global ships_sunk

    row, column = valid_missile_choice()


def main():
    """ Function that runs the game loop """
    global game_finished

    print("-----------------------------")
    print("Welcome to Battleships!")
    print("Can you destroy the 8 enemy ships within 50 shots?")
    print("X is a hit, # is a miss, . is unknown")
    print("Fire at will!")
    print("-----------------------------")

    create_starting_grid()

    # while game_finished is False:
        
    print_grid()
    print(" ")
    print("You have " + str(turns_left) + " missiles remaining!")
    print(str(ships_in_game - ships_sunk) + " enemy ships remain!")
    fire_missile()

main()