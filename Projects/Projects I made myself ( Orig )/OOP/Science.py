
class Formula:

    def __init__(self, pressure1, volume1):
        self.pressure1 = pressure1
        self.volume1 = volume1 


class Boyles(Formula):

    def __init__(self, pressure1, volume1, pressure2 , volume2):
        super().__init__(pressure1, volume1)
        self.pressure2 = pressure2
        self.volume2 = volume2

    def constant(self):
        return self.pressure1*self.volume1 / self.pressure2*self.volume2 

class Charles(Formula):
    
    def __init__(self, pressure1, volume1, volume2 , temperature1, temperature2 ):
        super().__init__(pressure1, volume1)
        self.volume2 = volume2
        self.temperature1 = temperature1
        self.temperature2 = temperature2
    
    def constant(self):
        return self.pressure1*1*self.temperature1*self.volume1 / self.temperature2*self.volume2

class GayLussac(Formula):

    def __init__(self, pressure1, pressure2, volume1, temperature1, temperature2):
        super().__init__(pressure1, volume1)
        self.pressure2 = pressure2
        self.temperature1 = temperature1
        self.temperature2 = temperature2

    def constant(self):
        return self.volume1*1*self.pressure1*self.temperature1 / self.pressure2*self.temperature2

boyles_law = Boyles(5,5,5,5)
charles_law = Charles(5,10,11,12,13)
gay_lussacs_law = GayLussac(1,20,30,200,32)
print(charles_law.constant())
print(boyles_law.constant())
print(gay_lussacs_law.constant())






