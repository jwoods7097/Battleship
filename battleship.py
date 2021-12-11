from graphics import *


def move():
    sq = input("Which square do you want to hit? (ex. F5) ")
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
    grid[letter, int(sq[1])] = "X"


def main():
    make_grid()
    move()
    make_grid()


if __name__ == "__main__":
    main()
