"""
Common 2D Shapes and Formulas
Rectangle:Multiply length (l) by width (w) (A = l × w)
Square: Multiply the side length (a) by itself (A = a²)
Circle: Multiply pi (π) by the radius squared (A = π r²)
Parallelogram: Multiply base (b) by vertical height (h) (A = bh).
Trapezium: Add parallel sides (a + b), multiply by height (h), and divide by two (A = ((a + b)h)/2).
"""

class Shape:

    name:str

    def __init__(self,name):
        self.name = name

class Rectangle(Shape):

    length:int
    width:int

    def __init__(self, name,length,width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):

        print(f"Area of {self.name} = {self.length*self.width}")

# rectangle_instance = Rectangle("Rectangle",10,12)
# rectangle_instance.area()

class Square(Shape):

    length:int

    def __init__(self, name,length):
        super().__init__(name)
        self.length = length

    def area(self):

        print(f"Area of {self.name} = {self.length**2}")

# square_instance = Square("Square",5)
# square_instance.area()

class Circle(Shape):

    radius:int

    def __init__(self, name,radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        print(f"Area of {self.name} = {3.14*(self.radius**2)}")

# circle_instamce = Circle("circle",7)
# circle_instamce.area()

class Parellelogram(Shape):

    base:int
    height:int

    def __init__(self, name,base,height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        print(f"Area of {self.name} = {self.base*self.height}")

# parellelogran_instance = Parellelogram("parellelogram",4,12)
# parellelogran_instance.area()

class Trapezium(Shape):

    parellel_side_a:int
    parellel_side_b:int
    height:int

    def __init__(self, name,parellel_side_a,parellel_side_b,height):
        super().__init__(name)
        self.parellel_side_a = parellel_side_a
        self.parellel_side_b = parellel_side_b
        self.height = height

    def area(self):
        print(f"Area of {self.name} = {((self.parellel_side_a+self.parellel_side_b)*self.height)/2}")

# trapezium_instance = Trapezium("trapezium",2,5,10)
# trapezium_instance.area()