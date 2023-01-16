import random

# Global variables
grid = [[]]
size_of_grid = 10
ships_in_game = 8
ship_positions = [[]]
ships_sunk = 0
turns_left = 50
game_finished = False


def attempt_placing_ship(start_row, end_row, start_column, end_column):
    """ Places a ship on the board if another ship is not occupying the space needed """
    global grid
    global ship_positions

# Checks space required for ship is all empty
    place_ship_here = True
    for r in range(start_row, end_row):
        for c in range(start_column, end_column):
            if grid[r][c] != ".":
                place_ship_here = False
                break

# Places a ship if space is available
    if place_ship_here:
        ship_positions.append([start_row, end_row, start_column, end_column])
        for r in range(start_row, end_row):
            for c in range(start_column, end_column):
                grid[r][c] = "O"
    return place_ship_here    


def check_ship_fits(random_row, random_column, random_direction, random_size):
    """ Check that the ship infomation generated fits onto the game grid """
    global size_of_grid

    start_row, end_row, start_column, end_column = random_row, random_row + 1, random_column, random_column + 1

    if random_direction == "up":
        if random_row - random_size < 0:
            return False
        start_row = random_row - random_size + 1

    elif random_direction == "down":
        if random_row + random_size >= size_of_grid:
            return False
        end_row = random_row + random_size

    elif random_direction == "left":
        if random_column - random_size < 0:
            return False
        start_column = random_column - random_size + 1

    elif random_direction == "right":
        if random_column + random_size >= size_of_grid:
            return False
        end_column = random_column + random_size

    return attempt_placing_ship(start_row, end_row, start_column, end_column)


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
        random_row = random.randint(0, rows - 1)
        random_column = random.randint(0, columns - 1)
        random_direction = random.choice("up", "down", "left", "right")
        random_size = random.randint(2, 5)

# Sends randomized ship infomation to be validated
        if check_ship_fits(random_row, random_column, random_direction, random_size)
            ships_placed += 1


def main():
    """ Function that runs the game loop """

    print("-----------------------------")
    print("Welcome to Battleships!")
    print("Can you destroy the 8 enemy ships within 50 shots?")
    print("X is a hit, # is a miss, . is unknown")
    print("Fire at will!")
    print("-----------------------------")

    create_starting_grid()

main()