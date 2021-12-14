class Ship:
    hitpoints = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2
    }

    initials = {
        "Carrier": 'C',
        "Battleship": 'B',
        "Cruiser": 'R',
        "Submarine": 'S',
        "Destroyer": 'D'
    }

    lookup_type = {
        'C': "Carrier",
        'B': "Battleship",
        'R': "Cruiser",
        'S': "Submarine",
        'D': "Destroyer"
    }

    def __init__(self, type):
        self.type = type
        self.hitpoints = Ship.hitpoints[type]
        self.initial = Ship.initials[type]
        self.sank = False
        
    def hit(self):
        self.hitpoints = self.hitpoints - 1
        if self.hitpoints == 0:
            self.sank = True
