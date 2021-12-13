from graphics import *

p1_ship_grid = Grid()
p1_hit_grid = Grid()
p2_ship_grid = Grid()
p2_hit_grid = Grid()

spots_used = []

# Places an 'X' in the desired spot of the user
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


# This method sets the ships to the proper spots on the 'board' (or grid) depending on what the user inputs
def set_ships(player):

    # Sets Aircraft Carrier position
    j = 0
    # Calls the data_validation method to get input from user and validate it
    place = data_validation(player, "Aircraft Carrier")
    # Converts the letter to an integer to make it compatable with arrays
    letter = set_letter(place[0].upper())
    hv = input("Which direction do you want to put the ship? ((H)orizontal or (V)ertical): ")
    indicator = 0
    while indicator != 2:
        # If the user inputs "HORIZONTAL" or "H"...
        if hv.upper() == "HORIZONTAL" or hv.upper() == "H":
            # Ask them if they want the ship to lay left or right
            direction = input("Left or right? ")
            # If left, check to see if it's a valid move (meaning it doesn't go off the board)
            if direction.upper() == "LEFT":
                indicator = 0
                # This for statement goes through the squares the ship would take up and see if it falls within the array's size
                for h in range(5):
                    if int(place[1]) - h != 0:
                        pass
                    # If the phrase above == 0 and h does not equal four then flip the switch (var indicator in this case)
                    elif h != 4:
                        indicator = 1
                        break
                # If the switch from the previous statement is flipped then give the error message...
                if indicator == 1:
                    # And ask the user for another option to try
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "RIGHT":
                        direction = "RIGHT"
                    else:
                        direction = ""
                else:
                    indicator = 2

            elif direction.upper() == "RIGHT":
                indicator = 0
                for h in range(5):
                    # This one differs a little bit compared to going left because an array only has so much size as defined
                    # in the graphics.py file. Because of this, instead of checking to see if the previous equation equaled 0,
                    # we have to use the try and catch method because an exception would occur if we tried to access elements outside
                    # the array's size
                    try:
                        p1_ship_grid.grid[letter, int(place[1]) + h]
                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "LEFT":
                        direction = "LEFT"
                    else:
                        direction = ""
                else:
                    indicator = 2

        if hv.upper() == "VERTICAL" or hv.upper() == "V":
            direction = input("Up or down? ")
            if direction.upper() == "UP":
                indicator = 0
                for h in range(5):
                    if letter - h != 0:
                        pass
                    elif h != 4:
                        indicator = 1
                        break
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "DOWN":
                        direction = "DOWN"
                    else:
                        direction = ""
                else:
                    indicator = 2

            elif direction.upper() == "DOWN":
                indicator = 0
                for h in range(5):
                    try:
                        p1_ship_grid.grid[letter + h, int(place[1])]
                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "UP":
                        direction = "UP"
                    else:
                        direction = ""
                else:
                    indicator = 2

    if direction.upper() == "LEFT":
        temp = place[1]
        for h in range(5):
            p1_ship_grid.grid[letter, int(place[1])-h] = "C"
            if h != 0:
                temp = int(temp)-1
            spots_used.append(place[0].upper() + str(temp))

    elif direction.upper() == "RIGHT":
        temp = place[1]
        for h in range(5):
            p1_ship_grid.grid[letter, int(place[1])+h] = "C"
            if h != 0:
                temp = int(temp)+1
            spots_used.append(place[0].upper() + str(temp))

    elif direction.upper() == "UP":
        temp = place[0]
        for h in range(5):
            p1_ship_grid.grid[letter-h, int(place[1])] = "C"
            if h != 0:
                temp = chr(ord(temp.upper()) - 1)
            spots_used.append(temp.upper() + place[1])

    elif direction.upper() == "DOWN":
        temp = place[0]
        for h in range(5):
            p1_ship_grid.grid[letter+h, int(place[1])] = "C"
            if h != 0:
                temp = chr(ord(temp.upper()) + 1)
            spots_used.append(temp.upper() + place[1])

    p1_ship_grid.display_grid()


    # Sets Battleship position
    j = 0
    place = data_validation(player, "Battleship")
    letter = set_letter(place[0].upper())
    hv = input("Which direction do you want to put the ship? ((H)orizontal or (V)ertical): ")

    indicator = 0
    while indicator != 2:
        if hv.upper() == "HORIZONTAL" or hv.upper() == "H":
            direction = input("Left or right? ")
            if direction.upper() == "LEFT":
                indicator = 0
                for h in range(4):
                    if int(place[1]) - h != 0:
                        pass
                    elif h != 3:
                        indicator = 1
                        break
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "RIGHT":
                        direction = "RIGHT"
                    else:
                        direction = ""
                else:
                    indicator = 2

            elif direction.upper() == "RIGHT":
                indicator = 0
                for h in range(4):
                    try:
                        p1_ship_grid.grid[letter, int(place[1]) + h]
                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "LEFT":
                        direction = "LEFT"
                    else:
                        direction = ""
                else:
                    indicator = 2

        if hv.upper() == "VERTICAL" or hv.upper() == "V":
            direction = input("Up or down? ")
            if direction.upper() == "UP":
                indicator = 0
                for h in range(4):
                    if letter - h != 0:
                        pass
                    elif h != 3:
                        indicator = 1
                        break
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "DOWN":
                        direction = "DOWN"
                    else:
                        direction = ""
                else:
                    indicator = 2

            elif direction.upper() == "DOWN":
                indicator = 0
                for h in range(4):
                    try:
                        p1_ship_grid.grid[letter + h, int(place[1])]
                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "UP":
                        direction = "UP"
                    else:
                        direction = ""
                else:
                    indicator = 2

    if direction.upper() == "LEFT":
        temp = place[1]
        for h in range(4):
            p1_ship_grid.grid[letter, int(place[1]) - h] = "B"
            if h != 0:
                temp = int(temp) - 1
            spots_used.append(place[0].upper() + str(temp))
            print(spots_used)

    elif direction.upper() == "RIGHT":
        temp = place[1]
        for h in range(4):
            p1_ship_grid.grid[letter, int(place[1]) + h] = "B"
            if h != 0:
                temp = int(temp) + 1
            spots_used.append(place[0].upper() + str(temp))
            print(spots_used)

    elif direction.upper() == "UP":
        temp = place[0]
        for h in range(4):
            p1_ship_grid.grid[letter - h, int(place[1])] = "B"
            if h != 0:
                temp = chr(ord(temp.upper()) - 1)
            spots_used.append(temp.upper() + place[1])
            print(spots_used)

    elif direction.upper() == "DOWN":
        temp = place[0]
        for h in range(4):
            p1_ship_grid.grid[letter + h, int(place[1])] = "B"
            if h != 0:
                temp = chr(ord(temp.upper()) + 1)
            spots_used.append(temp.upper() + place[1])
            print(spots_used)

    p1_ship_grid.display_grid()


    # Sets Cruiser position
    j = 0
    place = data_validation(player, "Cruiser")
    letter = set_letter(place[0].upper())
    hv = input("Which direction do you want to put the ship? ((H)orizontal or (V)ertical): ")

    indicator = 0
    while indicator != 2:
        if hv.upper() == "HORIZONTAL" or hv.upper() == "H":
            direction = input("Left or right? ")
            if direction.upper() == "LEFT":
                indicator = 0
                for h in range(3):
                    if int(place[1]) - h != 0:
                        pass
                    elif h != 2:
                        indicator = 1
                        break
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "RIGHT":
                        direction = "RIGHT"
                    else:
                        direction = ""
                else:
                    indicator = 2

            elif direction.upper() == "RIGHT":
                indicator = 0
                for h in range(3):
                    try:
                        p1_ship_grid.grid[letter, int(place[1]) + h]
                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "LEFT":
                        direction = "LEFT"
                    else:
                        direction = ""
                else:
                    indicator = 2

        if hv.upper() == "VERTICAL" or hv.upper() == "V":
            direction = input("Up or down? ")
            if direction.upper() == "UP":
                indicator = 0
                for h in range(3):
                    if letter - h != 0:
                        pass
                    elif h != 2:
                        indicator = 1
                        break
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "DOWN":
                        direction = "DOWN"
                    else:
                        direction = ""
                else:
                    indicator = 2

            elif direction.upper() == "DOWN":
                indicator = 0
                for h in range(3):
                    try:
                        p1_ship_grid.grid[letter + h, int(place[1])]
                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "UP":
                        direction = "UP"
                    else:
                        direction = ""
                else:
                    indicator = 2

    if direction.upper() == "LEFT":
        temp = place[1]
        for h in range(3):
            p1_ship_grid.grid[letter, int(place[1])-h] = "R"
            if h != 0:
                temp = int(temp)-1
            spots_used.append(place[0].upper() + str(temp))
            print(spots_used)

    elif direction.upper() == "RIGHT":
        temp = place[1]
        for h in range(3):
            p1_ship_grid.grid[letter, int(place[1])+h] = "R"
            if h != 0:
                temp = int(temp)+1
            spots_used.append(place[0].upper() + str(temp))
            print(spots_used)

    elif direction.upper() == "UP":
        temp = place[0]
        for h in range(3):
            p1_ship_grid.grid[letter-h, int(place[1])] = "R"
            if h != 0:
                temp = chr(ord(temp.upper()) - 1)
            spots_used.append(temp.upper() + place[1])
            print(spots_used)

    elif direction.upper() == "DOWN":
        temp = place[0]
        for h in range(3):
            p1_ship_grid.grid[letter+h, int(place[1])] = "R"
            if h != 0:
                temp = chr(ord(temp.upper()) + 1)
            spots_used.append(temp.upper() + place[1])
            print(spots_used)

    p1_ship_grid.display_grid()


    # Sets Submarine position
    j = 0
    place = data_validation(player, "Submarine")
    letter = set_letter(place[0].upper())
    hv = input("Which direction do you want to put the ship? ((H)orizontal or (V)ertical): ")

    indicator = 0
    while indicator != 2:
        if hv.upper() == "HORIZONTAL" or hv.upper() == "H":
            direction = input("Left or right? ")
            if direction.upper() == "LEFT":
                indicator = 0
                for h in range(3):
                    if int(place[1]) - h != 0:
                        pass
                    elif h != 4:
                        indicator = 1
                        break
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "RIGHT":
                        direction = "RIGHT"
                    else:
                        direction = ""
                else:
                    indicator = 2

            elif direction.upper() == "RIGHT":
                indicator = 0
                for h in range(3):
                    try:
                        p1_ship_grid.grid[letter, int(place[1]) + h]
                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "LEFT":
                        direction = "LEFT"
                    else:
                        direction = ""
                else:
                    indicator = 2

        if hv.upper() == "VERTICAL" or hv.upper() == "V":
            direction = input("Up or down? ")
            if direction.upper() == "UP":
                indicator = 0
                for h in range(3):
                    if letter - h != 0:
                        pass
                    elif h != 4:
                        indicator = 1
                        break
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "DOWN":
                        direction = "DOWN"
                    else:
                        direction = ""
                else:
                    indicator = 2

            elif direction.upper() == "DOWN":
                indicator = 0
                for h in range(3):
                    try:
                        p1_ship_grid.grid[letter + h, int(place[1])]
                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "UP":
                        direction = "UP"
                    else:
                        direction = ""
                else:
                    indicator = 2

    if direction.upper() == "LEFT":
        temp = place[1]
        for h in range(3):
            p1_ship_grid.grid[letter, int(place[1]) - h] = "S"
            if h != 0:
                temp = int(temp) - 1
            spots_used.append(place[0].upper() + str(temp))
            print(spots_used)

    elif direction.upper() == "RIGHT":
        temp = place[1]
        for h in range(3):
            p1_ship_grid.grid[letter, int(place[1]) + h] = "S"
            if h != 0:
                temp = int(temp) + 1
            spots_used.append(place[0].upper() + str(temp))
            print(spots_used)

    elif direction.upper() == "UP":
        temp = place[0]
        for h in range(3):
            p1_ship_grid.grid[letter - h, int(place[1])] = "S"
            if h != 0:
                temp = chr(ord(temp.upper()) - 1)
            spots_used.append(temp.upper() + place[1])
            print(spots_used)

    elif direction.upper() == "DOWN":
        temp = place[0]
        for h in range(3):
            p1_ship_grid.grid[letter + h, int(place[1])] = "S"
            if h != 0:
                temp = chr(ord(temp.upper()) + 1)
            spots_used.append(temp.upper() + place[1])
            print(spots_used)

    p1_ship_grid.display_grid()


    # Sets Destroyer position
    j = 0
    place = data_validation(player, "Destroyer")
    letter = set_letter(place[0].upper())
    hv = input("Which direction do you want to put the ship? ((H)orizontal or (V)ertical): ")

    indicator = 0
    while indicator != 2:
        if hv.upper() == "HORIZONTAL" or hv.upper() == "H":
            direction = input("Left or right? ")
            if direction.upper() == "LEFT":
                indicator = 0
                for h in range(2):
                    if int(place[1]) - h != 0:
                        pass
                    elif h != 4:
                        indicator = 1
                        break
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "RIGHT":
                        direction = "RIGHT"
                    else:
                        direction = ""
                else:
                    indicator = 2

            elif direction.upper() == "RIGHT":
                indicator = 0
                for h in range(2):
                    try:
                        p1_ship_grid.grid[letter, int(place[1]) + h]
                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "LEFT":
                        direction = "LEFT"
                    else:
                        direction = ""
                else:
                    indicator = 2

        if hv.upper() == "VERTICAL" or hv.upper() == "V":
            direction = input("Up or down? ")
            if direction.upper() == "UP":
                indicator = 0
                for h in range(2):
                    if letter - h != 0:
                        pass
                    elif h != 4:
                        indicator = 1
                        break
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "DOWN":
                        direction = "DOWN"
                    else:
                        direction = ""
                else:
                    indicator = 2

            elif direction.upper() == "DOWN":
                indicator = 0
                for h in range(2):
                    try:
                        p1_ship_grid.grid[letter + h, int(place[1])]
                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                    if hv.upper() == "UP":
                        direction = "UP"
                    else:
                        direction = ""
                else:
                    indicator = 2

    if direction.upper() == "LEFT":
        temp = place[1]
        for h in range(5):
            p1_ship_grid.grid[letter, int(place[1]) - h] = "D"
            if h != 0:
                temp = int(temp) - 1
            spots_used.append(place[0].upper() + str(temp))
            print(spots_used)

    elif direction.upper() == "RIGHT":
        temp = place[1]
        for h in range(2):
            p1_ship_grid.grid[letter, int(place[1]) + h] = "D"
            if h != 0:
                temp = int(temp) + 1
            spots_used.append(place[0].upper() + str(temp))
            print(spots_used)

    elif direction.upper() == "UP":
        temp = place[0]
        for h in range(2):
            p1_ship_grid.grid[letter - h, int(place[1])] = "D"
            if h != 0:
                temp = chr(ord(temp.upper()) - 1)
            spots_used.append(temp.upper() + place[1])
            print(spots_used)

    elif direction.upper() == "DOWN":
        temp = place[0]
        for h in range(2):
            p1_ship_grid.grid[letter + h, int(place[1])] = "D"
            if h != 0:
                temp = chr(ord(temp.upper()) + 1)
            spots_used.append(temp.upper() + place[1])
            print(spots_used)

    p1_ship_grid.display_grid()


