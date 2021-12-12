from graphics import *

p1_ship_grid = Grid()
p1_hit_grid = Grid()
p2_ship_grid = Grid()
p2_hit_grid = Grid()


def move(player):
    sq = input(f"Which square will Player {player} hit? (ex. F5) ")
    letter = 0
    if sq[0] == "A":
        letter = 0
    elif sq[0] == "B":
        letter = 1
    elif sq[0] == "C":
        letter = 2
    elif sq[0] == "D":
        letter = 3
    elif sq[0] == "E":
        letter = 4
    elif sq[0] == "F":
        letter = 5
    elif sq[0] == "G":
        letter = 6
    elif sq[0] == "H":
        letter = 7
    elif sq[0] == "I":
        letter = 8
    elif sq[0] == "J":
        letter = 9

    if player == 1:
        p1_hit_grid.grid[letter, int(sq[1])] = "X"
    else:
        p2_hit_grid.grid[letter, int(sq[1])] = "X"


def main():
    console_setup()
    p1_hit_grid.display_grid()
    move(1)
    clear_screen()
    p1_hit_grid.display_grid()


if __name__ == "__main__":
    main()
