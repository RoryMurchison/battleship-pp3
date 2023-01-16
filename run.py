import random

# Global variables
grid = [[]]
size_of_grid = 10
ships_in_game = 8
ship_positions = [[]]
ships_sunk = 0
turns_left = 50
game_finished = False


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

# Place the ships to be guessed on the grid
    ships_placed = 0
    ship_positions = []

    while ships_placed != ships_in_game:
        random_row = random.randint(0, rows - 1)
        random_column = random.randint(0, columns - 1)
        random_direction = random.choice("up", "down", "left", "right")
        random_length = random.randint(2, 5)



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