# Checks to see if the position the user inputted is either not given in the right format (ex. 'A' or 'F123'),
# Also checks to see if another ship occupies the desired space using the 'check' method
def data_validation(player, ship_type):
    place = input(f"Which square will Player {player} put the {ship_type}? (ex. F5) ")
    while len(place) != 2:
        place = input(f"Either too short or too long. Which square will Player {player} put the {ship_type}? (ex. F5) ")
    while check(place.upper()):
        place = input(
            f"That square has already been taken. Which square will Player {player} put the {ship_type}? (ex. F5) ")
        while len(place) != 2:
            place = input(
                f"Either too short or too long. Which square will Player {player} put the {ship_type}? (ex. F5) ")
    return place


# If any strings in spot_used equals the parameters passed in, it will return true then print an error message
def check(spot):
    for i in spots_used:
        if spot == i:
            return True
    return False


# Sets the letter passed in to a number and returns it
def set_letter(letter):
    if letter == "A":
        l = 0
    elif letter == "B":
        l = 1
    elif letter == "C":
        l = 2
    elif letter == "D":
        l = 3
    elif letter == "E":
        l = 4
    elif letter == "F":
        l = 5
    elif letter == "G":
        l = 6
    elif letter == "H":
        l = 7
    elif letter == "I":
        l = 8
    elif letter == "J":
        l = 9
    return l


def main():
    console_setup()
    p1_ship_grid.display_grid()
    set_ships(1)
    p1_ship_grid.display_grid()
    spots_used.clear()
    p2_ship_grid.display_grid()
    set_ships(2)
    p2_ship_grid.display_grid()


if __name__ == "__main__":
    main()
