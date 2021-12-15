from graphics import *
from ships import *

p1_ship_grid = Grid()
p1_hit_grid = Grid()
p2_ship_grid = Grid()
p2_hit_grid = Grid()

p1_ships = [Ship(type) for type in Ship.initials.keys()]
p2_ships = [Ship(type) for type in Ship.initials.keys()]

# These numbers correspond to how many of YOUR ships sank, not how many of your opponents ships you've sank
p1_ships_sank = 0
p2_ships_sank = 0


def set_ship(player, ship):
    valid = False
    while not valid:
        valid = True

        # Gets input from the user and validates it
        x, y = get_ship_location(player, ship.type, ship.hitpoints)
        direction = get_ship_direction()

        if direction == 'R':
            # Check if the ship is too long to be put at this position
            if y + ship.hitpoints > Grid.GRID_SIZE:
                print("Ship won't fit at this location!")
                valid = False

            # Make sure the positions where the ship will be set are free
            if valid:
                free = True
                for i in range(ship.hitpoints):
                    if player == 1:
                        free = free and p1_ship_grid.grid[x, y + i] == '.'
                    else:
                        free = free and p2_ship_grid.grid[x, y + i] == '.'
                if not free:
                    print("A ship is already in this location!")
                    valid = False

                # Place the ship in the appropriate grid if the location and direction are valid
                if valid:
                    for i in range(ship.hitpoints):
                        if player == 1:
                            p1_ship_grid.grid[x, y + i] = ship.initial
                        else:
                            p2_ship_grid.grid[x, y + i] = ship.initial
        elif direction == 'D':
            # Check if the ship is too long to be put at this position
            if x + ship.hitpoints > Grid.GRID_SIZE:
                print("Ship won't fit at this location!")
                valid = False

            # Make sure the positions where the ship will be set are free
            if valid:
                free = True
                for i in range(ship.hitpoints):
                    if player == 1:
                        free = free and p1_ship_grid.grid[x + i, y] == '.'
                    else:
                        free = free and p2_ship_grid.grid[x + i, y] == '.'
                if not free:
                    print("A ship is already in this location!")
                    valid = False

                # Place the ship in the appropriate grid if the location and direction are valid
                if valid:
                    for i in range(ship.hitpoints):
                        if player == 1:
                            p1_ship_grid.grid[x + i, y] = ship.initial
                        else:
                            p2_ship_grid.grid[x + i, y] = ship.initial

    # Display the grid once the ship has been placed
    if player == 1:
        p1_ship_grid.display_grid()
    else:
        p2_ship_grid.display_grid()


# This method sets the ships to the proper spots on the 'board' (or grid) depending on what the user inputs
def set_ships(player):
    if player == 1:
        for ship in p1_ships:
            set_ship(player, ship)
    else:
        for ship in p2_ships:
            set_ship(player, ship)


# Checks to see if the position the user inputted is either not given in the right format (ex. 'A' or 'F123'),
# and returns the x and y coordinates for the grid once it is
def get_ship_location(player, ship_type, ship_length):
    valid = False
    while not valid:
        valid = True
        place = input(f"\nWhere will Player {player} put the {ship_type} ({ship_length} spaces)? (ex. F5) ")
        if len(place) != 2:
            valid = False
            print("Input either too short or too long.")
        elif ord(place[0].upper()) not in range(65, 75) or not place[1].isdigit():
            valid = False
            print("Invalid location!")
    return convert_to_xy(place)


# Gets a valid direction for the ship
def get_ship_direction():
    direction = input("Which direction do you want to place the ship? (R)ight or (D)own: ").upper()
    while direction != 'R' and direction != 'D':
        direction = input("Invalid direction!\nWhich direction do you want to place the ship? (R)ight or (D)own: ").upper()
    return direction


