from graphics import *
from ships import *

p1_ship_grid = Grid()
p1_hit_grid = Grid()
p2_ship_grid = Grid()
p2_hit_grid = Grid()

p1_carrier = Ship(5)
p2_carrier = Ship(5)
p1_battleship = Ship(4)
p2_battleship = Ship(4)
p1_cruiser = Ship(3)
p2_cruiser = Ship(3)
p1_submarine = Ship(3)
p2_submarine = Ship(3)
p1_destroyer = Ship(2)
p2_destroyer = Ship(2)

spots_used = []

p1_spots_attacked = []
p2_spots_attacked = []

for i in range (100):
    p1_spots_attacked.append("null")
    p2_spots_attacked.append("null")
    
def set_ships_init(player, ship_type, ship_type_init, ship_length):
    # Sets Aircraft Carrier position
    j = 0
    # Calls the data_validation method to get input from user and validate it
    place = data_validation(player, ship_type, ship_length)
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
                for h in range(ship_length):
                    if int(place[1]) - h != 0:
                        pass
                    # If the equation above == 0 and h does not equal four then flip the switch (var indicator in this case)
                    elif h != 4:
                        indicator = 1
                        break
                # If the switch from the previous statement is flipped then give the error message...
                if indicator == 1:
                    # And ask the user for another option to try
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                else:
                    temp = place[1]
                    for h in range(ship_length):
                        temp = int(temp) - 1
                        if check(place[0].upper() + str(temp)):
                            indicator = 1
                            break
                        else:
                            indicator = 2
                    if indicator != 2:
                        hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")

            elif direction.upper() == "RIGHT":
                indicator = 0
                for h in range(ship_length):
                    # This one differs a little bit compared to going left because an array only has so much size as defined
                    # in the graphics.py file. Because of this, instead of checking to see if the previous equation equaled 0,
                    # we have to use the try and catch method because an exception would occur if we tried to access elements outside
                    # the array's size
                    try:
                        if (player == 1):
                            p1_ship_grid.grid[letter, int(place[1]) + h]
                        else:
                            p2_ship_grid.grid[letter, int(place[1]) + h]

                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                else:
                    temp = place[1]
                    for h in range(ship_length):
                        temp = int(temp) + 1
                        if check(place[0].upper() + str(temp)):
                            indicator = 1
                            break
                        else:
                            indicator = 2
                    if indicator != 2:
                        hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")

        if hv.upper() == "VERTICAL" or hv.upper() == "V":
            direction = input("Up or down? ")
            if direction.upper() == "UP":
                indicator = 0
                for h in range(ship_length):
                    if letter - h != 0:
                        pass
                    elif h != 4:
                        indicator = 1
                        break
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                else:
                    temp = place[0]
                    for h in range(ship_length):
                        temp = chr(ord(temp.upper()) - 1)
                        if check(temp.upper() + place[1]):
                            indicator = 1
                            break
                        else:
                            indicator = 2
                    if indicator != 2:
                        hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")

            elif direction.upper() == "DOWN":
                indicator = 0
                for h in range(ship_length):
                    try:
                        if (player == 1):
                            p1_ship_grid.grid[letter + h, int(place[1])]
                        else:
                            p2_ship_grid.grid[letter + h, int(place[1])]

                    except:
                        indicator = 1
                if indicator == 1:
                    hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")
                else:
                    temp = place[0]
                    for h in range(ship_length):
                        temp = chr(ord(temp.upper()) + 1)
                        if check(temp.upper() + place[1]):
                            indicator = 1
                            break
                        else:
                            indicator = 2
                    if indicator != 2:
                        hv = input("Cannot be done. Pick another direction: ((V)ertical) or (H)orizontal): ")

    if direction.upper() == "LEFT":
        temp = place[1]
        for h in range(ship_length):
            if (player == 1):
                p1_ship_grid.grid[letter, int(place[1]) - h] = ship_type_init
            else:
                p2_ship_grid.grid[letter, int(place[1]) - h] = ship_type_init

            if h != 0:
                temp = int(temp) - 1
            spots_used.append(place[0].upper() + str(temp))

    elif direction.upper() == "RIGHT":
        temp = place[1]
        for h in range(ship_length):
            if (player == 1):
                p1_ship_grid.grid[letter, int(place[1]) + h] = ship_type_init
            else:
                p2_ship_grid.grid[letter, int(place[1]) + h] = ship_type_init

            if h != 0:
                temp = int(temp) + 1
            spots_used.append(place[0].upper() + str(temp))

    elif direction.upper() == "UP":
        temp = place[0]
        for h in range(ship_length):
            if (player == 1):
                p1_ship_grid.grid[letter - h, int(place[1])] = ship_type_init
            else:
                p2_ship_grid.grid[letter - h, int(place[1])] = ship_type_init

            if h != 0:
                temp = chr(ord(temp.upper()) - 1)
            spots_used.append(temp.upper() + place[1])

    elif direction.upper() == "DOWN":
        temp = place[0]
        for h in range(ship_length):
            if (player == 1):
                p1_ship_grid.grid[letter + h, int(place[1])] = ship_type_init
            else:
                p2_ship_grid.grid[letter + h, int(place[1])] = ship_type_init

            if h != 0:
                temp = chr(ord(temp.upper()) + 1)
            spots_used.append(temp.upper() + place[1])

    if (player == 1):
        p1_ship_grid.display_grid()
    else:
        p2_ship_grid.display_grid()


# This method sets the ships to the proper spots on the 'board' (or grid) depending on what the user inputs
def set_ships(player):

    set_ships_init(player, "Aircraft Carrier", "C", 5)
    set_ships_init(player, "Battleship", "B", 4)
    set_ships_init(player, "Carrier", "R", 3)
    set_ships_init(player, "Submarine", "S", 3)
    set_ships_init(player, "Destroyer", "D", 2)


