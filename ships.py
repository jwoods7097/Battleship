class Ship:
    def __init__(self, hitpoints, player):  
        self.hp = hitpoints
        self.player = player
        
    def hit(self):
        hitpoints -= 1