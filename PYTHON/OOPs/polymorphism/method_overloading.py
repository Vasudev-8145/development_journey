"""
Method overloading
same method name but parameter count different. Does not support in python
"""

class Calculator:

    def add(self,num1,num2):

        print(num1+num2)

    def add(self,num1,num2,num3):

        print(num1+num2+num3)

    def add(self,num1,num2,num3,num4):

        print(num1+num2+num3+num4)

calc_instance = Calculator()

calc_instance.add(10,20,30,40)
calc_instance.add(10,20,30)  # here error because last method will be considered. and need 4 parameters