# Checks to see if the position the user inputted is either not given in the right format (ex. 'A' or 'F123'),
# Also checks to see if another ship occupies the desired space using the 'check' method
def data_validation(player, ship_type, ship_length):
    place = input(f"Which square will Player {player} put the {ship_type} ({ship_length} spaces)? (ex. F5) ")
    while len(place) != 2:
        place = input(f"Either too short or too long. Which square will Player {player} put the {ship_type}? (ex. F5) ")
    while check(place.upper()):
        place = input(
            f"That square has already been taken. Which square will Player {player} put the {ship_type}? (ex. F5) ")
        while len(place) != 2:
            place = input(
                f"Either too short or too long. Which square will Player {player} put the {ship_type}? (ex. F5) ")
    return place

# Gets the attack spot and ensures valid input and that the spot is availiable 
def attack_validation(player):
    place = input(f"Which square will Player {player} attack? (ex. F5) ")
    while len(place) != 2:
        place = input(f"Either too short or too long. Which square will Player {player} attack? (ex. F5) ")
    new_place = convert_to_attack(place)
    while attack_check(player, new_place):
        place = input(
            f"That square has already been attacked. Which square will Player {player} attack? (ex. F5) ")
        while len(place) != 2:
            place = input(
                f"Either too short or too long. Which square will Player {player} attack? (ex. F5) ")
        new_place = convert_to_attack(place)
    return new_place
    
# If any strings in spot_used equals the parameters passed in, it will return true then print an error message
def check(spot):
    for i in spots_used:
        if spot == i:
            return True
    return False
 
# Checks if the spot in the grid has already been attacked 
def attack_check(player, place):
    hit_char = "x"
    miss_char = "o"
    dup = False
    if (player == 1):
        if (p1_spots_attacked[place] == (hit_char or miss_char)):
            dup = True
    else:
        if (p2_spots_attacked[place] == (hit_char or miss_char)):
            dup = True
    return dup

# Converts the attack coordinate to a single number for the hit grids
def convert_to_attack(place):
    one = set_letter(place[0].upper())
    two = int(place[1])
    return ((10*one) + two)
    
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

# Checks for winner
def check_winner():
    if (p1_battleship.check() or p2_battleship.check()):
        print("Battleship sunk")
    if (p1_carrier.check() or p2_carrier.check()):
        print("Carrier sunk")
    if (p1_destroyer.check() or p2_destroyer.check()):
        print("Destroyer sunk")
    if (p1_submarine.check() or p2_submarine.check()):
        print("Submarine sunk")
    if (p1_cruiser.check() or p2_cruiser.check()):
        print("Cruiser sunk")
    if (p1_battleship.check() and p1_carrier.check() and p1_cruiser.check() and p1_destroyer.check()):
        return 2
    if (p2_battleship.check() and p2_carrier.check() and p2_cruiser.check() and p2_destroyer.check()):
        return 1
    else:
        return 0
        
# Controls a player's move
def move(player):
    hit_char = "x"
    miss_char = "o"
    
    if (player == 1):
        other = 2
    else:
        other = 1
        
    if (player ==  1):
        print(f"\nPlayer {other}'s hit grid")
        p1_hit_grid.display_grid()
        place = attack_validation(player)
        if ((p2_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) != "·"):
            p1_spots_attacked[place] = hit_char
            p1_hit_grid.grid[int(((place-(place%10))/10)), int((place%10))] = hit_char
            if ((p2_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) == "C"):
                p2_carrier.hit()
            if ((p2_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) == "B"):
                p2_battleship.hit()
            if ((p2_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) == "R"):
                p2_cruiser.hit()
            if ((p2_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) == "S"):
                p2_submarine.hit()
            if ((p2_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) == "D"):
                p2_destroyer.hit()
        else:
            p1_spots_attacked[place] = miss_char
            p1_hit_grid.grid[int(((place-(place%10))/10)), int((place%10))] = miss_char
        p1_hit_grid.display_grid()
    else: 
        print(f"Player {other}'s hit grid")
        p2_hit_grid.display_grid()
        place = attack_validation(player)
        if ((p1_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) != "·"):
            p2_spots_attacked[place] = hit_char
            p2_hit_grid.grid[int(((place-(place%10))/10)), int((place%10))] = hit_char
            if ((p1_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) == "C"):
                p1_carrier.hit()
            if ((p1_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) == "B"):
                p1_battleship.hit()
            if ((p1_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) == "R"):
                p1_cruiser.hit()
            if ((p1_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) == "S"):
                p1_submarine.hit()
            if ((p1_ship_grid.grid[int(((place-(place%10))/10)), int((place%10))]) == "D"):
                p1_destroyer.hit()
        else:
            p2_spots_attacked[place] = miss_char
            p2_hit_grid.grid[int(((place-(place%10))/10)), int((place%10))] = miss_char
        p2_hit_grid.display_grid()
 
def main_loop():
    who = 1
    winner = 0
    clear_screen()
    while (winner == 0):
        move(who)
        if (who == 1):
            who = 2
            winner = check_winner()
            cont = input("Press enter to continue...")
        else:
            who = 1
            winner = check_winner()
            cont = input("Press enter to continue...")
    clear_screen()
    print(f"Player {winner} is the winnner!")
            
def main():
    console_setup()
    p1_ship_grid.display_grid()
    set_ships(1)
    p1_ship_grid.display_grid()
    cont = input("Press enter to continue...")
    spots_used.clear()
    clear_screen()
    p2_ship_grid.display_grid()
    set_ships(2)
    p2_ship_grid.display_grid()
    cont = input("Press enter to continue...")
    main_loop()
    
if __name__ == "__main__":
    main()