# Gets the attack spot and ensures valid input and that the spot is available
def get_attack_location(player):
    valid = False
    while not valid:
        valid = True
        place = input(f"\nWhich square will Player {player} attack? (ex. F5) ")
        if len(place) != 2:
            valid = False
            print("Input either too short or too long.")
        elif ord(place[0].upper()) not in range(65, 75) or not place[1].isdigit():
            valid = False
            print("Invalid location!")
        else:
            x, y = convert_to_xy(place)
            if attack_check(player, x, y):
                valid = False
                print("That square has already been attacked!")
    return x, y


# Checks if the spot in the grid has already been attacked 
def attack_check(player, x, y):
    if player == 1:
        return p1_hit_grid.grid[x, y] != '.'
    elif player == 2:
        return p2_hit_grid.grid[x, y] != '.'


# Converts the alphanumeric location identifier to xy grid coordinates
def convert_to_xy(place):
    return letter_to_int(place[0].upper()), int(place[1])


# Sets the letter passed in to a number and returns it
def letter_to_int(letter):
    return ord(letter) - 65


# Checks for winner, returns which player won if there is and 0 if there isn't
def check_winner():
    if p1_ships_sank == 5:
        return 2
    elif p2_ships_sank == 5:
        return 1
    else:
        return 0


# Controls a player's move
def move(player):
    global p1_ships_sank
    global p2_ships_sank

    if player == 1:
        other = 2
    else:
        other = 1
        
    if player == 1:
        print(f"\nYour ship grid")
        p1_ship_grid.display_grid()
        print(f"\nYour hits grid")
        p1_hit_grid.display_grid()

        x, y = get_attack_location(player)

        # Process either a hit or miss
        if p2_ship_grid.grid[x, y] != ".":
            print(f"You hit Player {other}'s {Ship.lookup_type[p2_ship_grid.grid[x, y]]}!")
            p1_hit_grid.grid[x, y] = p2_ship_grid.grid[x, y]
            ship_hit = p2_ships[list(Ship.initials.values()).index(p2_ship_grid.grid[x, y])]
            ship_hit.hit()
            p2_ship_grid.grid[x, y] = 'X'
            if ship_hit.sank:
                print(f"You sank Player {other}'s {ship_hit.type}!")
                p2_ships_sank += 1
        else:
            print("You missed!")
            p1_hit_grid.grid[x, y] = 'X'
        p1_hit_grid.display_grid()
    else:
        print(f"\nYour ship grid")
        p2_ship_grid.display_grid()
        print(f"\nYour hits grid")
        p2_hit_grid.display_grid()

        x, y = get_attack_location(player)

        # Process either a hit or miss
        if p1_ship_grid.grid[x, y] != ".":
            print(f"You hit Player {other}'s {Ship.lookup_type[p1_ship_grid.grid[x, y]]}!")
            p2_hit_grid.grid[x, y] = p1_ship_grid.grid[x, y]
            ship_hit = p1_ships[list(Ship.initials.values()).index(p1_ship_grid.grid[x, y])]
            ship_hit.hit()
            p1_ship_grid.grid[x, y] = 'X'
            if ship_hit.sank:
                print(f"You sank Player {other}'s {ship_hit.type}!")
                p1_ships_sank += 1
        else:
            print("You missed!")
            p2_hit_grid.grid[x, y] = 'X'
        p2_hit_grid.display_grid()


def game_loop():
    current_player = 1
    winner = 0
    clear_screen()
    while winner == 0:
        move(current_player)
        if current_player == 1:
            current_player = 2
            winner = check_winner()
            input(f"Press enter to continue to Player {current_player}'s turn...")
        else:
            current_player = 1
            winner = check_winner()
            input(f"Press enter to continue to Player {current_player}'s turn...")
        clear_screen()
    clear_screen()
    print(f"\nPlayer {winner} is the winner!\n")
            

def main():
    print_title()
    p1_ship_grid.display_grid()
    set_ships(1)
    input("Press enter to continue to Player 2 ship setup...")
    clear_screen()
    p2_ship_grid.display_grid()
    set_ships(2)
    input("Press enter to continue to game...")
    game_loop()


if __name__ == "__main__":
    main()
