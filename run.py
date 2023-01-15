# Global variables
grid = [[]]
size_of_grid = 10
ships_placed = 8
ship_positions = [[]]
ships_sunk = 0
turns_left = 50
game_finished = False

def main():
    """ Function that runs the game loop """

    print("-----------------------------")
    print("Welcome to Battleships!")
    print("Can you destroy the 8 enemy ships within 50 shots?")
    print("X is a hit, # is a miss, . is unknown")
    print("Fire at will!")
    print("-----------------------------")

main()