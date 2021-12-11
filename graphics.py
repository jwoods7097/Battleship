import numpy as np

GRID_SIZE = 10
grid = np.array([['*' for i in range(GRID_SIZE)] for j in range(GRID_SIZE)])


def make_grid():
    print()

    # Print column numbers
    for i in range(GRID_SIZE):
        if i == 0:
            print(f"   {i}  ", end="")
        else:
            print(f"{i}  ", end="")
    print()

    letter = 'A'
    for i in range(GRID_SIZE):
        # Print row letters
        print(f"{letter}  ", end="")

        # Print rows from grid
        for j in range(GRID_SIZE):
            print(f"{grid[i, j]}  ", end="")
        print()

        letter = chr(ord(letter) + 1)
    print()
