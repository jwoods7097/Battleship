import numpy as np
import os


# Standard DOS terminal size for that old-school feel
def console_setup():
    os.system("mode con: cols=80 lines=25")
    clear_screen()


# Display title ASCII art and authors
def print_title():
    file = open("title.txt", "r")
    print(file.read())
    file.close()


# Run the right clear command depending on what OS the user is using
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print_title()

class Grid:
    GRID_SIZE = 10

    def __init__(self):
        self.grid = np.array([['·' for i in range(Grid.GRID_SIZE)] for j in range(Grid.GRID_SIZE)])

    def display_grid(self):
        print()

        # Print column numbers
        for i in range(Grid.GRID_SIZE):
            if i == 0:
                print(f"   {i}  ", end="")
            else:
                print(f"{i}  ", end="")
        print()

        letter = 'A'
        for i in range(Grid.GRID_SIZE):
            # Print row letters
            print(f"{letter}  ", end="")

            # Print rows from grid
            for j in range(Grid.GRID_SIZE):
                print(f"{self.grid[i, j]}  ", end="")
            print()

            letter = chr(ord(letter) + 1)
        print()