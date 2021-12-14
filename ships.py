class Ship:
    def __init__(self, hitpoints):  
        self.hitpoints = hitpoints
        
    def hit(self):
        self.hitpoints = self.hitpoints - 1
        
    def check(self):
        self.afloat = False
        if (self.hitpoints == 0):
            self.afloat = True
        return self.afloat
        
    