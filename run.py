import random

# Global variables
grid = [[]]
size_of_grid = 10
ships_in_game = 8
ship_positions = [[]]
ships_sunk = 0
turns_left = 50
game_finished = False


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