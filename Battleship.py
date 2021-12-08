grid = []

def make_grid():
    inside_grid = []
    for i in range(10):
        for j in range(10):
            inside_grid.append("*")
        grid.append(inside_grid)
        inside_grid = []

    for i in range(1, 11):
        if i == 1:
            print(f"   {i}  ", end="")
        else:
            print(f"{i}  ", end="")
    print()

    x = 'A'
    count2 = 0
    for i in range(1, 11):
        count1 = 0
        print(f"{x}  ", end="")
        for j in range(10):
            print(f"{grid[count1][count2]}  ", end="")
            count1 += 1
        count2 += 1
        print()
        x = chr(ord(x) + 1)

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
    grid[int(sq[1:])-1][letter] = "X"

def main():
    make_grid()
    move()
    make_grid()

main()
