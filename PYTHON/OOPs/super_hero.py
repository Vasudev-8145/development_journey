"""
class superhero attributes,methods
"""

class Superhero:

    name:str
    power:str
    universe:str

    def __init__(self,name,power,universe):

        self.name = name
        self.power = power
        self.universe = universe

    def get_superhero(self):

        print(self.name,self.power,self.universe)

superhero_instance1 = Superhero("Captain America","physical power","Marvel")

superhero_instance2 = Superhero("Iron Man","Suit","Marvel")

superhero_instance3 = Superhero("Minnal Murali","Run","Basil Joseph Universe")

superhero_instance1.get_superhero()
superhero_instance2.get_superhero()
superhero_instance3.get_superhero()