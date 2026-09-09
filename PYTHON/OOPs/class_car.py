"""
car class
"""

class Car:

    brand_name:str
    variant:str
    color:str
    price:int
    mileage:int

    def __init__(self,brand_name,variant,color,price,mileage):

        self.brand_name = brand_name
        self.variant = variant
        self.color = color
        self.price = price
        self.mileage = mileage

    def get_car(self):

        print(self.brand_name,self.variant,self.color,self.price,self.mileage)

baleno_instance = Car("Baleno","Delta","Black",850000,22)
thar_instance = Car("Thar","AXT RWD","Black",1300000,13)

baleno_instance.get_car()
thar_instance.get_car()


    




