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
    global grid
    global size_of_grid
    global ships_in_game
    global ship_positions

    rows, columns = (size_of_grid, size_of_grid)

    grid = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(".")
        grid.append(row)



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