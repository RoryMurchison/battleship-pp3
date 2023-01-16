import random

# Global variables
grid = [[]]
size_of_grid = 10
ships_in_game = 8
ship_positions = [[]]
ships_sunk = 0
turns_left = 50
game_finished = False


def check_ship_fits(random_row, random_column, random_direction, random_size):
    """ Check that the ship infomation generated fits onto the game grid """
    global size_of_grid

    start_row, end_row, start_col, end_col = random_row, random_row + 1, random_column, random_column + 1

    if random_direction == "up":
        if random_row - random_size < 0:
            return False
        start_row = random_row - random_size + 1

    elif random_direction == "down":
        if random_row + random_size >= size_of_grid:
            return False
        end_row = random_row + random_size


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